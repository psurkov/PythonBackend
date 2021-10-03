import unittest

import calendarApp.src.main.main as main
import calendar_pb2


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.events_copy = main.events.copy()

    def tearDown(self) -> None:
        main.events = self.events_copy

    def test_get_events_many_events(self):
        self.assertEqual(
            [
                calendar_pb2.Event(id="1", timestamp=1633250902, participant_ids=["123", "200"]),
                calendar_pb2.Event(id="2", timestamp=1633250905, participant_ids=["123", "1"]),
                calendar_pb2.Event(id="3", timestamp=1633250910, participant_ids=["123", "3", "1", "5"])
            ],
            list(main.get_events(calendar_pb2.User(id="123")))
        )

    def test_get_events_one_event(self):
        self.assertEqual(
            [
                calendar_pb2.Event(id="4", timestamp=1633251100, participant_ids=["500"])
            ],
            list(main.get_events(calendar_pb2.User(id="500")))
        )

    def test_get_events_no_events(self):
        self.assertEqual(
            [],
            list(main.get_events(calendar_pb2.User(id="-1")))
        )

    def test_add_participants_simple(self):
        main.add_participants(
            calendar_pb2.Event(id="1", timestamp=1633250902, participant_ids=["123", "200"]),
            ["500", "600"]
        )
        l = list(filter(lambda e: e.id == "1", main.events))
        self.assertEqual(1, len(l))
        self.assertEqual(["123", "200", "500", "600"], l[0].participant_ids)

    def test_add_participants_banned(self):
        main.add_participants(
            calendar_pb2.Event(id="1", timestamp=1633250902, participant_ids=["123", "200"]),
            ["1001", "1002"]
        )
        l = list(filter(lambda e: e.id == "1", main.events))
        self.assertEqual(1, len(l))
        self.assertEqual(["123", "200"], l[0].participant_ids)

    def test_add_participants_existing(self):
        main.add_participants(
            calendar_pb2.Event(id="1", timestamp=1633250902, participant_ids=["123", "200"]),
            ["123", "200"]
        )
        l = list(filter(lambda e: e.id == "1", main.events))
        self.assertEqual(1, len(l))
        self.assertEqual(["123", "200"], l[0].participant_ids)


if __name__ == '__main__':
    unittest.main()
