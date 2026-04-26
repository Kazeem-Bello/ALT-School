from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from schema.enrollment_schema import Enrollment, EnrollmentCreate
from services.enrollment_service import EnrollmentService
from dependency import is_student, is_admin



enrollment_router = APIRouter()

@enrollment_router.post("/", status_code = status.HTTP_201_CREATED)
async def enroll_student(enrollment: EnrollmentCreate, user = Depends(is_student)):
    enrollment_info = EnrollmentService.create_enrollment(enrollment)
    return enrollment_info


@enrollment_router.get("/", status_code = status.HTTP_200_OK)
async def retrieve_all_enrollments(user = Depends(is_admin)):
    return EnrollmentService.retrieve_all_enrollments()


@enrollment_router.get("/{user_id}", status_code = status.HTTP_200_OK)
async def retrieve_user_enrollments(user_id: int):
    return EnrollmentService.retrieve_user_enrollments(user_id)


@enrollment_router.get("/{course_id}", status_code = status.HTTP_200_OK)
async def retrieve_course_enrollments(course_id: int, user = Depends(is_admin)):
    return EnrollmentService.retrieve_course_enrollments(course_id)


@enrollment_router.delete("/", status_code = status.HTTP_200_OK)
async def deregister_student(enrollment_id: int, user = Depends(is_student)):
    return EnrollmentService.deregister_student(enrollment_id)

