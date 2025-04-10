from pydantic import BaseModel
from typing import Optional

class GoalInput(BaseModel):
    user_id: str
    goal: str
    deadline: str
    tone: str

class GoalResponse(BaseModel):
    goal: str
    deadline: str
    tone: str
    last_message: Optional[str] = None
