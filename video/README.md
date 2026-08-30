# Track 2 pitch video — superseded historical build assets

The previous 2:59.7 MP4 has been removed from the review branch because its
scientific wording predates the 30 August 2026 Track 2 report reconciliation.
It must not be uploaded as the final Hackathon pitch.

The remaining slide images and audio are retained only as historical build
artifacts and as a reference for the rendering pipeline. They include wording
that is no longer acceptable in the final submission, including:

- treating a child-specific 5-10% BUBR1 estimate as measured rather than as a
  scenario;
- presenting the 1.3-2.6-fold planning range too definitively; and
- a vincristine/oncology section unsupported by patient-specific response data.

## Canonical source for the replacement

Use:

`reports/pitch_script_track2_revised_20260830.md`

The replacement script is aligned with the revised report. It states that phase
is unproven, `p.Asn1002Lys` remains a VUS, the missense mechanism is unmeasured,
and no treatment or oncology change is recommended.

## Rebuild requirements

The historical pipeline is CPU/headless and may be reused after replacing its
script, slide content and captions from one source of truth:

```bash
pip install kokoro soundfile playwright matplotlib
apt-get install -y espeak-ng ffmpeg

python pipeline/genomewide/make_audio.py
python pipeline/genomewide/make_slides.py
python pipeline/genomewide/build_video.py
```

Before running those commands, update the pipeline inputs so they reproduce the
canonical revised pitch rather than the historical six-slide script.

The rebuilt final asset must then be checked for:

- runtime of no more than 180 seconds;
- complete audio/video decode;
- 1920x1080 H.264 video with AAC audio;
- synchronized burned-in captions;
- no old 5-10%, 1.3-2.6-fold, or vincristine claims presented as patient facts;
- one-frame-per-slide visual review; and
- full playback after upload to YouTube or Vimeo.

Do not restore the removed MP4. Commit only the report-aligned rebuilt version.
