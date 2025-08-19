from typing import Optional
from pydantic import BaseModel

class ClubBase(BaseModel):
    name: str
    location: str
    description: Optional[str] = None

class ClubCreate(ClubBase):
    pass

class ClubUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

class ClubRead(ClubBase):
    id: int

    class Config:
        from_attributes = True
