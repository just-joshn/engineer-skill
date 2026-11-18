# Investigation

State: Design. Node: `Choose playbook; investigate and design`.

Produce an explanation, not an unrequested implementation.

1. State the question and the observation that would settle it.
2. For incorrect behavior, define expected and observed behavior with concrete inputs. Reproduce the failure on the unchanged artifact. Record the environment and output.
3. Inspect the actual system, source, records, or artifact. Separate known facts from assumptions.
4. Form a small set of competing explanations. Choose the cheapest experiment that distinguishes them.
5. Run the experiment and preserve the observed evidence. Trace a failure to the first point where behavior diverges from the requirement.
6. Update the explanation. Repeat only when another experiment can reduce a material uncertainty.
7. Record the supported explanation, rejected explanations, limits, and the smallest justified next step.

Isolate any prototype and avoid production writes. A prototype proves only the behavior and environment it exercised. If the baseline cannot be reproduced, say so before any fix is claimed.
