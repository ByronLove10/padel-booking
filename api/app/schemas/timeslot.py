from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .common import TimeslotStatus

class TimeslotBase(BaseModel):
    court_id: int
    start_time: datetime
    end_time: datetime
    status: TimeslotStatus = "available"

class TimeslotCreate(TimeslotBase):
    pass

class TimeslotUpdate(BaseModel):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    status: Optional[TimeslotStatus] = None

class TimeslotRead(TimeslotBase):
    id: int

    class Config:
        from_attributes = True
