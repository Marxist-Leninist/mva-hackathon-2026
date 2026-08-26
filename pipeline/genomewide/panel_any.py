import json,sys
sys.path.insert(0,'work')
gt=json.load(open('work/gt_map.json'))
# rebuild the full candidate table (not just inheritance-filtered)
import importlib.util
recs={}
def pick(v):
    tcs=v.get('transcript_consequences') or []
    if not tcs: return None
    for t in tcs:
        if t.get('mane_select'): return t
    for t in tcs:
        if t.get('canonical'): return t
    return tcs[0]
def af_of(v):
    best=0.0
    for cv in (v.get('colocated_variants') or []):
        for a,d in (cv.get('frequencies') or {}).items():
            for k in ('gnomade','gnomadg','af'):
                if k in d:
                    try: best=max(best,float(d[k]))
                    except: pass
    return best
clin={}
for line in open('work/clinvar_hits.tsv'):
    p=line.rstrip('\n').split('\t')
    if len(p)<8: continue
    for a in p[3].split(','):
        clin[f"{p[0]}_{p[1]}_{p[2]}_{a}"]=(p[4],p[7])
NEPHRO=set("""CYP24A1 SLC34A1 SLC34A3 CLDN16 CLDN19 ATP6V1B1 ATP6V0A4 SLC4A1 AGXT GRHPR HOGA1 CASR SLC12A1
KCNJ1 CLCNKB BSND FAM20A VDR CA2 SLC9A3R1 CLCN5 OCRL SLC7A9 SLC3A1 AVPR2 AQP2 CYP27B1 GNA11 AP2S1 TRPM6
CNNM2 XDH APRT SLC26A1 TRPV5 TRPV6 CLDN14 MAGED2 KCNJ16 HNF1B PAX2 UMOD SLC12A3 CLDN10 CTNS SLC7A7""".split())
WATCH = NEPHRO | set("PEX5 PEX1 PEX6 PEX26 SERPINA1 TP53 DICER1 CEP57 TRIP13 MAD1L1 BUB1 CENPE".split())
out=[]
for line in open('work/vep_raw.jsonl'):
    v=json.loads(line)
    vs=v.get('vcf_string')
    if not vs: continue
    c,p,r,a=vs.split('-'); key=f"{c}_{p}_{r}_{a}"
    tc=pick(v)
    if not tc: continue
    g=tc.get('gene_symbol','')
    if g not in WATCH: continue
    gg=gt.get(key)
    if not gg: continue
    cons=",".join(tc.get('consequence_terms',[]))
    if tc.get('impact') not in ('HIGH','MODERATE'): continue
    cs=clin.get(key,('',''))
    out.append((g,gg['chrom'],gg['pos'],gg['ref'],gg['alt'],gg['gt'],gg['dp'],gg['gq'],af_of(v),
                tc.get('impact'),cons[:30],(tc.get('hgvsp') or '').split(':')[-1],cs[0][:40]))
out.sort(key=lambda x:(x[0],x[2]))
print(f"{'GENE':<10}{'POS':<20}{'GT':<6}{'DP':<5}{'GQ':<5}{'gnomAD':<11}{'IMP':<10}{'CONSEQ':<31}{'HGVSp':<18}CLINVAR")
for r in out:
    print(f"{r[0]:<10}{r[1]+':'+str(r[2]):<20}{r[5]:<6}{r[6]:<5}{r[7]:<5}{r[8]:<11.3g}{r[9]:<10}{r[10]:<31}{(r[11] or '')[:17]:<18}{r[12]}")
