# M2.3 — Cross-language parity gate

Date: 2026-10-15.

Added a Python unittest that compiles the portable C11 core as a shared library, calls it through ctypes, and compares state, logical power and outcome code against the Python reference and all 12 canonical CSV scenarios. A GitHub Actions workflow now invokes both C tests and the entire Python unittest suite on relevant changes.

**Evidence:** files committed. No successful CI execution has been verified. Local clone could not be completed because GitHub DNS resolution failed in the execution environment. This is a parity gate for the 12 CSV vectors only, not exhaustive equivalence or hardware validation.

Next: inspect workflow results, repair discrepancies, add state/event property tests and validate retry-window timing and journal failure handling.
