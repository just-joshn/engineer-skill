# Refactoring

Preserve observable behavior unless the user explicitly authorizes a behavior change.

1. State the behavior and compatibility guarantees that must remain unchanged.
2. Capture baseline behavior with existing tests or focused characterization checks.
3. Define the target structure and identify every affected caller.
4. Choose verifiable migration units. Delegate only across independent boundaries.
5. Migrate callers and remove replaced internal APIs within each coherent unit.
6. Compare behavior after each unit and on the integrated artifact.
7. Inspect for leftover compatibility paths, unused state, and unrelated changes.
8. Apply the entry skill's evidence decision.

Do not treat a type check as proof of behavior preservation. If a behavior change becomes necessary, stop that portion and establish authorization and new acceptance checks.
