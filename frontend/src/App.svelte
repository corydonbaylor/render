<script>
  let message = '';

  async function fetchMessage() {
    const response = await fetch('/api/hello');
    message = await response.text();
  }
</script>

<main>
  <h1>Svelte + Flask App</h1>
  <button on:click={fetchMessage}>Get Message</button>
  {#if message}
    <p>{message}</p>
  {/if}
</main>
