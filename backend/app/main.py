from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.redis import init_redis, close_redis

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize connections (Redis)
    await init_redis()
    yield
    # Close connections on shutdown
    await close_redis()

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

# CORS Middleware Configuration
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins  
        allow_credentials=False,  # Disallow credentials    
        allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
        allow_headers=["*"],  # Allow all headers
    )

# KEY RECORD: Include all v1 routes.
app.include_router(api_router, prefix=settings.API_V1_STR)