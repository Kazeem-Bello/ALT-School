from schema.user_schema import User, UserCreate, UserRole
from database.db import user_db

class UserService:

    @staticmethod
    def create_user(user: UserCreate):
        user_id = len(user_db) + 1
        user_data = User(
            id = user_id,    
            name = user.name,
            email = user.email,
            role = user.role
        )
        user_db[user_id] = user_data
        return user_data
    
    @staticmethod
    def get_users():
        if len(user_db) == 0:
            return "no user available in the database"
        return user_db
    
    @staticmethod
    def get_user_id(user_id: int):
        return user_db.get(user_id)
