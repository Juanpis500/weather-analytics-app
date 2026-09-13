import redis.asyncio as redis
from app.core.config import settings

# Global Redis client instance
redis_client: redis.Redis | None = None

async def init_redis():
    """Initializes the connection to Redis."""
    global redis_client
    redis_client = redis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True
    )

async def close_redis():
    """Closes the connection to Redis when the app shuts down."""
    global redis_client
    if redis_client:
        await redis_client.close()

async def get_redis() -> redis.Redis:
    """Dependency injection for obtaining the Redis client."""
    if redis_client is None:
        raise RuntimeError("Redis has not been initialized.")
    return redis_client