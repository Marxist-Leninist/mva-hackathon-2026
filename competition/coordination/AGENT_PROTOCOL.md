# Agent protocol for the MVA Hackathon

## Mandatory startup sequence

Every agent working on this competition must:

1. Read `competition/CANONICAL.json`.
2. Read the latest shared workboard issue and this protocol.
3. Check the open pull request before starting overlapping work.
4. Declare a bounded task and expected output.
5. Work on the canonical path or a clearly named supporting artifact.
6. Return evidence, changed paths, tests and unresolved uncertainty.

## Shared coordination authority

GitHub PR #1 and issue #2 are the cross-node source of truth. MCP lane claims
and hand-offs are optional SG1 operational aids; they are not a shared database
and must not be used as proof that work is unclaimed. SG2 coordination writes
are fenced unless a human performs the documented primary failover.

## Canonical ownership

The canonical Track 2 report path is fixed by the manifest. No agent may create
an alternate report, promote an addendum into a report, or replace the report by
changing only a pitch or methods file. The PDF is generated from the Markdown;
it is not edited separately.

## Scientific reconciliation

When agents disagree:

- record the conflicting claims;
- cite primary evidence for each;
- distinguish measurement, published model evidence, inference and scenario;
- patch one reconciled conclusion into the canonical report; and
- retain rejected reasoning in the PR discussion, not as a second report.

A confident sentence without primary support does not win because it arrived
last. That would be an impressively bureaucratic way to do science.

## Artifact states

Each artifact is one of:

- `canonical` - the single current source or rendered deliverable;
- `supporting` - evidence or methods that cannot be submitted as the report;
- `historical` - superseded but retained for provenance;
- `building` - incomplete output that cannot be submitted;
- `blocked` - waiting on a named participant-controlled input.

## Required hand-off

Every completed task must state:

- what changed;
- why it changed;
- exact file paths and commit/PR;
- tests or inspection performed;
- evidence grade and remaining uncertainty;
- whether the canonical manifest needs a version/hash update; and
- whether another agent is now unblocked.

## Safety and submission

No agent may recommend administration, invent a dose, alter oncology care, claim
clinical efficacy, expose gated patient data, upload to the Hackathon form, or
consume a submission slot without explicit participant authorization.
