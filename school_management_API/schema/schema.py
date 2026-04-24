from pydantic import BaseModel, EmailStr
from typing import Literal 



class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Literal["student", 'admin']


class Course(BaseModel):
    id: str
    title:str
    code: int


class Enrollment(BaseModel):
    id: str
    user_id: str
    course_id: str