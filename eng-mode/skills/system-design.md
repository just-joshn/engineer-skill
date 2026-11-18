# System design

State: Design.

- Model the domain before writing logic. Name the state, data shapes, invariants, and boundaries.
- Put a repeated decision in one place. Prefer a representation that prevents invalid states over conditionals that repair them later.
- Parse and validate external data at the boundary. Keep business rules separate from adapters. Trust established internal contracts.
