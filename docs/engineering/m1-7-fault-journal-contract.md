# M1.7 — Fault journal data contract

## Purpose
Define a portable record representation for management faults that can later be persisted in MCU NVM. This milestone **does not implement persistent storage**.

## Fields
- `v`: schema version, currently 1.
- `seq`: unsigned 64-bit monotonically increasing sequence (wrap policy TBD).
- `ms`: unsigned 64-bit uptime in milliseconds (not wall clock).
- `reason`: allowlisted reason code.
- `state`: state when the fault was recorded.

Encoding: canonical ASCII JSON payload followed by `|` and eight hexadecimal CRC32 digits; 512-byte maximum. CRC32 detects accidental corruption but is **not cryptographic authentication**. The caller supplies raw slots; `latest_valid` ignores malformed/torn records and chooses the greatest sequence.

## Safety and persistence requirements still open
1. Choose an MCU and actual NVM medium; validate endurance and brownout behavior.
2. Implement append/commit protocol with at least two slots, atomicity or torn-write recovery, wear leveling and boot-time recovery.
3. Define boot epochs and sequence-wrap policy, plus an explicit way to distinguish old records from current boot.
4. Never authorize power-on solely because the journal is readable or because a checksum passes.
5. Integrate journal writes with state transitions and fault handling; test with power-fail injection.
6. Define data retention/privacy policy and bounded record count.

The current Python codec is a host-side reference, not MCU firmware or a hardware-backed log.
