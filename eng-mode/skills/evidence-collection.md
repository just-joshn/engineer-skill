# Evidence collection

State: Test.

For every acceptance check, record:

| Check | Method and environment | Expected result | Observed result | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| Observable requirement | Exact command or interaction, revision, relevant setup | Defined before the run | What actually happened | Output, test, screenshot, trace, or artifact path | Pass, fail, or not run |

- Use current evidence. A green build, a worker report, or an old screenshot cannot stand in for the behavior claimed.
- Keep facts separate from inferences and assumptions. Link bulky logs instead of pasting them.
- Never fabricate a command, output, review, screenshot, or pass.
