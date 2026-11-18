# Shipping

Use this playbook only with explicit authority for the particular merge or release. A request to implement, commit, or open a PR is not merge or deploy authority.

1. Read the current remote state. Confirm the repository, target, revision, and authorized action.
2. Confirm acceptance checks passed for the exact revision to ship. Re-run affected checks if the artifact changed.
3. Independently check required CI, review approvals, branch policy, conflict state, and release-specific requirements.
4. Resolve failing gates within scope. Do not bypass policy, dismiss required review, or weaken checks to ship.
5. Confirm that the authorized action remains safe. Pause for any new irreversible action outside that authority.
6. Perform the authorized merge or release once.
7. Read back remote state. Confirm the target contains the intended revision and the operation completed.
8. Report the confirmed state and evidence.

A successful command exit is not enough to prove a merge. An accepted release request is not proof of a completed deployment.

If a gate cannot be met, stop and report the blocked gate and remaining work. If the action times out, inspect remote state before retrying. Never infer completion from intent.
