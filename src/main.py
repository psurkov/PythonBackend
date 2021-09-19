from fastapi import FastAPI, HTTPException

from src.models.task import Task

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


ready_tasks = {
    "task1": {"name": "Task1", "description": "easy task", "score": 5.0},
    "task2": {"name": "Task2", "description": "medium task", "score": 10.0},
    "task3": {"name": "Task3", "description": "hard task", "score": 15.0},
}


@app.get("/task/{task_id}", response_model=Task)
async def root(task_id: str):
    if task_id not in ready_tasks:
        raise HTTPException(status_code=400, detail="Task {} isn't ready".format(task_id))
    return ready_tasks[task_id]


@app.post("/task")
async def root(task: Task):
    if task.score < 0:
        raise HTTPException(status_code=400, detail="The score cannot be negative")
    return "Task {} has been created. It's score is {} points. After a soft deadline it will become {} points".format(
        task.name, task.score, task.score * 0.8)
