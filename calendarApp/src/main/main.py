import sys
import uuid
from concurrent import futures
from datetime import datetime

import grpc
import calendar_pb2 as pb
import calendar_pb2_grpc as pb_grpc

events = [
    pb.Event(id="1", timestamp=1633250902, participant_ids=["123", "200"]),
    pb.Event(id="2", timestamp=1633250905, participant_ids=["123", "1"]),
    pb.Event(id="3", timestamp=1633250910, participant_ids=["123", "3", "1", "5"]),
    pb.Event(id="4", timestamp=1633251100, participant_ids=["500"])
]


def get_events(user):
    for event in events:
        if user.id in event.participant_ids:
            yield event


class CalendarService(pb_grpc.CalendarServicer):
    def GetEvents(self, user, context):
        yield from get_events(user)

    def CreateEvent(self, new_event, context):
        event = pb.Event(id=str(uuid.uuid4()),
                         timestamp=datetime.now().timestamp(),
                         participant_ids=new_event.participant_ids)
        events.append(event)
        return event


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_CalendarServicer_to_server(
        CalendarService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
