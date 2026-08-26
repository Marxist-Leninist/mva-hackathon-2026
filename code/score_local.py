import csv, sys
Variant = tuple
GT_LOCAL = {"PROBAND01": frozenset([("chr15",40209701,"T","G"),("chr15",40220612,"T","G")])}
RANK_TIERS = [(1,100),(3,50),(5,25),(10,10)]
def rank_pts(r):
    for mx,p in RANK_TIERS:
        if r<=mx: return p
    return 0
rows=[]
with open(sys.argv[1], newline='') as f:
    for row in csv.DictReader(f):
        v1=(row['chrom_1'].strip(),int(row['pos_1']),row['ref_1'].strip().upper(),row['alt_1'].strip().upper())
        if row.get('chrom_2') and row['chrom_2'].strip():
            vs=frozenset([v1,(row['chrom_2'].strip(),int(row['pos_2']),row['ref_2'].strip().upper(),row['alt_2'].strip().upper())])
        else:
            vs=frozenset([v1])
        e=float(row['epcr']); assert 0<e<=1
        rows.append((vs,e))
rows.sort(key=lambda x:-x[1])
true_v=GT_LOCAL['PROBAND01']
full=part=None
for i,(vs,e) in enumerate(rows,1):
    if vs==true_v and full is None: full=i
for i,(vs,e) in enumerate(rows,1):
    if vs&true_v and part is None: part=i
rp = rank_pts(full) if full else (0.5*rank_pts(part) if part else 0)
thrs=sorted({e for _,e in rows},reverse=True)
best=0
for t in thrs:
    pred=set()
    for vs,e in rows:
        if e>=t: pred|=vs
    tp=len(pred&true_v); fp=len(pred-true_v); fn=len(true_v-pred)
    prec=tp/(tp+fp) if tp+fp else 0; rec=tp/(tp+fn) if tp+fn else 0
    f1=2*prec*rec/(prec+rec) if prec+rec else 0
    if f1>best: best=f1
print(f'rank_points={rp:.1f} f_max={best:.3f} full_match_rank={full} partial={part} rows={len(rows)}')
