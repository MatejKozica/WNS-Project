import { writable } from 'svelte/store'
import flightsMapper from '../mappers/flights/index'

export default function (url) {
	const loading = writable(false)
	const error = writable(false)
	const data = writable([])
	
	async function get() {
		loading.set(true)
		error.set(false)
		try {
			const response = await fetch(url)
			const flights = await response.json();
			data.set(await flightsMapper.from(!!flights.length ? flights : [flights]))
		} catch(e) {
			error.set(e)
		}
		loading.set(false)
	}
	
	return [ data, loading, error, get]
}