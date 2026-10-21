from sqlalchemy import Column, Integer, String, Boolean
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



class Players(Base):
    """Classe représentant un joueur"""

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True) # 1 pour actif, 0 pour inactif
