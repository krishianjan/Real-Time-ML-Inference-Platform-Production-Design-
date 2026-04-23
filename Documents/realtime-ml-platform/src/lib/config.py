from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    kafka_bootstrap_servers: str = Field("localhost:9092", env="KAFKA_BOOTSTRAP_SERVERS")
    kafka_raw_topic: str = Field("raw-events", env="KAFKA_RAW_TOPIC")
    kafka_inference_topic: str = Field("inference-requests", env="KAFKA_INFERENCE_TOPIC")
    kafka_output_topic: str = Field("predictions", env="KAFKA_OUTPUT_TOPIC")
    
    redis_host: str = Field("localhost", env="REDIS_HOST")
    redis_port: int = Field(6379, env="REDIS_PORT")
    redis_db: int = Field(0, env="REDIS_DB")
    
    inference_port: int = Field(8080, env="INFERENCE_PORT")
    model_store_path: str = Field("/models", env="MODEL_STORE_PATH")
    
    prometheus_port: int = Field(9090, env="PROMETHEUS_PORT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()