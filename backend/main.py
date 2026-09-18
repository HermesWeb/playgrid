from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

# Creates the tables (you already know this part!)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# This is a helper function that opens a temporary door to the database for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "PlayGrid API and Database are officially linked!"}

# --- OUR FIRST REAL ENDPOINT ---
# This allows the mobile app to send a POST request to create a new user
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Package the incoming data into our database model
    db_user = models.User(name=user.name, phone_number=user.phone_number, role=user.role)
    
    # 2. Add it to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # 3. Return the saved user back to the app
    return db_user
# --- FACILITY ENDPOINTS ---

# 1. Create a new facility
@app.post("/facilities/", response_model=schemas.FacilityResponse)
def create_facility(facility: schemas.FacilityCreate, db: Session = Depends(get_db)):
    db_facility = models.Facility(
        owner_id=facility.owner_id,
        name=facility.name,
        location=facility.location,
        sport_type=facility.sport_type,
        price_per_hour=facility.price_per_hour
    )
    db.add(db_facility)
    db.commit()
    db.refresh(db_facility)
    return db_facility

# 2. Get a list of all facilities (for the mobile app explore feed)
@app.get("/facilities/", response_model=list[schemas.FacilityResponse])
def get_all_facilities(db: Session = Depends(get_db)):
    facilities = db.query(models.Facility).all()
    return facilities
# --- BOOKING ENDPOINTS ---

@app.post("/bookings/", response_model=schemas.BookingResponse)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    # 1. The Overlap Check (The Core Business Logic)
    # We query the database to see if ANY existing booking at this turf overlaps with the requested times.
    overlapping_booking = db.query(models.Booking).filter(
        models.Booking.facility_id == booking.facility_id,
        models.Booking.status != "cancelled", # Ignore cancelled games
        models.Booking.start_time < booking.end_time,
        models.Booking.end_time > booking.start_time
    ).first()

    # 2. Block the booking if an overlap exists
    if overlapping_booking:
        raise HTTPException(status_code=400, detail="Sorry, boss. This time slot is already booked!")

    # 3. If the slot is free, lock it in as "pending"
    db_booking = models.Booking(
        facility_id=booking.facility_id,
        user_id=booking.user_id,
        start_time=booking.start_time,
        end_time=booking.end_time,
        status="pending"
    )
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking