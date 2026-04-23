import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "raw-events"

for i in range(10):
    event = {
        "event_id": f"evt_{i}",
        "user_id": f"user_{random.randint(1,5)}",
        "features": [random.random() for _ in range(10)]  # 10 random features
    }
    producer.send(topic, value=event)
    print(f"Sent: {event}")
    time.sleep(1)

producer.flush()
print("✅ 10 test events sent to Kafka")