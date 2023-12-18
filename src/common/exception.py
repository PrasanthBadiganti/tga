from starlette.responses import JSONResponse


async def global_exception_handler(request, exception):
    return JSONResponse(status_code=500, content=str(exception))
