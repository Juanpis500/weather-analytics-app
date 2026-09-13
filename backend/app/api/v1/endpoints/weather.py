from fastapi import APIRouter, Depends
import redis.asyncio as redis
from app.core.redis import get_redis
from app.schemas.weather import CurrentWeatherResponse
from app.services.openweather import OpenWeatherService
from app.schemas.weather import CurrentWeatherResponse, ForecastResponse

router = APIRouter()

@router.get("/current/{city}", response_model=CurrentWeatherResponse)
async def get_weather(
    city: str,
    redis_db: redis.Redis = Depends(get_redis)
):
    service = OpenWeatherService(redis_db=redis_db)
    return await service.get_current_weather(city)

@router.get("/forecast/{city}", response_model=ForecastResponse)
async def get_forecast(
    city: str,
    redis_db: redis.Redis = Depends(get_redis)
):
    service = OpenWeatherService(redis_db=redis_db)
    return await service.get_forecast(city)