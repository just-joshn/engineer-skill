# Gate checks

State: Deploy.

- Shipping gates are independent of acceptance checks: required CI, review approvals, branch policy, conflict state, and release-specific requirements.
- Read each gate's current state from its source of truth. Do not rely on an earlier reading.
- Never bypass policy, dismiss required review, or weaken a check to pass a gate.
