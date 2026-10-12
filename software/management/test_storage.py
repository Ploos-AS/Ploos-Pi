import unittest
from storage import MemoryStorage
from logged import LoggedController
from fault_journal import decode
from reference import State

class StorageTests(unittest.TestCase):
    def test_shared_memory_storage_across_controller_instances(self):
        storage = MemoryStorage()
        c = LoggedController(storage=storage)
        c.command("power_on", authorized=True)
        c.advance(1000)
        self.assertEqual("pgood_timeout", decode(storage.read_slots()[0]).reason)
        restored = LoggedController(storage=storage)
        self.assertEqual(2, restored.next_sequence)

    def test_write_failure_does_not_block_lockout(self):
        storage = MemoryStorage(fail_next_append=True)
        c = LoggedController(storage=storage)
        c.command("power_on", authorized=True)
        c.advance(1000)
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
        self.assertFalse(c.core.main_power)
        self.assertEqual([], storage.read_slots())
        self.assertEqual(1, c.journal_write_failures)

    def test_write_failure_does_not_block_pgood_shutdown(self):
        storage = MemoryStorage(fail_next_append=True)
        c = LoggedController(storage=storage)
        c.command("power_on", authorized=True)
        c.command("pgood_high")
        c.advance(5000)
        c.command("pgood_low")
        self.assertEqual(State.FAULT_LOCKOUT, c.core.state)
        self.assertFalse(c.core.main_power)
        self.assertEqual(1, c.journal_write_failures)

    def test_legacy_slots_compatibility(self):
        c = LoggedController()
        c.command("power_on", authorized=True)
        c.advance(1000)
        self.assertEqual(1, len(c.slots))
