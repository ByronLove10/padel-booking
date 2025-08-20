from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel

# Ojo: en el modelo SQLAlchemy renombraste metadata -> details para evitar conflicto.


class AuditLogBase(BaseModel):
    user_id: int
    action: str
    details: Optional[Dict[str, Any]] = None
    timestamp: datetime


class AuditLogCreate(AuditLogBase):
    pass


class AuditLogRead(AuditLogBase):
    id: int

    class Config:
        from_attributes = True
