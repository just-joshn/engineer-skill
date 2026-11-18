# Implementation

State: Build. Node: `Implement and clean`.

1. Follow the surrounding conventions, callers, and checks. Read [coding](../skills/coding.md).
2. For a bug, keep a regression check that already failed on the unchanged artifact. If that check is not in the suite yet, add it without changing the recorded failure. Change the code so the check passes. Do not weaken the check.
3. Build one unit at a time. Check that unit before you build on it.
4. For a structural change that must keep its behavior, capture the baseline before you restructure. Read [refactoring](../skills/refactoring.md).
5. Delegate an independent unit only when the host has workers and the boundary is stable. Read [delegation](../skills/delegation.md). You integrate the worker's output.
6. For an answer-only task, write the answer and its evidence. Do not edit source. For a review-only task, do not edit anything.
