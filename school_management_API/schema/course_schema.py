from pydantic import BaseModel, EmailStr, Field
from typing import Optional 


class CourseBase(BaseModel):
    title:str = Field((...), min_length = 1)
    code: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    code: Optional[int] = None