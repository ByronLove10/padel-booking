from typing import Optional
from pydantic import BaseModel, EmailStr
from .common import UserRole


class UserBase(BaseModel):
    email: EmailStr
    name: str
    phone: Optional[str] = None
    role: UserRole


class UserCreate(UserBase):
    password: str  # llega plano, se convierte a hash en servicio


class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[UserRole] = None
    # password opcional si implementas cambio de contraseña:
    password: Optional[str] = None


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
