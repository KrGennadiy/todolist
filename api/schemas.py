from pydantic import BaseModel
class Task(BaseModel):
    text: str
    id: int | None = None


class PushTask(BaseModel):
    text: str

class DeleteTask(BaseModel):
    id: int
