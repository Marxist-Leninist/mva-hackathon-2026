"""MVA hackathon Track 1 — genome-wide variant prioritisation, singleton WGS.

Pipeline:
  1. CDS+/-12bp PASS non-ref variants from the proband VCF (bcftools)
  2. VEP (Ensembl 112 REST) consequence + gnomAD AF, MANE-preferred transcript
  3. ClinVar exact REF/ALT match for clinical assertions
  4. Population-frequency and impact filters
  5. Inheritance modelling: homozygous / compound-het / hemizygous / de-novo-agnostic dominant
  6. HPO Resnik best-match-average phenotype score per gene
  7. Combined rank
"""
import json, collections, math, sys, os
sys.path.insert(0,'work')
from hpo_score import score_gene, gene_terms

gt_map=json.load(open('work/gt_map.json'))

# ---------- load VEP ----------
def pick(v):
    tcs=v.get('transcript_consequences') or []
    if not tcs: return None
    for t in tcs:
        if t.get('mane_select'): return t
    for t in tcs:
        if t.get('canonical'): return t
    order={'HIGH':0,'MODERATE':1,'LOW':2,'MODIFIER':3}
    return sorted(tcs,key=lambda t:order.get(t.get('impact','MODIFIER'),9))[0]

def gnomad_af(v, tc):
    best=0.0
    for cv in (v.get('colocated_variants') or []):
        fr=cv.get('frequencies') or {}
        for allele,d in fr.items():
            for k in ('gnomade','gnomadg','gnomade_nfe','gnomadg_nfe','af'):
                if k in d:
                    try: best=max(best,float(d[k]))
                    except: pass
    for k in ('gnomade_af','gnomadg_af'):
        if tc and tc.get(k) is not None:
            try: best=max(best,float(tc[k]))
            except: pass
    return best

recs={}
nline=0
for line in open('work/vep_raw.jsonl'):
    nline+=1
    try: v=json.loads(line)
    except: continue
    vs=v.get('vcf_string')
    if vs:
        c,p,r,a=vs.split('-'); key=f"{c}_{p}_{r}_{a}"
    else:
        ai=v.get('input','').split()
        if len(ai)>=5: key=f"{ai[0]}_{ai[1]}_{ai[3]}_{ai[4]}"
        else: continue
    tc=pick(v)
    if not tc: continue
    recs[key]=dict(
        gene=tc.get('gene_symbol') or tc.get('gene_id',''),
        conseq=",".join(tc.get('consequence_terms',[])),
        impact=tc.get('impact',''),
        hgvsc=tc.get('hgvsc',''), hgvsp=tc.get('hgvsp',''),
        transcript=tc.get('transcript_id',''),
        mane=bool(tc.get('mane_select')),
        af=gnomad_af(v,tc),
        sift=tc.get('sift_prediction',''), polyphen=tc.get('polyphen_prediction',''),
        exon=tc.get('exon',''), intron=tc.get('intron',''),
        biotype=tc.get('biotype',''),
    )
print(f"VEP json lines={nline} annotated variants={len(recs)}", flush=True)

# ---------- ClinVar exact match ----------
clin={}
for line in open('work/clinvar_hits.tsv'):
    p=line.rstrip('\n').split('\t')
    if len(p)<8: continue
    c,pos,ref,alts,sig,rev,gi,dn=p[:8]
    for a in alts.split(','):
        clin[f"{c}_{pos}_{ref}_{a}"]=dict(sig=sig, rev=rev, gene=gi, dis=dn)
print("clinvar exact-matchable records:", len(clin), flush=True)

HIGH={'transcript_ablation','splice_acceptor_variant','splice_donor_variant','stop_gained',
      'frameshift_variant','stop_lost','start_lost','transcript_amplification'}
MODER={'inframe_insertion','inframe_deletion','missense_variant','protein_altering_variant',
       'splice_region_variant','splice_donor_5th_base_variant','splice_donor_region_variant',
       'splice_polypyrimidine_tract_variant'}

AF_REC = 0.01     # recessive: allow up to 1% (carrier freq)
AF_DOM = 0.0005   # dominant: much stricter

cand=[]
for key,r in recs.items():
    g=gt_map.get(key)
    if not g: continue
    if r['biotype'] not in ('protein_coding',''): continue
    terms=set(r['conseq'].split(','))
    if terms & HIGH: cls='HIGH'
    elif terms & MODER: cls='MODERATE'
    else: continue
    cv=clin.get(key,{})
    cand.append(dict(key=key, **r, **g, clnsig=cv.get('sig',''), clnrev=cv.get('rev',''), clndn=cv.get('dis','')))
print("HIGH/MODERATE coding candidates:", len(cand), flush=True)

# ---------- inheritance modelling ----------
by_gene=collections.defaultdict(list)
for c in cand: by_gene[c['gene']].append(c)

def is_hom(c): return c['gt'] in ('1/1','1|1')
def is_het(c): return c['gt'] in ('0/1','1/0','0|1','1|0')
def rare_rec(c): return c['af'] <= AF_REC
def rare_dom(c): return c['af'] <= AF_DOM

events=[]
for gene, vs in by_gene.items():
    hom=[c for c in vs if is_hom(c) and rare_rec(c) and c['af']<=0.005]
    het=[c for c in vs if is_het(c) and rare_rec(c)]
    hp_score,_=score_gene(gene)
    for c in hom:
        events.append(dict(gene=gene, model='homozygous', v1=c, v2=None, hpo=hp_score))
    # compound het: at least one HIGH, or two MODERATE that are rare
    if len(het)>=2:
        het_s=sorted(het, key=lambda x:(0 if x['impact']=='HIGH' else 1, x['af']))
        # only build pairs among the most damaging few, require both rare (<1%) and at least one <0.1%
        top=het_s[:6]
        for i in range(len(top)):
            for j in range(i+1,len(top)):
                a,b=top[i],top[j]
                if min(a['af'],b['af'])>0.001: continue
                if a['impact']!='HIGH' and b['impact']!='HIGH':
                    if not (a['af']<=0.0005 and b['af']<=0.0005): continue
                events.append(dict(gene=gene, model='compound_het', v1=a, v2=b, hpo=hp_score))
    for c in vs:
        if is_het(c) and rare_dom(c) and c['impact']=='HIGH':
            events.append(dict(gene=gene, model='dominant_het', v1=c, v2=None, hpo=hp_score))

print("inheritance events:", len(events), flush=True)

def sev(c):
    s=0.0
    if c['impact']=='HIGH': s+=6
    elif c['impact']=='MODERATE': s+=2.5
    if 'missense' in c['conseq'] and c.get('polyphen')=='probably_damaging': s+=1.0
    if 'missense' in c['conseq'] and c.get('sift')=='deleterious': s+=1.0
    sg=(c.get('clnsig') or '')
    if 'Pathogenic' in sg and 'Conflicting' not in sg: s+=5
    elif 'Likely_pathogenic' in sg: s+=4
    elif 'Benign' in sg: s-=6
    if c['af']==0: s+=2.0
    elif c['af']<1e-4: s+=1.5
    elif c['af']<1e-3: s+=0.8
    if c.get('mane'): s+=0.3
    if float(c.get('gq',0) or 0)>=90: s+=0.2
    return s

for e in events:
    s=sev(e['v1'])+(sev(e['v2']) if e['v2'] else 0)
    if e['model']=='compound_het': s*=0.62      # normalise two-variant events
    if e['model']=='dominant_het': s*=0.55      # singleton: cannot show de novo
    e['sev']=s
    e['score']=s + 0.55*e['hpo']

events.sort(key=lambda e:-e['score'])
json.dump(events, open('work/events.json','w'), default=str)

print()
print(f"{'#':<4}{'GENE':<12}{'MODEL':<15}{'SCORE':<8}{'SEV':<7}{'HPO':<7}{'VARIANT(S)':<60}")
seen=set()
n=0
for e in events:
    if e['gene'] in seen: continue
    seen.add(e['gene']); n+=1
    if n>35: break
    def d(c):
        if not c: return ''
        return f"{c['chrom']}:{c['pos']}{c['ref']}>{c['alt']}[{c['gt']},af={c['af']:.2g},{c['impact'][:4]}]"
    print(f"{n:<4}{e['gene'][:11]:<12}{e['model']:<15}{e['score']:<8.2f}{e['sev']:<7.2f}{e['hpo']:<7.2f}{d(e['v1'])+' | '+d(e['v2']):<60}")
