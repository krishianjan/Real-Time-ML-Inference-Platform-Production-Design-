from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY
from fastapi import Response

request_count = Counter(
    "inference_requests_total",
    "Total inference requests",
    ["model_version", "status"]
)

request_latency = Histogram(
    "inference_request_duration_seconds",
    "Inference request latency",
    ["model_version"]
)

prediction_precision = Gauge(
    "inference_precision",
    "Current rolling precision of predictions"
)

def metrics_endpoint():
    return Response(content=generate_latest(REGISTRY), media_type="text/plain")