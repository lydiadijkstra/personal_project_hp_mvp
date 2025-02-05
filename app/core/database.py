# SQLAlchema
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os


load_dotenv()

# DB Data for localhost
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


#DATABASE_URL = os.getenv("DATABASE_URL") # Call DB from env for deployment at render


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # DB  localhost
#SQLALCHEMY_DATABASE_URL = f"{DATABASE_URL}" # DB deployed on Render


def initialize_database():
    """Initialize the database and create all tables."""
    Base.metadata.create_all(bind=engine)


engine = create_engine(
	SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
