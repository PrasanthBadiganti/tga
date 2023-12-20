import datetime
from typing import List

from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.security import HTTPBearer
from fastapi_ratelimit import limiter
from prometheus_client import Counter
from starlette.responses import JSONResponse

from src.service.async_service import AsyncService
from src.service.user_service import UserService

async_vs_sync_router = APIRouter(tags=["async_vs_sync"], dependencies=[Depends(HTTPBearer())])

requests_counter = Counter('my_async_sync_requests_total', 'Total number of requests')


@async_vs_sync_router.post("/execute_async_query")
@limiter.limit("5/minute")
async def execute_async_query(request: Request, tables: List[str]):
    try:
        service = AsyncService()
        start_time = datetime.datetime.now()
        response = await service.execute_asynchronous_query(tables)
        end_time = datetime.datetime.now()
        return JSONResponse(status_code=200,
                            content={"time_taken_in_seconds": (end_time - start_time).seconds, "response": response})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})


@async_vs_sync_router.post("/execute_sync_query")
@limiter.limit("5/minute")
async def execute_sync_query(request: Request, tables: List[str]):
    try:
        service = AsyncService()
        start_time = datetime.datetime.now()
        response = service.execute_synchronous_query(tables)
        end_time = datetime.datetime.now()
        return JSONResponse(status_code=200,
                            content={"time_taken_in_seconds": (end_time - start_time).seconds, "response": response})
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
