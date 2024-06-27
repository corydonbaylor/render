<script>
  let message = "";

  async function fetchMessage() {
    const response = await fetch("/api/hello");
    message = await response.text();
  }
</script>

<h1>Welcome to the Home Page</h1>
<button on:click={fetchMessage}>Get Message</button>
{#if message}
  <p>{message}</p>
{/if}
