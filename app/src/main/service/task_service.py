import uuid

from fastapi import HTTPException

from app.src.main.dao import task_dao
from app.src.main.model.task_model import TaskCreateModel, TaskModel


def __validate_score(task: TaskCreateModel):
    if task.original_score < 0:
        raise HTTPException(status_code=400, detail="The score cannot be negative")


def __default_task_score_after_soft_deadline(original_task_score: float):
    return original_task_score * 0.8


def create_task(task: TaskCreateModel) -> TaskModel:
    __validate_score(task)
    score_after_soft_deadline = __default_task_score_after_soft_deadline(task.original_score)
    new_task = TaskModel(id=str(uuid.uuid4()),
                         name=task.name,
                         description=task.description,
                         original_score=task.original_score,
                         score_after_soft_deadline=score_after_soft_deadline
                         )
    task_dao.upsert_task(new_task)
    return new_task


def get_task(task_id):
    task = task_dao.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=400, detail="Task {} does not exist".format(task_id))
    return task
