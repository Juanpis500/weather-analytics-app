from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Weather Analytics API"
    API_V1_STR: str = "/api/v1"
    OPENWEATHER_API_KEY: str
    OPENWEATHER_BASE_URL: str = "https://api.openweathermap.org/data/2.5"
    REDIS_URL: str = "redis://localhost:6379"

    # Allowed origins for CORS (Vue / Vite frontend)
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "https://weather-backend-a1ri.onrender.com",
        "https://weather-analytics-app-green.vercel.app"
    ]

    class Config:
        env_file = ".env"

settings = Settings()