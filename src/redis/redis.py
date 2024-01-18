import aioredis
from config import REDIS_PORT, REDIS_HOST


class RedisClient:
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(
            redis_url, encoding="utf-8", decode_responses=True
        )

    async def get_value(self, key: str) -> str:
        return await self.redis.get(key)

    async def set_value(self, key: str, new_value) -> None:
        await self.redis.set(key, new_value, nx=True)

    async def update_value(self, key: str, new_value) -> None:
        await self.redis.set(key, new_value, xx=True)


REDIS = RedisClient(f"redis://{REDIS_HOST}:{REDIS_PORT}")
