from app.src.main.model.task_model import TaskModel

tasks = [
    TaskModel(id="30", name="Name1", description="description1", original_score=10.0, score_after_soft_deadline=0.3),
    TaskModel(id="239", name="Name2", description="description2", original_score=13.0, score_after_soft_deadline=0.5),
    TaskModel(id="566", name="Name3", description="description3", original_score=5.0, score_after_soft_deadline=0.1)
]


def get_task_by_id(task_id: str):
    return next(filter(lambda task: task.id == task_id, tasks), None)


def upsert_task(new_task):
    tasks.append(new_task)
