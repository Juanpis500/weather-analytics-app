import json
import httpx
import redis.asyncio as redis
from fastapi import HTTPException, status
from app.core.config import settings
from app.schemas.weather import CurrentWeatherResponse, MainMetrics, WindMetrics, WeatherDescription
from app.schemas.weather import ForecastResponse, ForecastItem

CACHE_TTL_SECONDS = 600  # 10 minutes

class OpenWeatherService:
    def __init__(self, redis_db: redis.Redis):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = settings.OPENWEATHER_BASE_URL
        self.redis = redis_db

    async def get_current_weather(self, city: str) -> CurrentWeatherResponse:
        cache_key = f"weather:{city.strip().lower()}"

        # 1. Attempt to retrieve from Redis (Cache Miss)
        cached_data = await self.redis.get(cache_key)
        if cached_data:
            data = json.loads(cached_data)
            data["cached"] = True
            return CurrentWeatherResponse(**data)

        # 2. Consult external API (Cache Miss)
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "en"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/weather", params=params)

            if response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"City '{city}' not found."
                )
            elif response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail="Error communicating with the weather service."
                )

            raw_data = response.json()

            # Structured mapping to Pydantic schemas
            weather_obj = CurrentWeatherResponse(
                name=raw_data["name"],
                country=raw_data["sys"]["country"],
                metrics=MainMetrics(**raw_data["main"]),
                wind=WindMetrics(**raw_data["wind"]),
                weather=WeatherDescription(**raw_data["weather"][0]),
                cached=False
            )

            # 3. Save to Redis using Pydantic's .model_dump_json()
            # The 'cached' field is excluded so that it defaults to False upon retrieval.
            await self.redis.set(
                name=cache_key,
                value=weather_obj.model_dump_json(exclude={"cached"}),
                ex=CACHE_TTL_SECONDS
            )

            return weather_obj

    async def get_forecast(self, city: str) -> ForecastResponse:
        cache_key = f"forecast:{city.strip().lower()}"

        # 1. Cache Hit
        cached_data = await self.redis.get(cache_key)
        if cached_data:
            data = json.loads(cached_data)
            data["cached"] = True
            return ForecastResponse(**data)

        # 2. Cache Miss
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "en"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/forecast", params=params)

            if response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"City '{city}' not found."
                )
            elif response.status_code != 200:
                raise HTTPException(
                    status_code=status.HTTP_502_BAD_GATEWAY,
                    detail="Error communicating with the weather service."
                )

            raw_data = response.json()

            forecast_items = [
                ForecastItem(
                    dt_txt=item["dt_txt"],
                    metrics=MainMetrics(**item["main"]),
                    wind=WindMetrics(**item["wind"]),
                    weather=WeatherDescription(**item["weather"][0]),
                    pop=item.get("pop", 0.0)
                )
                for item in raw_data["list"]
            ]

            forecast_obj = ForecastResponse(
                name=raw_data["city"]["name"],
                country=raw_data["city"]["country"],
                list=forecast_items,
                cached=False
            )

            # 3. Save to Redis (10 minutes)
            await self.redis.set(
                name=cache_key,
                value=forecast_obj.model_dump_json(exclude={"cached"}),
                ex=CACHE_TTL_SECONDS
            )

            return forecast_obj