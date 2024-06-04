# FastAPI
from fastapi import FastAPI

# Import routers
from .auth import router as auth_router

# Add imported routers
def register_routers(app: FastAPI):
    routers = [
        auth_router,
    ]

    for router in routers:
        app.include_router(router)