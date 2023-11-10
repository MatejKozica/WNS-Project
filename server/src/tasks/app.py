import requests
from celery import Celery

redis_url = "redis://wns_redis:6379"
celery = Celery(__name__, broker=redis_url, result_backend=redis_url)
celery.conf.beat_schedule = {
    'test-every-5-seconds': {
        'task': 'test',
        'schedule': 5,
    },
}
celery.conf.timezone = 'UTC'


@celery.task(name="test")
def create_task():
    data = requests.get("http://plane_scanner:8080/data/aircraft.json")
    print(data.json())
    return True