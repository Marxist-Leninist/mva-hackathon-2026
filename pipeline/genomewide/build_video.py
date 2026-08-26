import json, subprocess, os, math

TL = json.load(open('audio/timeline.json'))
AUD = 'audio/narration.wav'
total = TL[-1]['end'] + TL[-1]['pause']

# ---- slide boundaries from the narration timeline
bounds = {}
for x in TL:
    s = x['slide']
    b = bounds.setdefault(s, [x['start'], 0.0])
    b[1] = x['end'] + x['pause']
slides = sorted(bounds)
segs = [(s, bounds[s][0], bounds[s][1]) for s in slides]
segs[-1] = (segs[-1][0], segs[-1][1], total)
for s, a, b in segs:
    print(f"slide {s}: {a:7.2f} -> {b:7.2f}  ({b-a:5.2f}s)")

# ---- ASS captions (explicit PlayRes so libass does no guessing)
def ats(t):
    h=int(t//3600); m=int(t%3600//60); sec=t%60
    return f"{h:d}:{m:02d}:{sec:05.2f}"
ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,40,&H001A1312,&H000000FF,&H00F5EFED,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,2,190,190,38,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
with open('audio/captions.ass','w') as f:
    f.write(ASS_HEAD)
    for x in TL:
        end = x['end'] + min(x['pause'], 0.35)
        txt = x['caption'].replace('\n',' ')
        f.write(f"Dialogue: 0,{ats(x['start'])},{ats(end)},Cap,,0,0,0,,{txt}\n")
print("captions written:", len(TL))

# ---- video: stills + crossfades + burned captions + audio
XF = 0.45
inputs, filt = [], []
for i, (s, a, b) in enumerate(segs):
    dur = (b - a) + (XF if i < len(segs)-1 else 0)
    inputs += ['-loop','1','-t',f'{dur:.3f}','-i',f'slides/slide{s}.png']
    filt.append(f"[{i}:v]scale=1920:1080,setsar=1,format=yuv420p[v{i}]")
prev, acc = 'v0', segs[0][2]-segs[0][1]
for i in range(1, len(segs)):
    out = f'x{i}'
    filt.append(f"[{prev}][v{i}]xfade=transition=fade:duration={XF}:offset={acc-XF:.3f}[{out}]")
    prev = out
    acc += (segs[i][2]-segs[i][1])
filt.append(f"[{prev}]drawbox=x=0:y=938:w=1920:h=142:color=0xEDEFF5@1.0:t=fill,drawbox=x=0:y=938:w=1920:h=3:color=0xD8DCE6@1.0:t=fill[band]");
filt.append(f"[band]ass=audio/captions.ass[vout]")

cmd = ['ffmpeg','-y'] + inputs + ['-i',AUD,
       '-filter_complex',';'.join(filt),
       '-map','[vout]','-map',f'{len(segs)}:a',
       '-c:v','libx264','-preset','slow','-crf','19','-pix_fmt','yuv420p','-r','30',
       '-c:a','aac','-b:a','192k','-ar','48000',
       '-movflags','+faststart','-shortest',
       'out/MVA_Track2_pitch_MarxistLeninist.mp4']
print("running ffmpeg...")
RAW = 'out/MVA_Track2_pitch_MarxistLeninist.mp4'
FINAL = 'out/MVA_Track2_pitch_MarxistLeninist_final.mp4'
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode:
    print(r.stderr[-2500:])
    raise SystemExit(1)
print("OK")

# ---- loudness normalisation (two-pass EBU R128)
# make_audio.py peak-normalises, which is not the same thing: this mux measured
# -23.8 LUFS integrated, roughly 7 LU below the ~-14 LUFS platforms normalise
# to. A quiet, narrow-range source sounds weak next to other submissions, and a
# judge should not have to reach for the volume. Two-pass rather than one so the
# gain is computed from the real measurement instead of a running estimate.
def measure(path):
    p = subprocess.run(
        ['ffmpeg','-hide_banner','-nostats','-i',path,
         '-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],
        capture_output=True, text=True)
    blob = p.stderr[p.stderr.rindex('{'):p.stderr.rindex('}')+1]
    return json.loads(blob)

m = measure(RAW)
print(f"measured: {m['input_i']} LUFS, TP {m['input_tp']} dBFS")
norm = (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={m['input_i']}:"
        f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
        f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
r2 = subprocess.run(
    ['ffmpeg','-y','-v','error','-i',RAW,'-af',norm,
     '-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000',
     '-movflags','+faststart', FINAL],
    capture_output=True, text=True)
if r2.returncode:
    print(r2.stderr[-2000:])
    raise SystemExit(1)
print(f"normalised -> {FINAL}")
