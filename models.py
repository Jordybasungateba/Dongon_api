from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from database import Base


class Heroes(Base):
    """Classe représentant un héros"""

    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    nick_name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    occupation = Column(ARRAY(String), nullable=False)
    powers = Column(ARRAY(String), nullable=False)
    hobby = Column(ARRAY(String), nullable=False)
    type = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
