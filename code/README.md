# Code

Sanitised analysis code (no patient data).

- `score_local.py` — local replica of the official Track 1 scorer (`evaluation.py`) for pre-submission validation.
- `extract_candidates.py` — bcftools extraction of BUB1B-region and SAC-gene candidate variants with GT/AD/DP/GQ summary (run against the gated VCF; paths parameterised).
