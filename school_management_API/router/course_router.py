from fastapi import FastAPI, APIRouter, HTTPException, status, Depends
from schema.course_schema import CourseCreate, CourseUpdate
from services.course_service import CourseService
from dependency import is_admin

course_router = APIRouter()


@course_router.post("/", status_code = status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, user = Depends(is_admin)):
    course_info = CourseService.create_course(course)
    return course_info


@course_router.get("/", status_code = status.HTTP_200_OK)
async def get_courses():
    return CourseService.get_courses()
  

@course_router.get("/{course_id}", status_code = status.HTTP_200_OK)
async def get_course_by_id(course_id: int):
    return CourseService.get_course_id(course_id)
   

@course_router.patch("/{course_id}", status_code = status.HTTP_200_OK)
async def update_course(course_id: int, course_info:CourseUpdate, user = Depends(is_admin)):
    return CourseService.update_course(course_id, course_info)


@course_router.delete("/", status_code = status.HTTP_200_OK)
async def delete_course(course_id: int, user = Depends(is_admin)):
    return CourseService.delete_course(course_id)