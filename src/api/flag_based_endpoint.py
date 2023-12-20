from fastapi import APIRouter
from fastapi import Header
from fastapi import Request, Depends
from fastapi.security import HTTPBearer
from fastapi_ratelimit import limiter
from prometheus_client import Counter
from starlette.responses import JSONResponse
from src.service.user_service import UserService

router = APIRouter(tags=["flag_based_rollout"], dependencies=[Depends(HTTPBearer())])
requests_counter = Counter('my_requests_total', 'Total number of requests')


@router.get("/fetch-users")
@limiter.limit("5/minute")
async def fetch_users(request: Request, flag_enabled: bool = Header(False)):
    requests_counter.inc()
    try:
        service = UserService()
        return service.fetch_all_users(request, flag_enabled)
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
