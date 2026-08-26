import json, os, sys, time, threading, queue, urllib.request, urllib.error

IN  = 'work/cds_variants.tsv'
OUT = 'work/vep_raw.jsonl'
URL = "https://rest.ensembl.org/vep/human/region"
BATCH = 200
WORKERS = 6

rows=[]
with open(IN) as f:
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<9: continue
        rows.append(p)
print("variants:", len(rows), flush=True)

# key -> genotype info
gt_map = {}
vcf_lines=[]
for c,pos,ref,alt,qual,gt,ad,dp,gq in rows:
    key=f"{c}_{pos}_{ref}_{alt}"
    gt_map[key]=dict(chrom=c,pos=int(pos),ref=ref,alt=alt,qual=float(qual),gt=gt,ad=ad,dp=dp,gq=gq)
    vcf_lines.append(f"{c} {pos} . {ref} {alt} . . .")
json.dump(gt_map, open('work/gt_map.json','w'))

done=set()
if os.path.exists(OUT):
    for line in open(OUT):
        try: done.add(json.loads(line)['_batch'])
        except: pass
print("resuming, batches done:", len(done), flush=True)

batches=[(i, vcf_lines[i:i+BATCH]) for i in range(0,len(vcf_lines),BATCH)]
q=queue.Queue()
for b in batches:
    if b[0] not in done: q.put(b)
total=q.qsize()
print("batches to run:", total, flush=True)

lock=threading.Lock()
fout=open(OUT,'a')
counter=[0]

def work():
    while True:
        try: idx, chunk = q.get_nowait()
        except queue.Empty: return
        payload={"variants":chunk,"canonical":1,"hgvs":1,"numbers":1,"mane":1,
                 "af":1,"af_gnomade":1,"af_gnomadg":1,"variant_class":1,"pick_order":["mane_select","canonical","rank"]}
        data=json.dumps(payload).encode()
        for attempt in range(6):
            try:
                req=urllib.request.Request(URL, data=data,
                    headers={"Content-Type":"application/json","Accept":"application/json"})
                r=json.load(urllib.request.urlopen(req, timeout=300))
                with lock:
                    for v in r:
                        v['_batch']=idx
                        fout.write(json.dumps(v)+"\n")
                    fout.flush()
                    counter[0]+=1
                    if counter[0]%10==0: print(f"  {counter[0]}/{total} batches", flush=True)
                break
            except urllib.error.HTTPError as e:
                wait = int(e.headers.get('Retry-After', 2**attempt)) if e.code==429 else 2**attempt
                time.sleep(min(wait,30))
            except Exception:
                time.sleep(2**attempt)
        else:
            with lock: print("BATCH FAILED", idx, flush=True)
        q.task_done()

ts=[threading.Thread(target=work) for _ in range(WORKERS)]
[t.start() for t in ts]; [t.join() for t in ts]
fout.close()
print("DONE", flush=True)
