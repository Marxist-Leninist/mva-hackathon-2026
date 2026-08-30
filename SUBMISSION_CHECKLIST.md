# MVA Hackathon submission checklist

Nothing in this file authorizes a submission. Re-check the live form and obtain
the participant's explicit confirmation immediately before using a submission
slot.

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
- Report file: `reports/MarxistLeninist_track2_report.md`
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
- [ ] Upload the final 179-second pitch video to YouTube or Vimeo and record the
      stable URL.

Do not guess or write a generic "no training" statement without verifying the
actual account setting.

### Report freeze checks

- [ ] Confirm the report says phase is inferred, not proven.
- [ ] Confirm `p.Asn1002Lys` is described as a VUS with unmeasured function.
- [ ] Confirm the child-specific 5-10% BUBR1 level and 1.3-2.6-fold rescue target
      are labelled scenario analysis, not patient measurements.
- [ ] Confirm azithromycin is described as an ex vivo lead screen, not a drug
      recommendation.
- [ ] Confirm arimoclomol is conditional on demonstrating missense instability.
- [ ] Confirm sirolimus and acetylcysteine are downstream benchmarks/comparators,
      not upstream cures.
- [ ] Confirm gentamicin is a laboratory control only.
- [ ] Confirm the report recommends no change to current oncology treatment.
- [ ] Run `make check` and `make privacy` on the exact candidate commit.
- [ ] Confirm every cited 2026 source and current medicine label remains accurate
      on the submission date.

### Video freeze checks

- [x] Runtime below three minutes: approximately 179 seconds.
- [x] 1920x1080 H.264 video and AAC audio.
- [x] Burned-in captions generated from the corrected narration source.
- [x] Corrected gnomAD wording: one allele in 1,461,878 exome alleles, not
      "absent from gnomAD".
- [x] Corrected phase wording: candidate biallelic, not proven compound
      heterozygosity.
- [x] Corrected mechanism wording: predicted hypomorph/instability, not an
      established property of `p.Asn1002Lys`.
- [ ] Upload and watch the hosted copy from beginning to end after platform
      processing.

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
2. Compare the default-branch report, methods material, and video against the
   reviewed versions.
3. Confirm the hosted video URL is accessible without login.
4. Confirm the AI disclosure and Synapse citation are complete.
5. Obtain the participant's explicit instruction to use a submission slot.
6. Save the submission timestamp and a screenshot or receipt of the accepted
   form without exposing gated data.
