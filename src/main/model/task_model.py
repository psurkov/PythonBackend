from pydantic import BaseModel


class TaskModel(BaseModel):
    id: str
    name: str
    description: str
    original_score: float
    score_after_soft_deadline: float


class TaskCreateModel(BaseModel):
    name: str
    description: str
    original_score: float
