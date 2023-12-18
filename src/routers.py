from fastapi import APIRouter
from src.api.endpoint import router

routers = APIRouter()
routers.include_router(router)
