import os, json, numpy as np, soundfile as sf, time
from kokoro import KPipeline
from script_segments import SEGMENTS

VOICE='af_heart'; SPEED=1.09; SR=24000
pipe=KPipeline(lang_code='a')
os.makedirs('audio',exist_ok=True)
timeline=[]; parts=[]; t=0.0
t0=time.time()
for i,(slide,cap,tts,pause) in enumerate(SEGMENTS):
    au=np.concatenate([a for _,_,a in pipe(tts, voice=VOICE, speed=SPEED)]).astype(np.float32)
    # trim leading/trailing near-silence
    thr=0.006
    idx=np.where(np.abs(au)>thr)[0]
    if len(idx): au=au[max(0,idx[0]-600):min(len(au),idx[-1]+900)]
    dur=len(au)/SR
    timeline.append(dict(i=i,slide=slide,caption=cap,start=round(t,3),end=round(t+dur,3),dur=round(dur,3),pause=pause))
    parts.append(au); parts.append(np.zeros(int(pause*SR),dtype=np.float32))
    t+=dur+pause
full=np.concatenate(parts)
# gentle normalise to -1.5 dBFS peak with soft limiting headroom
peak=np.abs(full).max()
full=full*(0.84/peak)
sf.write('audio/narration.wav', full, SR)
json.dump(timeline, open('audio/timeline.json','w'), indent=1)
print(f"voice={VOICE} speed={SPEED} segments={len(SEGMENTS)}")
print(f"TOTAL {t:.1f}s = {int(t//60)}:{t%60:04.1f}   (render {time.time()-t0:.0f}s)")
for s in range(1,7):
    d=sum(x['dur']+x['pause'] for x in timeline if x['slide']==s)
    print(f"  slide {s}: {d:5.1f}s")
