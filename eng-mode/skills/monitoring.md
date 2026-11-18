# Monitoring

State: Maintain.

- Watch a pending gate, check, or dependency with a deadline. When the deadline passes, the gate cannot be met.
- Read status from its source of truth each time. Do not report a cached state as current.
- Do not loop on a failure without new evidence.
