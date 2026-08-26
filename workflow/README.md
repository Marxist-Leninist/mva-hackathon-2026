# Private analysis workflow contract

The restricted workflow is intentionally not runnable from this public tree
without an explicit private configuration and adequate authorized storage.

1. Validate the GRCh38 VCF header, sample count, contigs, compression, and index.
2. Normalize and decompose against a checksum-pinned GRCh38 FASTA.
3. Annotate with pinned VEP/MANE, ClinVar, gnomAD, LOFTEE, SpliceAI, and
   missense predictors.
4. Run a gene-agnostic phenotype/inheritance lane and an MVA/SAC-focused lane.
5. Construct gene-level recessive pairs, including SNV/indel plus CNV/SV.
6. Inspect shortlisted calls in an authorized private alignment workspace and
   independently re-call when feasible.
7. Export only the exact allowlisted Track 1 fields.
8. Run the public submission validator and privacy gate before commit.

Recommended high-confidence raw-read rerun: a checksum-pinned GRCh38 germline
workflow such as nf-core/sarek with DeepVariant plus separate CNV/SV/MEI lanes.
It requires substantially more storage than available in the current workspace.

Phase remains `unknown/inferred` unless parents or a molecule spanning both
sites establish trans. Population phasing is not diagnostic confirmation.

