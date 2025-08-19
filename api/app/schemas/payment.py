from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    booking_id: int
    amount: Decimal
    currency: str
    provider: Optional[str] = None
    status: Optional[str] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    amount: Optional[Decimal] = None
    currency: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[str] = None

class PaymentRead(PaymentBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
