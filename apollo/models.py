from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(244), index=True)
    email = Column(String(244), unique=True, index=True)
