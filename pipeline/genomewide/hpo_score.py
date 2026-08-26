"""Resnik/Phenomizer-style HPO semantic similarity: gene -> proband phenotype score.
Builds the HPO DAG from hp.obo, derives information content from gene-annotation
frequency, and scores each gene by symmetric best-match-average similarity."""
import json, math, collections, sys

OBO='ref/hp.obo'; P2G='ref/phenotype_to_genes.txt'

# ---- parse hp.obo -> parents, alt_id map, obsolete set
parents=collections.defaultdict(set); alt2main={}; obsolete=set(); names={}
cur=None; is_ob=False
for line in open(OBO):
    line=line.rstrip('\n')
    if line=='[Term]': cur=None; is_ob=False; continue
    if line.startswith('id: HP:'): cur=line[4:]; continue
    if cur is None: continue
    if line.startswith('name: '): names[cur]=line[6:]
    elif line.startswith('is_a: '): parents[cur].add(line[6:].split(' ')[0])
    elif line.startswith('alt_id: '): alt2main[line[8:]]=cur
    elif line=='is_obsolete: true': obsolete.add(cur)

def ancestors(t, cache={}):
    t=alt2main.get(t,t)
    if t in cache: return cache[t]
    seen=set(); stack=[t]
    while stack:
        x=stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(parents.get(x,()))
    cache[t]=seen
    return seen

# ---- gene -> set(HPO terms), from phenotype_to_genes
gene_terms=collections.defaultdict(set)
term_genes=collections.defaultdict(set)
with open(P2G) as f:
    hdr=f.readline()
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<4: continue
        hp, gene = p[0], p[3]
        if not hp.startswith('HP:'): continue
        gene_terms[gene].add(hp); term_genes[hp].add(gene)

# ---- information content, propagated to ancestors
N=len(gene_terms)
anc_genes=collections.defaultdict(set)
for g,ts in gene_terms.items():
    allanc=set()
    for t in ts: allanc |= ancestors(t)
    for a in allanc: anc_genes[a].add(g)
IC={t: -math.log(max(len(gs),1)/N) for t,gs in anc_genes.items()}
maxIC=max(IC.values()) if IC else 1.0

def resnik(a,b):
    ca = ancestors(a) & ancestors(b)
    if not ca: return 0.0
    return max(IC.get(x,0.0) for x in ca)

PROBAND=["HP:0002859","HP:0000121","HP:0004322","HP:0001508",
         "HP:0003202","HP:0001622","HP:0001518","HP:0200067"]

def score_gene(gene):
    ts = gene_terms.get(gene)
    if not ts: return 0.0, {}
    fwd=[]; detail={}
    for q in PROBAND:
        best=0.0; bt=None
        for t in ts:
            s=resnik(q,t)
            if s>best: best=s; bt=t
        fwd.append(best)
        if bt: detail[q]=(bt, names.get(bt,''), round(best,2))
    rev=[]
    for t in ts:
        best=max((resnik(q,t) for q in PROBAND), default=0.0)
        rev.append(best)
    bma = 0.5*(sum(fwd)/len(fwd) + sum(rev)/max(len(rev),1))
    return bma/maxIC*100.0, detail

if __name__=='__main__':
    genes=sys.argv[1:] or ['BUB1B','CEP57','TRIP13','CYP24A1','SLC34A1','CLDN16','TP53','DICER1','NF1','ATP6V1B1']
    print(f"{'GENE':<12} {'HPOscore':<10} best-matches")
    for g in genes:
        s,d=score_gene(g)
        bm="; ".join(f"{names.get(q,q)[:18]}->{v[1][:22]}({v[2]})" for q,v in list(d.items())[:4])
        print(f"{g:<12} {s:<10.2f} {bm}")
    json.dump({'ok':True}, open('work/hpo_ready.json','w'))
