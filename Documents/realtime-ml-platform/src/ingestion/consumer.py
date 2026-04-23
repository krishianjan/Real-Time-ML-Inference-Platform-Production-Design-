import json
import time
from kafka import KafkaConsumer, KafkaProducer
import redis
import structlog
from src.lib.config import settings
from src.lib.logging import logger

def main():
    consumer = KafkaConsumer(
        settings.kafka_raw_topic,
        bootstrap_servers=settings.kafka_bootstrap_servers,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='ingestion-group',
        auto_offset_reset='latest',
        enable_auto_commit=True
    )
    
    producer = KafkaProducer(
        bootstrap_servers=settings.kafka_bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    r = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        db=settings.redis_db,
        decode_responses=True
    )
    
    logger.info("Ingestion consumer started", topic=settings.kafka_raw_topic)
    
    for message in consumer:
        event = message.value
        event_id = event.get("event_id")
        
        # Enrich with cached features
        user_id = event.get("user_id")
        if user_id:
            cached_features = r.hgetall(f"user:{user_id}")
            event["features"] = cached_features
        
        # Forward to inference topic
        producer.send(settings.kafka_inference_topic, value=event)
        logger.debug("Event forwarded to inference", event_id=event_id)

if __name__ == "__main__":
    main()