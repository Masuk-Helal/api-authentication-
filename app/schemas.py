from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# User Schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRes(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# FoodItem Schemas
class FoodItemCreate(BaseModel):
    name: str
    price: float
    image: str


class FoodItemRes(BaseModel):
    id: int
    name: str
    price: float
    image: str

    class Config:
        from_attributes = True