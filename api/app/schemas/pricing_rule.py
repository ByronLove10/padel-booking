from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class PricingRuleBase(BaseModel):
    club_id: int
    day_of_week: int  # 0 = Monday … 6 = Sunday
    time_range: str  # ej: "08:00-12:00"
    price_override: Decimal


class PricingRuleCreate(PricingRuleBase):
    pass


class PricingRuleUpdate(BaseModel):
    day_of_week: Optional[int] = None
    time_range: Optional[str] = None
    price_override: Optional[Decimal] = None


class PricingRuleRead(PricingRuleBase):
    id: int

    class Config:
        from_attributes = True
