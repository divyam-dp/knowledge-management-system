from fastapi import RouterAPI

from app.api.v1.enpoints.health import router as health_router

api_router = RouterAPI

api_router.include_router(health_router)