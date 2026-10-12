"""M1.9 storage abstraction. In-memory simulation only, no durability guarantee."""
from dataclasses import dataclass, field
from typing import Protocol

class JournalStorage(Protocol):
    def read_slots(self) -> list[bytes]: ...
    def append(self, record: bytes) -> None: ...

@dataclass
class MemoryStorage:
    slots: list[bytes] = field(default_factory=list)
    fail_next_append: bool = False

    def read_slots(self) -> list[bytes]:
        return list(self.slots)

    def append(self, record: bytes) -> None:
        if self.fail_next_append:
            self.fail_next_append = False
            raise OSError("simulated journal write failure")
        self.slots.append(bytes(record))
