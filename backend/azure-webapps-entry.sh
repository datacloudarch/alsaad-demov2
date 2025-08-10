#!/usr/bin/env bash
set -euo pipefail

# Azure App Service startup script for FastAPI (gunicorn+uvicorn workers)

export PYTHONUNBUFFERED=1

WORKERS=${WORKERS:-4}
PORT=${PORT:-8000}

# Migrate or init tasks could be placed here in the future

exec gunicorn app.main:app \
  --workers ${WORKERS} \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:${PORT} \
  --timeout 120


