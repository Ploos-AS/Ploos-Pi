# Management MCU portable C core — M2.0 initial port

This is an **experimental**, dependency-free C11 state machine with no MCU binding, hardware timing, GPIO, persistence, authentication, watchdog driver or reset safety implementation.

Run `make -C firmware/management test` with a C11 compiler. This smoke test covers a subset of the Python state model, not parity with all CSV vectors.

**Safety:** Do not connect the output directly to physical rails. Timing, brownout handling, boot defaults, real power sequencing and fail-safe electrical circuitry must be designed and verified separately. Python simulation remains the specification reference pending cross-language equivalence tests.
