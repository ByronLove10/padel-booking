from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .common import BookingStatus


class BookingBase(BaseModel):
    user_id: int
    court_id: int
    timeslot_id: int
    status: BookingStatus = "pending"


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    status: Optional[BookingStatus] = None


class BookingRead(BookingBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
