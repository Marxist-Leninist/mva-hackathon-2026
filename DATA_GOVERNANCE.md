# Data governance and public-release boundary

## Allowed in this repository

- The final Track 1 prediction row.
- Aggregate counts and minimal QC values needed to support that prediction.
- Public literature, database identifiers, code, schemas, and synthetic tests.
- Reports that avoid identifying details beyond the organizers' authorized
  public release.

## Never allowed

- Raw or processed sequence files, alignments, indexes, variant files, or
  phenotype source documents.
- Sample-wide variant tables, IGV screenshots, read names, absolute private
  paths, access tokens, or dataset credentials.
- Private caches, logs, temporary files, cloud snapshots, or workflow metadata
  that could reconstruct restricted records.
- Incidental findings that have not passed clinical confirmation and an
  appropriate return-of-results review.

The `.gitignore` is only a convenience. The enforceable release check is
`python scripts/privacy_gate.py .`, which fails on banned paths, extensions,
unexpected binary/large files, token patterns, and an invalid prediction CSV.
It is intentionally conservative.

## Incidental findings

The gene-agnostic scan produced additional candidate records. They are not
included in the public CSV or report because automated annotation is not a
clinical confirmation process, and public competition submission is not an
appropriate return-of-results pathway. A qualified clinical genetics team may
review them under the governing protocol.

## Retention and deletion

The organizers require deletion from local, cloud, notebook, repository, cache,
and backup locations within 30 days of hackathon close. Assuming the stated
close of 2026-10-24 23:59 UTC, the conservative deadline used here is
**2026-11-23 23:59 UTC**. See `DELETION_RUNBOOK.md`.

No claim of secure erasure is made for SSDs or cloud storage. Provider-level
deletion and snapshot-retention confirmation are required where applicable.

