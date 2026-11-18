# Refactoring

State: Build.

- Preserve observable behavior unless the user authorized a change.
- Capture baseline behavior with existing tests or focused characterization checks before restructuring.
- Migrate every caller and delete the replaced internal API in the same unit.
- A type check does not prove behavior preservation. If a behavior change becomes necessary, stop that part. It reaches `Evidence` as `Blocked or inconclusive` until the user authorizes the change.
