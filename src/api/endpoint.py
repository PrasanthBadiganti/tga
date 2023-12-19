from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.security import HTTPBearer
from fastapi_ratelimit import limiter
from starlette.responses import JSONResponse

from src.service.user_service import UserService

router = APIRouter(tags=["ops"], dependencies=[Depends(HTTPBearer())])


@router.get("/fetch-users")
@limiter.limit("2/minute")
async def fetch_users(request: Request):
    try:
        service = UserService()
        return service.fetch_all_users(request)
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
