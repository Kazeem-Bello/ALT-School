from fastapi import FastAPI, APIRouter, HTTPException
from schema.schema import User, Course, Enrollment

app = APIRouter()


@app.get("/")
async def list_users(user:User):
    if user:
        return user