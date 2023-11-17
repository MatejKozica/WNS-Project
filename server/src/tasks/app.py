import requests
from celery import Celery

redis_url = "redis://wns_redis:6379"
celery = Celery(__name__, broker=redis_url, result_backend=redis_url)
celery.conf.beat_schedule = {
    'collect_data_5': {
        'task': 'collect_data',
        'schedule': 5,
    },
}
celery.conf.timezone = 'UTC'


def get_flight_radar_data(flight):
    resp = requests.get(
        f"https://www.flightradar24.com/v1/search/web/find?query={flight}&limit=50"
    )
    resp.raise_for_status()
    results = resp.json().get("results")
    target = None
    for result in results:
        if result["type"] != "live":
            continue
        detail = result.get("detail", {})
        if detail.get("callsign") != flight or detail.get("flight") != flight:
            target = result.get("id", None)
            break
    if not target:
        return None
    
    flight_data = requests.get(
        f"https://data-live.flightradar24.com/clickhandler/?version=1.5&flight={target}"
    )
    return flight_data.json()


@celery.task(name="collect_data")
def collect_data():
    resp = requests.get("http://plane_scanner:8080/data/aircraft.json")
    resp.raise_for_status()
    data = resp.json()
    aircrafts = []
    for aircraft in data.get("aircraft", []):
        if flight := aircraft.get("flight"):
            flight_data = get_flight_radar_data(flight.strip())
            aircrafts.append({**flight_data, "dump1090_data": data})

    print(aircrafts)