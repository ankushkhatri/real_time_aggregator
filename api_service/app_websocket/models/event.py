from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    user_id: int
    event_type: str
    timestamp: datetime