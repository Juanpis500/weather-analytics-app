from fastapi import APIRouter
from app.api.v1.endpoints import weather

api_router = APIRouter()

# We include the weather routes under the /weather prefix.
api_router.include_router(weather.router, prefix="/weather", tags=["Weather"])