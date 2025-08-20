from fastapi import Depends, HTTPException, status
from app import models
from app.dependencies.auth import get_current_user


def require_role(*allowed_roles: str):
    def checker(user: models.User = Depends(get_current_user)) -> models.User:
        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
            )
        return user

    return checker
