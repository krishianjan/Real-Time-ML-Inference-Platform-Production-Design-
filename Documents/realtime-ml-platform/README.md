# Real‑Time ML Inference Platform

[![CI/CD](https://github.com/your-org/realtime-ml-platform/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/your-org/realtime-ml-platform/actions/workflows/ci-cd.yml)

A production‑grade, horizontally scalable ML inference system capable of **10,000+ requests/second** with **<100ms p95 latency**.

## Architecture

```mermaid
graph LR
    A[Client] -->|Raw Events| B[Kafka]
    B --> C[Ingestion Service]
    C -->|Enrich| D[Redis Feature Store]
    C -->|Inference Requests| E[Kafka Topic]
    E --> F[Inference Service (GPU)]
    F -->|Predictions| G[Kafka Topic]
    G --> H[Downstream Consumers]
    
    subgraph Observability
        F --> I[Prometheus]
        I --> J[Grafana]
    end