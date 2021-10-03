from datetime import datetime

import graphene
import grpc

import calendar_pb2
import calendar_pb2_grpc


class Participant(graphene.ObjectType):
    id = graphene.String()


class Event(graphene.ObjectType):
    id = graphene.String()
    timestamp = graphene.Float()
    participants = graphene.List(Participant)


class CalendarQuery(graphene.ObjectType):
    hello = graphene.String(name=graphene.String())
    timestamp = graphene.Float()
    events = graphene.List(Event, user_id=graphene.String())

    def resolve_events(self, info, user_id):
        channel = grpc.insecure_channel('localhost:50051')
        stub = calendar_pb2_grpc.CalendarStub(channel)
        all_events = stub.GetEvents(calendar_pb2.User(id=user_id))
        return [{
            "id": e.id,
            "timestamp": e.timestamp,
            "participants": [{"id": p_id} for p_id in e.participant_ids]}
            for e in all_events]

    def resolve_hello(self, info, name):
        return "Hello " + name

    def resolve_timestamp(self, info):
        return datetime.now().timestamp()
