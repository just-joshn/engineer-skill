# Review

Assess the requested scope. Do not modify it unless the user asks for fixes.

1. Establish intent, acceptance checks, base revision, and the exact artifact under review.
2. Inspect the whole relevant change and its surrounding contracts.
3. Prioritize correctness, safety, regressions, missing behavior checks, and unnecessary complexity.
4. Probe suspected defects with a test, reproduction, or concrete source trace.
5. For each finding, give its location, affected behavior, evidence, and impact. Label an untested concern as unverified.
6. Separate new defects from pre-existing issues. Drop preferences that do not affect the goal or an established project rule.
7. Report findings in impact order, checks performed, and coverage limits.

Delegate independent risk questions when useful. Inspect and verify each returned finding before adopting it. Agreement between reviewers does not establish correctness.

"No supported findings" means none were found within the checks performed. It does not prove the artifact is defect-free or authorize a merge.
