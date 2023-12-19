import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
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
Instrumentator().instrument(app).expose(app)


@app.post("/prefilter")
async def prefilter_endpoint():
    # Your logic here
    return {"message": "Received POST request at /prefilter"}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
