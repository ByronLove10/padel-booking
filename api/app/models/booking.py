from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class BookingStatus(str):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    court_id = Column(Integer, ForeignKey("courts.id"), nullable=False)
    timeslot_id = Column(Integer, ForeignKey("timeslots.id"), nullable=False)
    status = Column(String, default=BookingStatus.PENDING, nullable=False)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="bookings")
    court = relationship("Court", back_populates="bookings")
    timeslot = relationship("Timeslot", back_populates="bookings")
    payment = relationship("Payment", uselist=False, back_populates="booking")
