from schema.user_schema import User, UserRole
from database.db import user_db
from services.user_service import UserService
from fastapi import HTTPException, status



def is_admin(user_id: int):
    user = UserService.get_user_id(user_id)
    if not user:
        raise HTTPException(detail = "user not found", status_code = status.HTTP_404_NOT_FOUND)
    if not user.role == UserRole.admin:
        raise HTTPException(detail = "you are not authorized to perform this operation", status_code = status.HTTP_403_FORBIDDEN)


def is_student(user_id: int):
    user = UserService.get_user_id(user_id)
    if not user:
        raise HTTPException(detail = "user not found", status_code = status.HTTP_404_NOT_FOUND)
    if not user.role == UserRole.student:
        raise HTTPException(detail = "you are not authorized to perform this operation", status_code = status.HTTP_403_FORBIDDEN)
