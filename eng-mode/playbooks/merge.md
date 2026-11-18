# Merge

State: Deploy. Nodes: `Meet independent shipping gates`, `Merge and confirm actual state`.

## Meet independent shipping gates

1. Read the current remote state. Confirm the repository, target, revision, and authorized action.
2. Confirm the acceptance checks passed on the exact revision to ship. If the artifact changed after verification, take `Gate cannot be met`.
3. Check required CI, review approvals, branch policy, conflict state, and release-specific requirements. Apply gate checks.
4. Wait on a pending gate with a deadline. Apply monitoring.
5. If any gate fails, cannot be checked, or misses its deadline, take `Gate cannot be met`. Do not bypass policy, dismiss required review, or weaken checks.
6. Confirm the authorized action is still safe. A new irreversible action outside that authority is a gate that cannot be met.
7. When every gate passes, go to `Merge and confirm actual state`.

## Merge and confirm actual state

1. Perform the authorized merge or release once. Apply release management.
2. If the action times out, inspect remote state before any retry.
3. Read back the remote state. Confirm the target contains the intended revision and the operation completed. Apply rollout confirmation.
4. Report the confirmed state and evidence.
