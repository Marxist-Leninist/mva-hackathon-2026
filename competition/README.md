# MVA Hackathon 2026 - dedicated competition workspace

This directory is the single entry point for every human or agent working on the
submission. Read [`CANONICAL.json`](CANONICAL.json) before touching any report,
video, methods file, or submission form.

## One report, not three

There is exactly one canonical Track 2 report:

`reports/MarxistLeninist_track2_report.md`

The PDF is a rendered artifact of that Markdown source, not an independently
editable report. The addendum and older pitch scripts are supporting or
historical material. They must not be uploaded as competing reports and must not
be silently treated as a newer source of truth.

## Dedicated areas

- `competition/CANONICAL.json` - machine-readable source-of-truth manifest.
- `competition/artifacts/` - final uploadable PDF and MP4 only.
- `competition/coordination/` - agent rules, workboard and hand-offs.
- `reports/` - canonical report source plus clearly labelled supporting history.
- `methods/` - methods disclosure and reproducibility material.
- `pipeline/competition_video/` - report-aligned video build.

## Change rule

Agents do not create `track2_report_v2.md`, `final_final_report.md`, personal
copies, or alternate conclusions. Proposed scientific changes must patch the
canonical Markdown on a branch and explain the evidence in the shared pull
request or workboard. Humanity has already invented enough filenames ending in
`FINAL-v7`; the robots do not need to preserve the tradition.

## Submission rule

The release gate must pass before upload:

1. Canonical manifest validates.
2. Public-release and privacy checks pass.
3. PDF hash matches the manifest.
4. Video was built from the canonical pitch source and inspected.
5. AI disclosure and Synapse citation are complete.
6. Hosted video URL works without login.
7. The participant explicitly authorizes use of a Track 2 submission slot.
