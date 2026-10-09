# M1 — Nano power-domain and management interface contract

Date: 2026-10-09. **Requirements draft; not a verified electrical design.**

## Functional contract
- An external management MCU must retain control of main SoC power and reset when the SoC is crashed, powered down, or stuck during boot.
- Separate always-on management power from switchable application power. Do not assume the SoC-integrated MCU survives removal of application rails.
- Provide a hardware-defined safe default after input power is applied; an unprogrammed MCU must not cause uncontrolled boot loops.
- The management controller shall report reset reason, power-good state, watchdog expirations and measured supply conditions when hardware permits.
- Recovery must remain possible without a working Linux installation, eMMC filesystem or network stack.
- Main-power cycling must not remove power from the management MCU unless the external supply itself fails.

## Proposed logical signals (names provisional)
| Signal | Direction from management MCU | Meaning | Electrical specification |
|---|---|---|---|
| MAIN_PWR_EN | output | Enable application power sequence | TBD by selected PMIC |
| SOC_RESET_N | output/open-drain candidate | Assert application reset | TBD by SoC reset guidance |
| MAIN_PGOOD | input | Aggregated application power-good | TBD by PMIC |
| SOC_WDOG | input | Heartbeat or watchdog status | TBD by chosen implementation |
| RECOVERY_REQ | output | Request documented boot recovery mode | TBD by boot straps |
| HOST_UART_TX/RX | bidirectional | Out-of-band management/control | Voltage levels TBD |
| INPUT_PWR_OK | input | External input supply healthy | Comparator thresholds TBD |
| FAULT_N | input | Power/thermal fault indication | TBD |

These names are **logical interfaces**, not KiCad nets ready for wiring. Polarity, drive type, isolation, sequencing, pull-ups, voltage domains and default states require component-specific approval.

## Failure-injection acceptance tests
1. Linux hangs: management MCU remains reachable and can force a controlled power cycle.
2. eMMC unreadable: recovery path is still usable.
3. Main rail short/fault: controller does not repeatedly re-enable power without a defined policy.
4. Unexpected input power loss: no undefined back-powering through UART/GPIO.
5. MCU firmware corrupt: documented hardware recovery/programming path exists.
6. Host boots repeatedly: rate-limit and event logging prevent endless reboot storms.
7. Main SoC fully off: measure management-only idle power.

## Hard safety blockers
Do not assign GPIOs or choose MOSFETs, supervisors, fuses or PMIC variants until supply voltage, maximum currents, sequencing and absolute maximum ratings are established. Verify watchdog and power-cycle behavior with a bench prototype before integrating the SoC.
