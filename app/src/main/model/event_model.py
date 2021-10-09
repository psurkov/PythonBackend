from pydantic import BaseModel
from typing import List


class EventCreateModel(BaseModel):
    participants: List[str]
