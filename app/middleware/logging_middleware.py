import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware

logging.basicConfig(level=logging.INFO)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        s = time.time()
        r = await call_next(request)
        elapsed = time.time() - s
        logging.info(f"{request.method} {request.url.path} {elapsed:.3f}s")
        return r
