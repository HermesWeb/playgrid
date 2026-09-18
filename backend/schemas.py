from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# --- USERS ---
class UserCreate(BaseModel):
    name: str
    phone_number: str
    role: str = "player"

class UserResponse(BaseModel):
    id: int
    name: str
    phone_number: str
    role: str

    class Config:
        from_attributes = True

# --- FACILITIES ---
class FacilityCreate(BaseModel):
    owner_id: int
    name: str
    location: str
    sport_type: str = "Football"
    price_per_hour: float

class FacilityResponse(BaseModel):
    id: int
    owner_id: int
    name: str
    location: str
    sport_type: str
    price_per_hour: float

    class Config:
        from_attributes = True

# --- BOOKINGS ---
class BookingCreate(BaseModel):
    facility_id: int
    user_id: int
    start_time: datetime
    end_time: datetime

class BookingResponse(BaseModel):
    id: int
    facility_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    status: str
    payment_reference: Optional[str] = None

    class Config:
        from_attributes = True