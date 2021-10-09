import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

import app.src.main.service.task_service as task_service
import app.src.main.service.event_service as event_service
from app.src.main.graphene_query.calendar import CalendarQuery
from app.src.main.model.task_model import TaskModel, TaskCreateModel
from app.src.main.model.event_model import EventCreateModel
import app.src.main.database as database

database.init()
app = FastAPI()

app.add_route("/calendar", GraphQLApp(schema=graphene.Schema(query=CalendarQuery)))


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/task/{task_id}", response_model=TaskModel)
async def get_task(task_id: str):
    return task_service.get_task(task_id)


@app.post("/task", response_model=TaskModel)
async def create_task(task: TaskCreateModel):
    return task_service.create_task(task)


@app.post("/event")
async def create_event(event: EventCreateModel):
    event_service.create_event(event)
