# Track 2 pitch video — build

Fully reproducible, no recording and no editing software. Everything here runs headless on CPU.

| | |
|---|---|
| Output | `MVA_Track2_pitch_MarxistLeninist.mp4` — 2:59.7, 1920×1080, H.264/AAC, ~7.7 MB |
| Narration | **Kokoro-82M** (`hexgrad/Kokoro-82M`), voice `af_heart`, speed 1.07, rendered per sentence |
| Slides | HTML + CSS → headless Chromium (Playwright) screenshots at 1920×1080 |
| Figure | `pipeline/genomewide/bubr1_dosage_model.py` → matplotlib |
| Assembly | ffmpeg — 0.45 s crossfades, drawbox caption band, burned-in ASS captions |
| Audio | loudnorm to **−16.5 LUFS**, true peak −1.5 dBTP, 70 Hz high-pass |

## Why this way

The narration is generated per sentence rather than as one take, so each line's real duration is
measured and the slide timings are derived from the audio — not guessed. That means the deck never
drifts out of sync, and the script can be re-cut and rebuilt in about four minutes.

Captions are burned into a dedicated band reserved in the slide layout (bottom 142 px), with an
explicit-`PlayRes` ASS file rather than an SRT, so libass does no coordinate guessing. Judges often
watch the first pass muted; the argument has to survive that.

## Rebuild

```bash
pip install kokoro soundfile playwright matplotlib
apt-get install -y espeak-ng ffmpeg

python pipeline/genomewide/make_audio.py     # narration + timeline.json
python pipeline/genomewide/make_slides.py    # slide1..6.png
python pipeline/genomewide/build_video.py    # captions + mux
```

Edit `pipeline/genomewide/script_segments.py` to change the script; slide durations follow
automatically from the rendered audio.

## Slide order

1. The answer — both variants, ClinVar assertion, genotype architecture
2. Mechanism — null + hypomorph → 5–10% residual BUBR1. *Not a broken protein. A scarce one.*
3. The dosage window — 1.3–2.6× is the target
4. The framing error — aneuploidy-selective lethality is inverted when the patient is the aneuploid organism
5. Vincristine needs the checkpoint. He doesn't have one.
6. The experiment and the pre-registered gate
