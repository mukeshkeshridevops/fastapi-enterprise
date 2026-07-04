from fastapi import FastAPI

# Middleware
from app.middleware.logging_middleware import LoggingMiddleware

# Exception Handler
from app.core.exceptions import AppException, app_exception_handler

# Routers
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.employees import router as employees_router
from app.api.v1.departments import router as departments_router
from app.api.v1.health import router as health_router

app = FastAPI(
    title="Enterprise FastAPI",
    description="Production Ready FastAPI Application",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Register Middleware
app.add_middleware(LoggingMiddleware)

# Register Exception Handlers
app.add_exception_handler(AppException, app_exception_handler)

# Register Routers
app.include_router(health_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(employees_router, prefix="/api/v1")
app.include_router(departments_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
def root():
    return {
        "application": "Enterprise FastAPI",
        "version": "1.0.0",
        "status": "Running"
    }
