# Management policy reference implementation — M1.2

Python standard library only. This is an executable **policy simulation**, not firmware, electrical verification or production-grade power-control software.

Run from repository root:

```sh
python3 -m unittest discover -s software/management -p 'test_*.py' -v
```

The tests read `docs/engineering/m1-1-management-test-vectors.csv` and compare state, main-power logical output and outcome. No GPIO, time source, MCU watchdog, persistent event log or network authentication is implemented.

**Limitations:** `within_retry_limit` is supplied externally; actual wall-clock rate limiting, MCU reset handling, atomic event logging, secure commands and power-fault behavior require separate implementation and tests. The model does not control physical rails. No hardware should be wired from this simulation alone.
