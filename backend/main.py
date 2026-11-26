from fastapi import FastAPI

app = FastAPI(
    title="Knowledge Management System",
    description="An original knowledge and =documentation respository API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
            "message": "Knowledge Mangement System API",
        }
