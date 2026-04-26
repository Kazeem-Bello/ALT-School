from schema.user_schema import User, UserCreate, UserRole
from database.db import user_db
from fastapi import HTTPException, status

class UserService:

    @staticmethod
    def create_user(user: UserCreate) -> User:
        user_id = max(user_db.keys(), default = 0) + 1
        user_data = User(
            id = user_id,    
            name = user.name,
            email = user.email,
            role = user.role
        )
        if not user_data.name:
            raise HTTPException(detail = "Please input your name", status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
        user_db[user_id] = user_data
        return user_data
    
    @staticmethod
    def get_users():
        if len(user_db) == 0:
            raise HTTPException(detail = "no user available in the database", status_code = status.HTTP_404_NOT_FOUND)
        return user_db
    
    @staticmethod
    def get_user_id(user_id: int):
        user = user_db.get(user_id)
        if not user:
            raise HTTPException(detail = "user not found", status_code = status.HTTP_404_NOT_FOUND)
        return user
