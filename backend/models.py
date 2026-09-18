from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship

# This Base class is the foundation that all our database tables will inherit from
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    role = Column(String, default="player") # "player" or "owner"
    
    # These relationships allow us to link tables together easily
    bookings = relationship("Booking", back_populates="user")
    facilities = relationship("Facility", back_populates="owner")

class Facility(Base):
    __tablename__ = 'facilities'
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id')) # Links to the User who owns it
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    sport_type = Column(String, default="Football")
    price_per_hour = Column(Float, nullable=False)
    
    owner = relationship("User", back_populates="facilities")
    bookings = relationship("Booking", back_populates="facility")

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True, index=True)
    facility_id = Column(Integer, ForeignKey('facilities.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    
    status = Column(String, default="pending") # "pending", "confirmed", or "cancelled"
    payment_reference = Column(String, unique=True) # Where we will store the Paystack transaction ID
    
    user = relationship("User", back_populates="bookings")
    facility = relationship("Facility", back_populates="bookings")