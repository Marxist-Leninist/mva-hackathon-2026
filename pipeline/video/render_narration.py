#!/usr/bin/env python3
"""Render the Track 2 pitch narration with Kokoro-82M.

Why Kokoro rather than the highest-ELO model available: the binding constraint
here is credentials, not quality ranking. Cartesia Sonic and ElevenLabs v3 need
paid API access this project does not have. Kokoro-82M is Apache-2.0, runs on
CPU in minutes, needs no account, and is far above the flite baseline the first
cut of this video used.

Renders one WAV per script segment so the editor can place them against fixed
slide timings without re-cutting, plus a single concatenated track with
configurable inter-segment pauses.
"""
import argparse
import json
import os
import sys
import wave

import numpy as np
import soundfile as sf

SAMPLE_RATE = 24000


def synth_segment(pipeline, text, voice, speed):
    """Kokoro yields per-sentence chunks; concatenate them into one segment."""
    chunks = []
    for _graphemes, _phonemes, audio in pipeline(text, voice=voice, speed=speed):
        if audio is None:
            continue
        arr = audio.detach().cpu().numpy() if hasattr(audio, "detach") else np.asarray(audio)
        chunks.append(arr.astype(np.float32))
    if not chunks:
        raise RuntimeError("Kokoro produced no audio for a segment")
    return np.concatenate(chunks)


def peak_normalise(x, target_dbfs=-1.5):
    peak = float(np.max(np.abs(x)))
    if peak == 0:
        return x
    target = 10 ** (target_dbfs / 20.0)
    return x * (target / peak)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--segments", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--voice", default="bm_george")
    ap.add_argument("--speed", type=float, default=0.95)
    ap.add_argument("--gap", type=float, default=0.55,
                    help="seconds of silence between segments in the joined track")
    ap.add_argument("--lang-code", default="b", help="'b' British English, 'a' American")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    spec = json.load(open(args.segments))
    segments = spec["segments"]

    from kokoro import KPipeline
    pipeline = KPipeline(lang_code=args.lang_code)

    joined, manifest = [], []
    gap = np.zeros(int(SAMPLE_RATE * args.gap), dtype=np.float32)

    for seg in segments:
        audio = peak_normalise(synth_segment(pipeline, seg["text"], args.voice, args.speed))
        dur = len(audio) / SAMPLE_RATE
        path = os.path.join(args.outdir, f"{seg['id']}_{args.voice}.wav")
        sf.write(path, audio, SAMPLE_RATE)

        words = len(seg["text"].split())
        manifest.append({
            "id": seg["id"], "slide": seg.get("slide"),
            "target_window": seg.get("target_window"),
            "file": os.path.basename(path),
            "duration_s": round(dur, 2),
            "words": words,
            "wpm": round(words / (dur / 60.0), 1) if dur else None,
        })
        print(f"  {seg['id']:<14} {dur:6.2f}s  {words:>3} words  "
              f"{words/(dur/60.0):5.1f} wpm  -> {os.path.basename(path)}", flush=True)

        joined.append(audio)
        joined.append(gap)

    full = np.concatenate(joined[:-1])  # drop trailing gap
    full_path = os.path.join(args.outdir, f"narration_full_{args.voice}.wav")
    sf.write(full_path, full, SAMPLE_RATE)
    total = len(full) / SAMPLE_RATE

    out = {
        "voice": args.voice, "speed": args.speed, "gap_s": args.gap,
        "sample_rate": SAMPLE_RATE,
        "total_duration_s": round(total, 2),
        "total_duration_mmss": f"{int(total // 60)}:{int(total % 60):02d}",
        "segments": manifest,
    }
    json.dump(out, open(os.path.join(args.outdir, f"manifest_{args.voice}.json"), "w"), indent=2)
    print(f"\nTOTAL {out['total_duration_mmss']} ({total:.1f}s) -> {os.path.basename(full_path)}")
    if total > 180:
        print(f"  WARNING: exceeds the 3-minute limit by {total - 180:.1f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
