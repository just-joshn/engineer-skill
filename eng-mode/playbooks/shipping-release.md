# Shipping/release

State: Deploy. Nodes: `Authorized endpoint`, `Deliver artifact and evidence`.

## Authorized endpoint

1. Read the authorized endpoint from the task record. Apply authorization.
2. Take `Merge` only when the user explicitly authorized this merge or release of this artifact. A request to implement, commit, or open a PR is not merge or release authority.
3. Otherwise take `Handoff`.

## Deliver artifact and evidence

1. Deliver the artifact only as far as the endpoint allows: local changes, a commit, a pushed branch, or a PR.
2. Read back any remote action before you report it.
3. Hand off the artifact with its evidence table and the report.

A release or deployment takes `Merge` and follows the merge playbook. Apply release management.
