<script>
  import Map from "./lib/components/Map.svelte";
  import { SvelteUIProvider } from '@svelteuidev/core';
  import {setContext} from 'svelte';
  import { fns, AppShell, Navbar, Header, Title, Divider } from '@svelteuidev/core';


  setContext('data', 'something');
  

</script>

<SvelteUIProvider themeObserver="dark">
  <AppShell>
    <Navbar slot="navbar" width={{base: 340}}>
      Something is here
    </Navbar>
    <slot><Map /></slot>
  </AppShell>
</SvelteUIProvider>
