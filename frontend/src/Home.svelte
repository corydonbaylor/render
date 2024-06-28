<script>
  let message = "";

  async function fetchMessage() {
    const response = await fetch("/api/hello");
    message = await response.text();
  }
</script>

<h1>Welcome to the Dumb Page</h1>
<button on:click={fetchMessage}>Get Message</button>
{#if message}
  <p>{message}</p>
{/if}
<img src="https://corydon1.gitlab.io/cdn/hotel.jpeg" />
