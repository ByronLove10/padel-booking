from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Court(Base):
    __tablename__ = "courts"

    id = Column(Integer, primary_key=True, index=True)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    name = Column(String, nullable=False)
    surface_type = Column(String)
    has_lights = Column(Boolean, default=False)
    price_per_hour = Column(Numeric(10, 2))

    club = relationship("Club", back_populates="courts")
    timeslots = relationship("Timeslot", back_populates="court")
    bookings = relationship("Booking", back_populates="court")
