
from datetime import date
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

class Priority(str, Enum):
    high = "High"
    medium = "Medium"
    low = "Low"


class Todo_obj():

    def __init__(self, **args) -> None:
        for k in args:
            setattr(self, k, args[k])
        
    def __repr__(self) -> str:
        return ToDo(self.id, self.name, self.owner, self.due_date, self.description, self.done, self.priority)

class ToDo(BaseModel):
    id: Optional[UUID] = uuid4
    name: str
    owner: str
    due_date: date
    description: str
    done: Optional[bool] = False
    priority: Priority