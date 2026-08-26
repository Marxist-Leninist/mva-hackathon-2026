#!/usr/bin/env python3
"""Correct the false and overclaimed statements in the pitch-video build source.

Three defects, all in material that is spoken aloud or rendered on screen:

1. FALSE. "Absent from gnomAD and ClinVar" / "absent from gnomAD". gnomAD v4
   exomes report 15-40220612-T-G at AC=1, AN=1,461,878 (AF 6.84e-07). It is
   absent from gnomAD *genomes* only. The written repo was corrected earlier;
   the video build was not, so the claim survived into the narration, the
   burned-in captions and slide 1. A judging panel can check it in under a
   minute.

2. OVERCLAIM. The slide-1 badge reads "compound het". Phase is inferred, not
   demonstrated — the variants are 10,911 bp apart with no parental samples and
   no read-backed phase, which ClinGen SVI scores PM3_Supporting. The agreed
   wording everywhere else is "candidate biallelic".

3. OVERCLAIM. p.Asn1002Lys is labelled "hypomorph" as established fact. It is
   predicted, not demonstrated; there is a counterexample in the same published
   series (Q921H, same domain, functionally normal), and the Track 2 report
   states an explicit kill condition against exactly this assumption.

Captions are generated at build time from script_segments.py, so correcting the
narration source fixes the spoken line and the burned-in caption together. The
archived reports/pitch_captions.ass copy is updated for consistency.

Every replacement is exact-match and asserted, so this fails loudly rather than
silently no-op'ing if the surrounding text has moved.
"""
import sys

REPLACEMENTS = [
    # --- 1. narration (drives both audio and generated captions) -----------
    (
        "pipeline/genomewide/script_segments.py",
        ' (1,"And a novel missense at asparagine 1002, absent from gnomAD, in the pseudokinase domain.",\n'
        '    "And a novel missense at asparagine one thousand and two, absent from gnomad, '
        'in the pseudokinase domain.",0.45),',
        ' (1,"And a novel missense at asparagine 1002 — one allele in 1.5 million — in the pseudokinase domain.",\n'
        '    "And a novel missense at asparagine one thousand and two. One allele in one and a half million. '
        'In the pseudokinase domain.",0.45),',
    ),
    # --- 2. slide 1 frequency line -----------------------------------------
    (
        "pipeline/genomewide/make_slides.py",
        '   <div class="n">Absent from gnomAD and ClinVar · novel</div></div>',
        '   <div class="n">gnomAD v4 exomes: 1 in 1,461,878 (AF 6.8&times;10<sup>-7</sup>) · '
        'unreported in ClinVar</div></div>',
    ),
    # --- 3. slide 1 phase badge --------------------------------------------
    (
        "pipeline/genomewide/make_slides.py",
        '<span class="pill">BUB1B · compound het</span>',
        '<span class="pill">BUB1B · candidate biallelic</span>',
    ),
    # --- 4. slide 1 hypomorph badge ----------------------------------------
    (
        "pipeline/genomewide/make_slides.py",
        '— pseudokinase domain <span class="pill">hypomorph</span>',
        '— pseudokinase domain <span class="pill">predicted hypomorph</span>',
    ),
    # --- 5. archived caption copy ------------------------------------------
    (
        "reports/pitch_captions.ass",
        "And a novel missense at asparagine 1002, absent from gnomAD, in the pseudokinase domain.",
        "And a novel missense at asparagine 1002 — one allele in 1.5 million — in the pseudokinase domain.",
    ),
]


def main():
    failures = []
    for path, old, new in REPLACEMENTS:
        try:
            text = open(path, encoding="utf-8").read()
        except FileNotFoundError:
            failures.append(f"{path}: file not found")
            continue
        n = text.count(old)
        if n != 1:
            failures.append(f"{path}: expected exactly 1 occurrence, found {n}")
            continue
        open(path, "w", encoding="utf-8").write(text.replace(old, new))
        print(f"fixed {path}: {old.strip()[:60]}...")
    if failures:
        print("\nNOT APPLIED:", file=sys.stderr)
        for f in failures:
            print("  " + f, file=sys.stderr)
        sys.exit(1)
    print("\nAll corrections applied. The video MUST be rebuilt from this source; "
          "the existing MP4 still carries the old text in audio, captions and slide 1.")


if __name__ == "__main__":
    main()
