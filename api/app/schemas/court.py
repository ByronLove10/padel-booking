from typing import Optional
from decimal import Decimal
from pydantic import BaseModel

class CourtBase(BaseModel):
    club_id: int
    name: str
    surface_type: Optional[str] = None
    has_lights: bool = False
    price_per_hour: Optional[Decimal] = None

class CourtCreate(CourtBase):
    pass

class CourtUpdate(BaseModel):
    name: Optional[str] = None
    surface_type: Optional[str] = None
    has_lights: Optional[bool] = None
    price_per_hour: Optional[Decimal] = None

class CourtRead(CourtBase):
    id: int

    class Config:
        from_attributes = True
