<script>
    import {getContext} from 'svelte';
    import {writable} from 'svelte/store';
    import { Navbar, Title, Divider, Text, Group } from '@svelteuidev/core';
    import {selectedFlightStore} from '../../store/flightsStore';
</script>

<Navbar slot="navbar" width={{base: 340}}>
    {#if !Object.keys($selectedFlightStore).length}
        Click on some aircraft
    {:else}
        <img src={$selectedFlightStore.thumbnail?.src}>
        <Title order={2}>{$selectedFlightStore?.airline} - {$selectedFlightStore?.flightNumber}</Title>
        <Divider />
        <Group>
            <Text><b>Origin:</b> {$selectedFlightStore.origin?.name}</Text>
            <Text><b>Destination:</b> {$selectedFlightStore?.destination?.name}</Text>
        </Group>
        <Divider />
        <Group>
            <Text><b>Departure:</b> {$selectedFlightStore?.time.departure}</Text>
            <Text><b>Arrival:</b> {$selectedFlightStore?.time?.arrival}</Text>
        </Group>
    {/if}
</Navbar>