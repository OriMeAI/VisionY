from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pymongo.errors import PyMongoError
import logging
from app.locales.translations import get_translation

"""
使用
raise HTTPException(status_code=404)

替换 abort(404)
"""
     
def register_exception_handlers(fast_app: FastAPI):
    @fast_app.exception_handler(401)
    async def handle_401(request: Request, exc):
        logging.warning(f"401 at {request.url.path}, Error: {str(exc)}")
        return JSONResponse(
            status_code=401,
            content={
                "code": 800,
                "data": {},
                "msg": get_translation("user_not_login")
            }
        )
        
    @fast_app.exception_handler(404)
    async def handle_404(request: Request, exc):
        logging.warning(f"404 at {request.url.path}, Error: {str(exc)}")
        return JSONResponse(
            status_code=404,
            content={
                "code": 404,
                "data": {},
                "msg": get_translation("API_not_found")
            }
        )

    @fast_app.exception_handler(500)
    async def handle_500(request: Request, exc):
        logging.error(f"500 at {request.url.path}, Error: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "code": 500,
                "data": {},
                "msg": get_translation("server_inner_error")
            }
        )

    @fast_app.exception_handler(PyMongoError)
    async def handle_mongo_exception(request: Request, exc: PyMongoError):
        logging.error(f"PyMongoError: at {request.url.path}, {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "code": 500,
                "data": {},
                "msg": get_translation("DB_inner_error")
            }
        )
        
    @fast_app.exception_handler(HTTPException)
    async def handle_http_exception(request: Request, exc: HTTPException):
        logging.critical(f"handle_http_exception: at {request.url.path}, {str(exc)}")
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail if isinstance(exc.detail, dict) else {
                "code": exc.status_code,
                "data": {},
                "msg": str(exc.detail)
            }
        )

    @fast_app.exception_handler(Exception)
    async def handle_generic_exception(request: Request, exc: Exception):        
        logging.critical(f"handle_generic_error: at {request.url.path}, {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "code": 500,
                "data": {},
                "msg": get_translation("server_inner_error")
            }
        )