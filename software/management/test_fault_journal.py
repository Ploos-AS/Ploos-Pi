import unittest
from fault_journal import FaultRecord, encode, decode, latest_valid

class FaultJournalTests(unittest.TestCase):
    def test_round_trip(self):
        r = FaultRecord(42, 5000, "rail_fault", "RUNNING")
        self.assertEqual(r, decode(encode(r)))

    def test_corruption_detected(self):
        wire = bytearray(encode(FaultRecord(1, 10, "watchdog_timeout", "RUNNING")))
        wire[5] ^= 1
        with self.assertRaises(ValueError):
            decode(bytes(wire))

    def test_torn_write_falls_back(self):
        good = encode(FaultRecord(2, 20, "pgood_timeout", "POWERING_ON"))
        torn = encode(FaultRecord(3, 30, "rail_fault", "RUNNING"))[:-5]
        self.assertEqual(2, latest_valid([good, torn]).sequence)

    def test_latest_sequence(self):
        a = encode(FaultRecord(1, 1, "rail_fault", "RUNNING"))
        b = encode(FaultRecord(2, 2, "watchdog_timeout", "RUNNING"))
        self.assertEqual(2, latest_valid([a, b]).sequence)

    def test_empty_slots(self):
        self.assertIsNone(latest_valid([b"", b"garbage"]))

    def test_invalid_reason(self):
        with self.assertRaises(ValueError):
            FaultRecord(1, 2, "unknown", "RUNNING")

    def test_negative_counter(self):
        with self.assertRaises(ValueError):
            FaultRecord(-1, 2, "rail_fault", "RUNNING")

    def test_schema_rejects_oversized(self):
        with self.assertRaises(ValueError):
            decode(b"x" * 513)
