# MVA Hackathon submission checklist

Nothing in this file authorizes a submission. Re-check the live form and obtain
the participant's explicit confirmation immediately before using a submission
slot.

## Canonical source of truth

- Manifest: `competition/CANONICAL.json`
- Canonical version: `2026-08-30.4`
- Agent protocol: `competition/coordination/AGENT_PROTOCOL.md`
- Alternate Track 2 report sources: forbidden and checked by `make check`

## Track 1

- Team / display name: `MarxistLeninist`
- GitHub repository: `https://github.com/Marxist-Leninist/mva-hackathon-2026`
- Predictions file: `results/MarxistLeninist_bub1b_compound_het.csv`
- Report file: `reports/MarxistLeninist_track1_report.md`
- Expected local validation: `make check` passes
- Primary row count: `1`
- Finding type: `primary`
- Proband identifier: `PROBAND01`
- Coordinate build and format: `GRCh38`, `chr15`
- Phase disclosure: in trans inferred, not proven

Before submitting Track 1:

1. Fetch the current files from the default branch and confirm their hashes or
   contents match the reviewed versions.
2. Confirm the GitHub Actions `public-release-checks` workflow is green.
3. Confirm the live form still shows unused quota and unchanged schema.
4. Confirm the participant wants this slot used.
5. Record the submission time, returned score, and leaderboard URL without
   publishing gated data.

## Track 2

### Required form fields

- Team / display name: `MarxistLeninist`
- GitHub repository: `https://github.com/Marxist-Leninist/mva-hackathon-2026`
- Report file: `competition/artifacts/MarxistLeninist_track2_report.pdf`
- Editable report source: `reports/MarxistLeninist_track2_report.md`
- Pitch source: `reports/pitch_script_track2_revised_20260830.md`
- Pitch file: `competition/artifacts/MarxistLeninist_track2_pitch.mp4`
- Pitch-video URL: **pending YouTube or Vimeo upload**
- Notes for judges: use the reviewed text below

### Current live-form rule and usage

The Track 2 form permits up to **three submissions**. Submission 1 has been
received, so **two submissions remain**. The independent panel reviews only the
**latest** entry.

The Submission 1 receipt and exact supplied artifacts are archived under
`competition/history/submission-01/`. They are historical and do not replace
the current canonical v4 artifacts. Its YouTube URL is not the hosting URL for
the current canonical pitch.

### Required participant-controlled fields still open

- [x] Provider plans verified: OpenAI ChatGPT Pro and Anthropic Claude Max
      20x, including Claude Code.
- [ ] Confirm and record the relevant account-level training/retention/data-
      handling setting that applied during each AI-assisted session.
- [ ] After review, upload the exact canonical v4 MP4 to YouTube or Vimeo and
      record the stable URL.

Do not guess or write a generic "no training" statement without verifying the
actual account setting.

### Report freeze checks

- [x] One canonical report source only.
- [x] Report says phase is inferred, not proven.
- [x] `p.Asn1002Lys` is described as a VUS with unmeasured function.
- [x] The child-specific 5-10% BUBR1 level and 1.3-2.6-fold rescue target are
      labelled scenario analysis, not patient measurements.
- [x] Azithromycin is described as an ex vivo lead screen, not a drug
      recommendation.
- [x] Arimoclomol is conditional on demonstrating missense instability.
- [x] Sirolimus and acetylcysteine are downstream benchmarks/comparators, not
      upstream cures.
- [x] Gentamicin is a laboratory control only.
- [x] Report recommends no change to current oncology treatment.
- [ ] Visually inspect every page of the exact v4 PDF.
- [ ] Confirm extracted v4 PDF text contains no replacement glyphs and all
      required sections are present.
- [x] `make check` and the privacy/single-source gates pass.
- [ ] Reconfirm every cited 2026 source and current medicine label on the actual
      submission date.

Canonical PDF:

```text
competition/artifacts/MarxistLeninist_track2_report.pdf
SHA-256 dc28529b02535edc7cfabdd6f6478ce3724d246a4d8786343b4079b2754444c8
Status built_unreviewed
```

### Pitch freeze checks

The historical MP4 remains superseded. The **new report-aligned video** is the
only canonical pitch artifact.

- [x] Narration regenerated from the revised script using Kokoro `bm_george`.
- [x] Five report-aligned slides generated from the same source of truth.
- [x] Burned captions generated.
- [ ] Inspect the exact v4 captions and representative frames.
- [x] Runtime 177.267 seconds, below the 180-second limit.
- [x] 1920x1080 H.264 video, AAC mono audio at 48 kHz.
- [ ] Measure integrated loudness and true peak on the exact v4 MP4.
- [x] Full audio/video decode completed without errors.
- [x] Contact sheet and representative frames generated.
- [ ] Inspect the complete v4 video and contact sheet.
- [x] No child-specific 5-10% level presented as measured.
- [x] No unsupported vincristine or oncology-treatment implication.
- [ ] Upload the exact reviewed file to YouTube or Vimeo.
- [ ] Watch the hosted copy from beginning to end after platform processing.

Canonical video:

```text
competition/artifacts/MarxistLeninist_track2_pitch.mp4
SHA-256 ccf6b4f8be2845ab28197316bb3ab9150b088e7b46c5d79e85c6aaf139d74db2
Status built_unreviewed
```

### Dedicated SG competition MCP

- [x] Competition-specific MCP implemented.
- [x] Twelve dedicated tools exposed, including strictly read-only
      `mva_report` and `mva_video`.
- [x] Deployed and verified on SG1.
- [x] Deployed and verified on SG2.
- [x] SG1/SG2 tool-surface parity verified.
- [x] Registered once as backend `mva-hackathon-2026` on each node.
- [x] SG1 is the single coordination writer; SG2 writes are fenced.
- [x] Confirmed that the MCP has no submission capability.

### Suggested notes for judges

> This is an allele-resolved preclinical rescue-screen proposal, not a cure or
> treatment recommendation. The report ranks azithromycin as an exact-context
> readthrough screen for p.Leu737Ter; retains arimoclomol only after proving that
> p.Asn1002Lys is an unstable, recoverable protein; and uses sirolimus and
> acetylcysteine only as downstream benchmarks. Every arm must show molecular
> target engagement, improve at least two orthogonal checkpoint/segregation
> outcomes near approved human exposure, and pass a rescue-versus-clone-safety
> gate. Phase is inferred, p.Asn1002Lys remains a VUS, and no change to current
> clinical care is proposed.

### Final authorization gate

Immediately before submission:

1. Re-open the live Track 2 form and confirm the quota and fields.
2. Run `make check` on the exact commit to be referenced.
3. Verify the PDF and local MP4 hashes against `competition/CANONICAL.json`.
4. Confirm the hosted video URL is accessible without login and matches the
   reviewed local file in content.
5. Confirm the AI account-level data-handling disclosure is complete.
6. Obtain the participant's explicit instruction for canonical version
   `2026-08-30.4` to use one of the two remaining submission slots.
7. After submission, update the quota and archive the returned receipt without
   exposing gated data.
