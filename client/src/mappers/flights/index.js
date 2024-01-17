const from = (data) => {
    return data.map(el => ({
        trail: el.trail.map(trail => [trail.lat, trail.lng]),
        airline: el.airline.name,
        flightNumber: el.identification.number.default,
        location: [el.trail[0].lat, el.trail[0].lng],
        time: {
            departure: new Date(+el.time.scheduled.departure * 1000).toLocaleString(),
            arrival: new Date(+el.time.scheduled.arrival * 1000).toLocaleString(),
        },
        thumbnail: el.aircraft.images.medium[0],
        origin: el.flightHistory.aircraft[0].airport.origin,
        destination: el.flightHistory.aircraft[0].airport.destination,
    }))
}

export default {from: from}