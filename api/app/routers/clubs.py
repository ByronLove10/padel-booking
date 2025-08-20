from fastapi import APIRouter, Depends
from app.core.deps import require_role
from app import models

router = APIRouter(prefix="/clubs", tags=["clubs"])


@router.post("/")
def create_club(
    current_user: models.User = Depends(require_role("club_manager", "admin"))
):
    # placeholder de prueba
    return {"ok": True, "by": current_user.email}


@router.get("/admin-only")
def admin_only(current_user: models.User = Depends(require_role("admin"))):
    return {"ok": True, "role": current_user.role}
