<script>
  let appInfo = "";

  async function fetchAppInfo() {
    const response = await fetch("/api/about");
    appInfo = await response.json();
  }
</script>

<h1>About This App</h1>
<button on:click={fetchAppInfo}>Get App Info</button>
{#if appInfo}
  <p>Frontend: {appInfo.frontend}</p>
  <p>Backend: {appInfo.backend}</p>
{/if}
