from fastapi import APIRouter
from src.api.flag_based_endpoint import router
from src.api.async_endpoint import async_vs_sync_router

routers = APIRouter()
routers.include_router(router)
routers.include_router(async_vs_sync_router)
