from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

class UserRole(str):
    PLAYER = "player"
    CLUB_MANAGER = "club_manager"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default=UserRole.PLAYER, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String)

    bookings = relationship("Booking", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")
