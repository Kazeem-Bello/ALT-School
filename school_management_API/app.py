from fastapi import FastAPI
from router.user_router import user_router
from router.course_router import course_router

app = FastAPI()

app.include_router(user_router, prefix = "/user", tags = ["user"])
app.include_router(course_router, prefix = "/course", tags = ["course"])