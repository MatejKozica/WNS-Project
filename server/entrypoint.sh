#!/bin/bash

if [ "$1" = "api_dev" ]; then
  exec uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
fi

if [ "$1" = "api" ]; then
  exec gunicorn src.app:app --config=config/gunicorn_config.py --bind=:8000 --preload
fi

if [ "$1" = "worker" ]; then
  exec celery -A src.tasks.celery worker
fi

if [ "$1" = "scheduler" ]; then
  exec celery -A src.tasks.celery beat
fi

exec "$@"
