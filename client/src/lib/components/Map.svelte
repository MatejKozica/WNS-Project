<script>
import L from 'leaflet';
import * as markerIcons from '../../assets/markers';
import {onMount, getContext} from 'svelte';

let data = getContext('data');

console.log('data', data)

let map;
let markerLayers;
let markers = new Map();

const initialView = [43.5147, 16.4435];
const markerLocations = [initialView];

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

function markerIcon() {
    let html = `<div class="map-marker">${markerIcons.library}</div>`;
    return L.divIcon({
        html,
        className: 'map-marker'
    });
}

function createMarker(loc) {
    let icon = markerIcon();
    let marker = L.marker(loc, {
        icon
    });

    return marker;
}

function mapAction(container) {
    map = createMap(container);

    markerLayers = L.layerGroup()
    for (let location of markerLocations) {
        let m = createMarker(location);
        markerLayers.addLayer(m);
    }

    markerLayers.addTo(map);

    return {
        destroy: () => {
            map.remove();
            map = null;
        }
    };
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
