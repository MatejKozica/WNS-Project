from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.cache import cache

import json

app = FastAPI()

origins = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/flights")
async def flights_all():
    data = cache.get("all_flights")

    return data


@app.get("/flights/{flight_id}")
async def flights_all(flight_id):
    data = cache.get(flight_id)
    return data



@app.get("/test")
async def test_data():
    with open("test.json") as file:
        result = file.read()
    return json.loads(result)