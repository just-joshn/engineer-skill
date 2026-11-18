# Performance

Do not optimize until a reproducible workload shows the problem.

1. Define the user-visible performance goal and the correctness requirements.
2. Record the workload, metric, environment, revision, and measurement method.
3. Capture a repeatable baseline. Account for cache state, warmup, contention, and run-to-run variance.
4. Profile or instrument the limiting operation.
5. Choose one supported hypothesis. Change one relevant factor.
6. Re-run the same workload under comparable conditions. Repeat enough to distinguish an effect from noise.
7. Check correctness and resource tradeoffs. Confirm the treatment still performs all required work.
8. Report the baseline, treatment, variation, method, and limits. Apply the entry skill's evidence decision.

Delegate independent hypotheses or profile analysis. Keep benchmark runs isolated. Do not compare measurements from workers with different environments as if they were controlled runs.

If comparable measurement is unavailable, report the change as unverified for performance. Do not invent an improvement percentage.
