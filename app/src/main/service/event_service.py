import json

import grpc

import calendar_pb2
import calendar_pb2_grpc
from app.src.main.model.event_model import EventCreateModel
import pika

def create_event(event: EventCreateModel):
    channel = grpc.insecure_channel('localhost:50051')
    stub = calendar_pb2_grpc.CalendarStub(channel)
    new_event = calendar_pb2.NewEvent()
    new_event.participant_ids.extend(event.participants)
    stub.CreateEvent(new_event)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    pika_channel = connection.channel()
    pika_channel.queue_declare(queue='event')
    pika_channel.basic_publish(exchange='', routing_key='event', body=json.dumps(event.participants).encode())
