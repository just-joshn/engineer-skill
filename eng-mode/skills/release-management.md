# Release management

State: Deploy.

- Perform each merge, release, or deployment exactly once, against the exact revision that passed the gates.
- If an action times out or its result is unclear, inspect the remote state before any retry. Never infer completion from intent.
- Pause before any irreversible action outside the authorized endpoint.
