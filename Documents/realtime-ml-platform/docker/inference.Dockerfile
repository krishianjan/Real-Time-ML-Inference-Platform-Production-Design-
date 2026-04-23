FROM pytorch/torchserve:latest-gpu

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY src/inference/handler.py /home/model-server/
COPY config.properties /home/model-server/

USER model-server
WORKDIR /home/model-server

CMD ["torchserve", "--start", "--model-store", "/home/model-server/model-store", "--ts-config", "/home/model-server/config.properties"]