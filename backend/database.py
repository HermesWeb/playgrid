from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# This is the connection string. 
# You MUST replace 'YOUR_PASSWORD' with the actual password you set when installing PostgreSQL.
# The default username is usually 'postgres'.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:playgrid123@localhost/playgrid_db"

# The engine is the actual bridge to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# This creates a temporary session every time someone makes a request to the app
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)