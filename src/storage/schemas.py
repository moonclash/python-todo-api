from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None
    completed: bool

    class Config:
        orm_mode = True

class CreateTaskDTO(BaseModel):
    title: str
    description: str | None
    completed: bool | None

class SearchTaskDTO(BaseModel):
    task_id: str | None
    title: str | None
    description: str | None
    completed: bool | None

class UpdateTaskDTO(BaseModel):
    title: str | None
    description: str | None
    completed: bool | None
    