from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class TimeslotStatus(str):
    AVAILABLE = "available"
    BLOCKED = "blocked"


class Timeslot(Base):
    __tablename__ = "timeslots"

    id = Column(Integer, primary_key=True, index=True)
    court_id = Column(Integer, ForeignKey("courts.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String, default=TimeslotStatus.AVAILABLE, nullable=False)

    court = relationship("Court", back_populates="timeslots")
    bookings = relationship("Booking", back_populates="timeslot")
