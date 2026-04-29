from schema.enrollment_schema import Enrollment, EnrollmentBase, EnrollmentCreate
from schema.user_schema import UserRole
from fastapi import HTTPException, status
from database.db import enrollment_db, user_db, course_db



class EnrollmentService:

    @staticmethod
    def create_enrollment(enrollment: EnrollmentCreate):
        if enrollment.user_id not in user_db.keys():
            raise HTTPException(detail = "user not found", status_code = status.HTTP_404_NOT_FOUND)
        if enrollment.course_id not in course_db.keys():
            raise HTTPException(detail = "course not found", status_code = status.HTTP_404_NOT_FOUND)
        user = user_db[enrollment.user_id]
        if not user.role == UserRole.student:
            raise HTTPException(detail = "user not a student. Only a student can be enrolled", status_code = status.HTTP_409_CONFLICT)        
        if any(enrollment.user_id == existing_enrollment.user_id and enrollment.course_id == existing_enrollment.course_id for existing_enrollment in enrollment_db.values()):
            raise HTTPException(detail = "User is already enrolled in this course", status_code = status.HTTP_409_CONFLICT)        
        
        enrollment_id = max(enrollment_db.keys(), default = 0) + 1
        enrollment_info = Enrollment(
            user_id = enrollment.user_id,
            course_id = enrollment.course_id,
            id = enrollment_id
        )
        enrollment_db[enrollment_id] = enrollment_info

        return enrollment_info

    @staticmethod
    def retrieve_all_enrollments():
        if len(enrollment_db) == 0:
            raise HTTPException(detail = "no user enrollment yet", status_code = status.HTTP_404_NOT_FOUND)
        return enrollment_db
    
    @staticmethod
    def retrieve_user_enrollments(user_id: int):
        if user_id not in user_db.keys():
            raise HTTPException(detail = "user not found", status_code = status.HTTP_404_NOT_FOUND)
        user = user_db[user_id]
        if not user.role == UserRole.student:
            raise HTTPException(detail = "user not a student. Only a student can be enrolled", status_code = status.HTTP_409_CONFLICT)  
        user_enrollments = [enrollment for enrollment in enrollment_db.values() if enrollment.user_id == user_id]
        if not user_enrollments:
            raise HTTPException(detail = "the user has not enrolled in any course", status_code = status.HTTP_404_NOT_FOUND)
        return user_enrollments

    @staticmethod
    def retrieve_course_enrollments(course_id: int):
        if course_id not in course_db.keys():
            raise HTTPException(detail = "course not found", status_code = status.HTTP_404_NOT_FOUND)
        course_enrollments = [enrollment for enrollment in enrollment_db.values() if enrollment.course_id == course_id]
        if not course_enrollments:
            raise HTTPException(detail = "no user has enrolled in this course", status_code = status.HTTP_404_NOT_FOUND)
        return course_enrollments

    @staticmethod
    def deregister_student(enrollment_id: int):
        if enrollment_id not in enrollment_db.keys():
            raise HTTPException(detail = "enrollment_ID not found", status_code = status.HTTP_404_NOT_FOUND)
        del enrollment_db[enrollment_id]
        return {"status": f"user erollment with id-{enrollment_id} successfully deregistered"}
        
        