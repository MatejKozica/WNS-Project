<script>
  import Map from "./lib/components/Map.svelte";
  import Navbar from "./lib/components/Navbar.svelte"
  import { SvelteUIProvider } from '@svelteuidev/core';
  import { AppShell} from '@svelteuidev/core';

</script>

<SvelteUIProvider themeObserver="dark">
  <AppShell>
    <Navbar />
    <slot><Map /></slot>
  </AppShell>
</SvelteUIProvider>
