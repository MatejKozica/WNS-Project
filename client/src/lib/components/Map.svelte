<script>
import L from 'leaflet';
import * as markerIcons from '../../assets/markers';
import {selectedFlightStore} from '../../store/flightsStore';
import fetchStore from '../../services/fetch'
import { onMount } from 'svelte';

let map;
let markerLayers;
let lines;

const [data, loading, error, get] = fetchStore('http://localhost:8000/flights');

data.subscribe(value => {
    updateMarkers(value); 
    updateLines(value.find(el => el.flightNumber === $selectedFlightStore.flightNumber)?.trail);
});
selectedFlightStore.subscribe(value => updateLines(value?.trail))


onMount(get);

setInterval(() => {
  get();
}, 2000)

const initialView = [43.577499, 16.417471];

function createMap(container) {
    let m = L.map(container, {
        preferCanvas: true
    }).setView(initialView, 9);
    L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
            attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
              &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
            subdomains: 'abcd',
            maxZoom: 14,
        }
    ).addTo(m);

    return m;
}

function markerIcon(label) {
    let html = `<div style="transform: translateY(-25px)"><label>${label}</label><div class="map-marker">${markerIcons.library}</div></div>`;
    return L.divIcon({
        html,
        className: 'map-marker'
    });
}

function createMarker(data) {
    let icon = markerIcon(data.flightNumber);
    let marker = L.marker(data.location, {
        icon
    })
    .on('click', () => selectedFlightStore.set(data));

    return marker;
}

function mapAction(container) {
    map = createMap(container);

    return {
        destroy: () => {
            map.remove();
            map = null;
        }
    };
}

function updateMarkers(markers){
    if(markerLayers){
        map.removeLayer(markerLayers);
        markerLayers = null;
    }
    if(!markers.length){
        return;
    }
    
    markerLayers = L.layerGroup()
    for (let marker of markers) {
        let m = createMarker(marker);
        markerLayers.addLayer(m);
    }

    markerLayers.addTo(map);
    updateLines($selectedFlightStore.trail)
}

function updateLines(markers) {
    if (lines) {
        map.removeLayer(lines)
        lines = null;
    }
    if(!markers?.length){
        return;
    }
	lines = L.polyline(markers, { color: '#E4E', opacity: 0.5 });
    lines.addTo(map);
	}

</script>

<div class="map" use:mapAction/>

<style>
.map {
    height: 97vh;
    width: 100%;
}

.map :global(.map-marker) {
    width: 30px;
    color: blue;
}
</style>
