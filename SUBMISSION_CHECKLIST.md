# MVA Hackathon submission checklist

Nothing in this file authorizes a submission. Re-check the live form and obtain
the participant's explicit confirmation immediately before using a submission
slot.

## Canonical source of truth

- Manifest: `competition/CANONICAL.json`
- Canonical version: `2026-08-30.3`
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

### Current live-form rule

The Track 2 form permits up to **three submissions**. The independent panel will
review only the **latest** entry. Earlier repository text referring to a one-shot
submission rule is obsolete.

### Required participant-controlled fields still open

- [ ] Insert the exact Synapse dataset citation supplied with the controlled
      Hackathon data-access record.
- [ ] Confirm the exact provider plan/tier used for each AI assistant.
- [ ] Confirm and record the relevant account-level training/retention/data-
      handling setting that applied during each AI-assisted session.
- [ ] Upload the reviewed MP4 to YouTube or Vimeo and record the stable URL.

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
- [x] Canonical PDF rendered and visually inspected across all 16 pages.
- [x] Extracted PDF text contains no replacement glyphs and all required
      sections are present.
- [x] `make check` and the privacy/single-source gates pass.
- [ ] Reconfirm every cited 2026 source and current medicine label on the actual
      submission date.

Canonical PDF:

```text
competition/artifacts/MarxistLeninist_track2_report.pdf
SHA-256 8ed015d441563ddcce92de07432e7767afcc5374c42998c5980b06b47b25e1ef
```

### Pitch freeze checks

The historical MP4 remains superseded. The **new report-aligned video** is the
only canonical pitch artifact.

- [x] Narration regenerated from the revised script using Kokoro `bm_george`.
- [x] Five report-aligned slides generated from the same source of truth.
- [x] Burned captions generated and inspected.
- [x] Runtime 177.267 seconds, below the 180-second limit.
- [x] 1920x1080 H.264 video, AAC mono audio at 48 kHz.
- [x] Integrated loudness -16.71 LUFS; true peak -1.41 dBTP.
- [x] Full audio/video decode completed without errors.
- [x] Contact sheet and representative frames from every slide inspected.
- [x] No child-specific 5-10% level presented as measured.
- [x] No unsupported vincristine or oncology-treatment implication.
- [ ] Upload the exact reviewed file to YouTube or Vimeo.
- [ ] Watch the hosted copy from beginning to end after platform processing.

Canonical video:

```text
competition/artifacts/MarxistLeninist_track2_pitch.mp4
SHA-256 7e12b02a90604d4c765a500a496d39405a95c17e7b15d2122f547ae7f5fd0ac8
```

### Dedicated SG coordination MCP

- [x] Competition-specific MCP implemented.
- [x] Unit tests passed.
- [x] Live Streamable HTTP initialization, tool listing and health call passed.
- [x] Infrastructure code merged at
      `28b6c54bdc76acb3b8eb8529364a8bfa9c4e5b00`.
- [ ] Deploy and verify on SG1.
- [ ] Deploy and verify on SG2.
- [ ] Register exactly once as `SG MVA Hackathon 2026` in each applicable client.

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
5. Confirm the AI disclosure and Synapse citation are complete.
6. Obtain the participant's explicit instruction for canonical version
   `2026-08-30.3` to use a submission slot.
7. Save the submission timestamp and a screenshot or receipt of the accepted
   form without exposing gated data.
