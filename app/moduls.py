from sqlalchemy import Column, INTEGER, Float, String, TIMESTAMP, text
from . database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class FoodItem(Base):
    __tablename__ = "fooditem"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String, nullable=False) 
    

