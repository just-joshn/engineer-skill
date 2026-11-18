# Merge

State: Deploy. Nodes: `Meet independent shipping gates`, `Merge and confirm actual state`.

A release or a deployment uses these same steps.

## Meet independent shipping gates

1. Read the current remote state. Confirm the repository, the target, the revision, and the authorized action.
2. Confirm the acceptance checks passed on the exact revision to ship. If the artifact changed after verification, the gate cannot be met.
3. Check required CI, review approvals, branch policy, conflict state, and release-specific requirements. Read [gate checks](../skills/gate-checks.md).
4. Wait on a pending gate until a deadline you set. Read [monitoring](../skills/monitoring.md).
5. If any gate fails, cannot be checked, or misses its deadline, the gate cannot be met. Do not bypass policy, dismiss a required review, or weaken a check.
6. Confirm the authorized action is still safe. A new irreversible action outside that authority means the gate cannot be met.

## Merge and confirm actual state

1. Perform the authorized merge or release once. Read [release management](../skills/release-management.md).
2. If the action times out, inspect the remote state before any retry.
3. Read back the remote state. Confirm the target contains the intended revision and the operation completed. Read [rollout confirmation](../skills/rollout-confirmation.md).
