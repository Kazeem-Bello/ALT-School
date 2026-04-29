from fastapi import APIRouter, HTTPException, status
from services.user_service import UserService
from schema.user_schema import User, UserCreate
   
user_router = APIRouter()


@user_router.post("/", status_code = status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return UserService.create_user(user)


@user_router.get("/", status_code = status.HTTP_200_OK)
async def get_users():
    return UserService.get_users()
     

@user_router.get("/{user_id}", status_code = status.HTTP_200_OK)
async def get_user_by_id(user_id: int):
    return UserService.get_user_id(user_id)
    