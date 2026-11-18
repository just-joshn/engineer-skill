# Shipping/release

State: Deploy. Nodes: `Authorized endpoint`, `Deliver artifact and evidence`.

## Authorized endpoint

1. Read the authorized endpoint from the task record or the prompt. Read [authorization](../skills/authorization.md).
2. Treat merge or release authority as present only when the user explicitly authorized this merge or release of this artifact. A request to implement, commit, or open a pull request is not that authority.

## Deliver artifact and evidence

1. Deliver the artifact only as far as the endpoint allows. That limit is local changes, a commit, a pushed branch, or a pull request.
2. Read back any remote action before you report it.
3. Hand off the artifact with the evidence table.
