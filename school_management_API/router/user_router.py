from fastapi import APIRouter, HTTPException, status
from services.user_service import UserService
from schema.user_schema import User, UserCreate
   
user_router = APIRouter()


@user_router.post("/", status_code = status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    user_info = UserService.create_user(user)
    if not user_info.name:
        raise HTTPException(detail = "Please input your name", status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    return user_info

@user_router.get("/", status_code = status.HTTP_200_OK)
async def get_users():
    users = UserService.get_users()
    return users

@user_router.get("/{user_id}", status_code = status.HTTP_200_OK)
async def get_user_id(user_id: int):
    user = UserService.get_user_id(user_id)
    if not user:
        raise HTTPException(detail = "user not found", status_code = status.HTTP_404_NOT_FOUND)
    return user