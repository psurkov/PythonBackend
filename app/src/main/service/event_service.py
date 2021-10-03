import grpc

import calendar_pb2
import calendar_pb2_grpc
from app.src.main.model.event_model import EventCreateModel


def create_event(event: EventCreateModel):
    channel = grpc.insecure_channel('localhost:50051')
    stub = calendar_pb2_grpc.CalendarStub(channel)
    new_event = calendar_pb2.NewEvent()
    new_event.participant_ids.extend(event.participants)
    stub.CreateEvent(new_event)
