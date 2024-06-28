<script>
  import { Router, Link, Route } from "svelte-routing";
  import Nav from "./Nav.svelte";
  import Home from "./Home.svelte";
  import About from "./About.svelte";
  import Tutorials from "./routes/Tutorials.svelte";

  export let url = "";
</script>

<Router {url}>
  <Nav />
  <main>
    <Route path="/" component={Home} />
    <Route path="/about" component={About} />
    <Route path="/Tutorials" component={Tutorials} />
  </main>
</Router>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
  }

  main {
    padding: 80px 20px 20px; /* Increased top padding to account for fixed navbar */
    max-width: 1200px;
    margin: 0 auto;
  }
</style>
