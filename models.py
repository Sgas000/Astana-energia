from pydantic import BaseModel
from datetime import date

class Task(BaseModel):
    id: int
    equipment_type: str
    status: str
    technician: str
    date: date
    description: str
