from pydantic import BaseModel, EmailStr
from typing import Optional 


class CourseBase(BaseModel):
    title:str
    code: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    code: Optional[int] = None