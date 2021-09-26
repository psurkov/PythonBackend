from fastapi import FastAPI
import src.main.service.task_service as task_service

from src.main.model.task_model import TaskModel, TaskCreateModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/task/{task_id}", response_model=TaskModel)
async def get_task(task_id: str):
    return task_service.get_task(task_id)


@app.post("/task", response_model=TaskModel)
async def create_task(task: TaskCreateModel):
    return task_service.create_task(task)
