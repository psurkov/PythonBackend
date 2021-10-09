from app.src.main.model.task_model import TaskModel
import app.src.main.database as database


def get_task_by_id(task_id: str):
    res = database.execute('''
    select * from tasks where id = '{}'
    '''.format(task_id), True)
    if len(res) == 0:
        return None
    id, name, description, original_score, score_after_soft_deadline = res[0]
    return TaskModel(id=id,
                     name=name,
                     description=description,
                     original_score=original_score,
                     score_after_soft_deadline=score_after_soft_deadline)


def upsert_task(new_task):
    database.execute('''
    insert into tasks(id, name, description, original_score, score_after_soft_deadline)
    values ('{}', '{}', '{}', '{}', '{}')
    '''.format(
        new_task.id,
        new_task.name,
        new_task.description,
        new_task.original_score,
        new_task.score_after_soft_deadline)
    )
