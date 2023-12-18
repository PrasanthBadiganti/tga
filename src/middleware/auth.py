from expiringdict import ExpiringDict
from fastapi import Request, Response
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.common.constants import PRIVILEGES_DICT, Constants

cache = ExpiringDict(max_len=100, max_age_seconds=60)


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        authorize_request(request)
        return await call_next(request)


def get_privileges_from_wal(token):
    # 1 Decode token using hantweb key
    # 2 Obtain username from the claims
    # 3 Get respective privileges from WAL by passing the username.
    return PRIVILEGES_DICT.get(token)


def authorize_request(request: Request):
    # Get the Bearer token from the Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Authorization header missing or invalid"})

    token = auth_header.split("Bearer ")[1].strip()
    if cache.get(token) is None:
        if token not in Constants.ALLOWED_USERS:
            raise Exception('User not allowed')
        privileges = get_privileges_from_wal(token)
        if privileges is None or privileges != ['READ', 'WRITE']:
            raise Exception('Invalid token')
        cache.update({token: privileges})
