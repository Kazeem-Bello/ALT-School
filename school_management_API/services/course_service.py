from schema.course_schema import Course, CourseBase, CourseCreate, CourseUpdate
from database.db import course_db
from fastapi import HTTPException, status


class CourseService:

    @staticmethod
    def create_course(course: CourseCreate):
        if any(course.code == existing_course.code for existing_course in course_db.values()):
            raise HTTPException(detail = "course code already exist", status_code = status.HTTP_409_CONFLICT)
        course_id = max(course_db.keys(), default = 0) + 1
        course_info = Course(
            id = course_id,
            title = course.title,
            code = course.code
        )

        course_db[course_id] = course_info
        return course_info
    
    @staticmethod
    def get_courses():
        if len(course_db) == 0:
            return "no course in the database"
        return course_db
    
    @staticmethod
    def get_course_id(course_id: int):
        return course_db.get(course_id)

    @staticmethod
    def update_course(course_id: int, course_info: CourseUpdate):
        if course_id not in course_db.keys():
            raise HTTPException(detail = "Course not found", status_code = status.HTTP_404_NOT_FOUND)
        course = course_db[course_id]
        if course_info.title:
            course.title = course_info.title
        if course_info.code:
            course.code = course_info.code
        return course

    @staticmethod
    def delete_course(course_id: int):
        if course_id not in course_db.keys():
            raise HTTPException(detail = "Course not found", status_code = status.HTTP_404_NOT_FOUND)
        del course_db[course_id]
        return {"status": f"course with id-{course_id} deleted successfully"}

