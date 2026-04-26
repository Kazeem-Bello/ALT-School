from pydantic import BaseModel
from typing import Literal 


class EnrollmentBase(BaseModel):
    user_id: str
    course_id: str

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
        id: int