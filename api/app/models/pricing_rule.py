from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class PricingRule(Base):
    __tablename__ = "pricing_rules"

    id = Column(Integer, primary_key=True, index=True)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    day_of_week = Column(Integer)  # 0=Monday … 6=Sunday
    time_range = Column(String)
    price_override = Column(Numeric(10, 2))

    club = relationship("Club", back_populates="pricing_rules")
