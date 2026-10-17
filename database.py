from typing import Annotated, TypeAlias

from fastapi import Depends
from sqlalchemy import create_engine 
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://fastapi:fastapi_dev_password@localhost:5432/fastapi_db"

# create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base class for our models
Base = declarative_base()


def get_db():
    """
    Dependency function to get a database session.
    This function can be used in FastAPI routes to provide a database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DbDependency: TypeAlias = Annotated[Session, Depends(get_db)]
