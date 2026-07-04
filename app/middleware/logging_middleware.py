from starlette.middleware.base import BaseHTTPMiddleware
import time,logging
logging.basicConfig(level=logging.INFO)
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request,call_next):
        s=time.time()
        r=await call_next(request)
        logging.info(f"{request.method} {request.url.path} {(time.time()-s):.3f}s")
        return r
