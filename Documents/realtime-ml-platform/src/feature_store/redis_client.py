import redis
from src.lib.config import settings

class FeatureStore:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True
        )
    
    def get_features(self, user_id: str) -> dict:
        return self.client.hgetall(f"user:{user_id}")
    
    def set_features(self, user_id: str, features: dict):
        self.client.hset(f"user:{user_id}", mapping=features)

feature_store = FeatureStore()