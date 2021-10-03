from pydantic import BaseModel


class EventCreateModel(BaseModel):
    participants: list[str]
