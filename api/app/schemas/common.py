from typing import Literal

# Enums como Literals (validación estricta)
UserRole = Literal["player", "club_manager", "admin"]
TimeslotStatus = Literal["available", "blocked"]
BookingStatus = Literal["pending", "paid", "cancelled", "expired"]
