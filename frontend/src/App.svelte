<script>
  import { Router, Link, Route } from "svelte-routing";
  import Nav from "./Nav.svelte";
  import Home from "./Home.svelte";
  import About from "./About.svelte";

  export let url = "";
</script>

<Router {url}>
  <Nav />
  <main>
    <Route path="/" component={Home} />
    <Route path="/about" component={About} />
  </main>
</Router>

<style>
  main {
    padding: 20px;
  }
</style>
