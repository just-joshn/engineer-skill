# Small change

Use this path for a bounded, low-risk change with a direct check. Do not create workers or a planning document by default.

1. Inspect the relevant artifact and the surrounding convention.
2. State the goal, constraints, endpoint, and a concrete acceptance check in working context.
3. Make the smallest complete change. Avoid unrelated cleanup.
4. Run the check on the changed artifact. Inspect the final diff.
5. Use the evidence decision in the entry skill. Report the result and the endpoint reached.

If the check exposes unknown behavior, use investigation or bug fix. If the change crosses boundaries or needs several dependent steps, use implementation.
