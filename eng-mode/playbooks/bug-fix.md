# Bug fix

Keep reproduction, diagnosis, and the final correction under one owner. Delegate bounded source tracing or independent regression checks when useful.

1. Define expected and observed behavior with concrete inputs.
2. Reproduce the failure on the unchanged artifact. Record the environment and output.
3. Trace the first point where behavior diverges from the requirement.
4. Add a regression check that fails for the observed bug. Explain any reproduction limit.
5. Fix the cause with the smallest coherent change.
6. Run the regression check, nearby behavior checks, and applicable project checks.
7. Inspect the final diff. Apply the entry skill's evidence decision.

If the baseline cannot be reproduced, investigate before claiming a fix. Do not claim that a passing test proves a bug was fixed unless the test exposed that bug before the correction.
