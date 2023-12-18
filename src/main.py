import uvicorn
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.common.exception import global_exception_handler
from src.middleware.auth import AuthMiddleware
from src.routers import routers

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_middleware(AuthMiddleware)
app.include_router(routers)
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8080)
