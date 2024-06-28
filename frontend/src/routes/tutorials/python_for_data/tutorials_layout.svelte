<!-- src/routes/tutorials/TutorialLayout.svelte -->
<script>
  import { Link } from "svelte-routing";
</script>

<div class="tutorial-container">
  <div class="tutorial-content">
    <slot></slot>
  </div>
</div>

<style>
  .tutorial-container {
    display: flex;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }

  .tutorial-nav {
    width: 200px;
    padding-right: 20px;
  }

  .tutorial-nav :global(a) {
    display: block;
    margin-bottom: 10px;
    color: #333;
    text-decoration: none;
  }

  .tutorial-nav :global(a:hover) {
    text-decoration: underline;
  }

  .tutorial-content {
    flex-grow: 1;
  }

  /* Add any other shared styles for tutorials here */
</style>
