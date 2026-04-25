from pydantic import BaseModel, EmailStr
from typing import Literal 
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    user = "student"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int







