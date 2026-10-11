"""M1.7: portable, bounded fault-record codec; storage supplied by caller.

No file I/O, flash driver, durability or wear-leveling is provided.
"""
from dataclasses import dataclass
import json
import zlib

MAX_RECORD_BYTES = 512
ALLOWED_REASONS = frozenset({"rail_fault", "pgood_timeout", "watchdog_timeout", "rate_limited", "shutdown_timeout"})

@dataclass(frozen=True)
class FaultRecord:
    sequence: int
    uptime_ms: int
    reason: str
    state: str

    def __post_init__(self):
        if not 0 <= self.sequence < 2**64 or not 0 <= self.uptime_ms < 2**64:
            raise ValueError("sequence and uptime must be unsigned 64-bit integers")
        if self.reason not in ALLOWED_REASONS:
            raise ValueError("unsupported fault reason")
        if self.state not in {"OFF", "POWERING_ON", "RUNNING", "POWERING_OFF", "CYCLING", "FAULT_LOCKOUT", "RECOVERY"}:
            raise ValueError("unsupported state")

def encode(record: FaultRecord) -> bytes:
    payload = json.dumps({"v": 1, "seq": record.sequence, "ms": record.uptime_ms,
                          "reason": record.reason, "state": record.state},
                         sort_keys=True, separators=(",", ":")).encode("ascii")
    checksum = zlib.crc32(payload) & 0xffffffff
    wire = payload + b"|" + format(checksum, "08x").encode("ascii")
    if len(wire) > MAX_RECORD_BYTES:
        raise ValueError("record too large")
    return wire

def decode(wire: bytes) -> FaultRecord:
    if len(wire) > MAX_RECORD_BYTES:
        raise ValueError("record too large")
    try:
        payload, checksum = wire.rsplit(b"|", 1)
        if len(checksum) != 8 or (zlib.crc32(payload) & 0xffffffff) != int(checksum, 16):
            raise ValueError("checksum mismatch")
        obj = json.loads(payload.decode("ascii"))
        if not isinstance(obj, dict) or set(obj) != {"v", "seq", "ms", "reason", "state"} or type(obj["v"]) is not int or obj["v"] != 1:
            raise ValueError("invalid schema")
        if type(obj["seq"]) is not int or type(obj["ms"]) is not int:
            raise ValueError("invalid integer fields")
        return FaultRecord(obj["seq"], obj["ms"], obj["reason"], obj["state"])
    except (UnicodeError, json.JSONDecodeError, TypeError, KeyError, OverflowError) as exc:
        raise ValueError("invalid fault record") from exc

def latest_valid(slots: list[bytes]) -> FaultRecord | None:
    """Pick highest sequence among intact slots. Caller handles wrap/reset policy."""
    records = []
    for slot in slots:
        try:
            records.append(decode(slot))
        except ValueError:
            continue
    return max(records, key=lambda record: record.sequence, default=None)
