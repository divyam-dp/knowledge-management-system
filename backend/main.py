from fastapi import FastAPI
from app.api.v1.router import api_router
app = FastAPI(
    title="Knowledge Management System",
    description="An original knowledge and =documentation respository API",
    version="0.1.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
            "message": "Knowledge Mangement System API",
        }
