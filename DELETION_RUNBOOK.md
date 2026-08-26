# Restricted-data deletion runbook

Deadline: **2026-11-23 23:59 UTC**, unless organizers publish a stricter date.

1. Freeze analysis and export only allowlisted public artifacts.
2. Enumerate every authorized private location: workstation, cloud volume,
   notebook, object store, cache, backup, snapshot, and collaborator container.
3. Verify that each target is a narrow, explicit analysis path. Never operate
   on a home directory, filesystem root, repository root, unresolved variable,
   wildcard, or symlink.
4. Delete the gated source data and every derived individual-level artifact
   using the storage provider's supported deletion process.
5. Remove notebook checkpoints, package/download caches, workflow work trees,
   trash/recycle bins, snapshots, and object versions where policy permits.
6. Re-run searches for known filenames and gated extensions. Confirm that public
   repositories contain only allowlisted derived outputs.
7. Record date, operator, systems checked, residual provider-retention limits,
   and verification evidence in a deletion receipt kept outside this public repo.
8. Email `RarediseaserealkidMVAhackathon2026@synapse.org` to confirm deletion,
   as required by the official rules.

Deletion must be performed by the authorized data holder. This repository does
not ship an automatic recursive deletion command because the correct targets
are environment-specific and a broad mistake would be irrecoverable.

