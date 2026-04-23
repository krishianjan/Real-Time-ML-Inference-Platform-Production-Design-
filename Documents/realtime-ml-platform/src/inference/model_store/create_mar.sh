#!/bin/bash

# Install torch-model-archiver if needed
pip install torch-model-archiver

# Generate dummy model
python train_dummy_model.py

# Create .mar archive
torch-model-archiver \
  --model-name dummy_model \
  --version 1.0 \
  --serialized-file model.pt \
  --handler ../handler.py \
  --export-path . \
  --force

echo "✅ dummy_model.mar created"