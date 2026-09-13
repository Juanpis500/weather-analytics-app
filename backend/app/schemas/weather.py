from typing import List
from pydantic import BaseModel, ConfigDict, Field

class MainMetrics(BaseModel):
    temp: float = Field(..., description="Current temperature in Celsius")
    feels_like: float = Field(..., description="Apparent temperature / feels like")
    temp_min: float = Field(..., description="Minimum temperature")
    temp_max: float = Field(..., description="Maximum temperature")
    humidity: int = Field(..., description="Humidity percentage")
    pressure: int = Field(..., description="Atmospheric pressure in hPa")

class WindMetrics(BaseModel):
    speed: float = Field(..., description="Wind speed in m/s")
    deg: int = Field(..., description="Wind direction in degrees")

class WeatherDescription(BaseModel):
    main: str = Field(..., description="Weather condition group (Clear, Rain, Clouds, etc.)")
    description: str = Field(..., description="Detailed weather condition description")
    icon: str = Field(..., description="OpenWeatherMap icon code")

class CurrentWeatherResponse(BaseModel):
    city_name: str = Field(..., alias="name", description="City name")
    country: str = Field(..., description="Country code")
    metrics: MainMetrics
    wind: WindMetrics
    weather: WeatherDescription
    cached: bool = Field(False, description="Indicates whether the response comes from Redis cache")

    model_config = ConfigDict(populate_by_name=True)

class ForecastItem(BaseModel):
    dt_txt: str = Field(..., description="Forecast date and time (YYYY-MM-DD HH:MM:SS)")
    metrics: MainMetrics
    wind: WindMetrics
    weather: WeatherDescription
    pop: float = Field(0.0, description="Probability of precipitation (0 to 1)")

class ForecastResponse(BaseModel):
    city_name: str = Field(..., alias="name", description="City name")
    country: str = Field(..., description="Country code")
    list: List[ForecastItem] = Field(..., description="List of forecast entries")
    cached: bool = Field(False, description="Indicates whether the response comes from Redis cache")

    model_config = ConfigDict(populate_by_name=True)