<script>
  import { Link } from "svelte-routing";
  let isMenuOpen = false;

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }
</script>

<nav>
  <div class="nav-container">
    <div class="logo">
      <Link to="/">YourLogo</Link>
    </div>
    <div class="menu-icon" on:click={toggleMenu}>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>
    <ul class:active={isMenuOpen}>
      <li><Link to="/" on:click={toggleMenu}>Home</Link></li>
      <li><Link to="/about" on:click={toggleMenu}>About</Link></li>
      <!-- Add more navigation items here -->
    </ul>
  </div>
</nav>

<style>
  nav {
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
  }

  .nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
  }

  .logo a {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
    text-decoration: none;
  }

  ul {
    display: flex;
    list-style-type: none;
    margin: 0;
    padding: 0;
  }

  li {
    margin-left: 2rem;
  }

  a {
    color: #333;
    text-decoration: none;
    font-size: 1rem;
    transition: color 0.3s ease;
  }

  a:hover {
    color: #007bff;
  }

  .menu-icon {
    display: none;
    cursor: pointer;
  }

  .bar {
    width: 25px;
    height: 3px;
    background-color: #333;
    margin: 5px 0;
    transition: 0.4s;
  }

  @media (max-width: 768px) {
    .menu-icon {
      display: block;
    }

    ul {
      display: none;
      flex-direction: column;
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      background-color: #ffffff;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    ul.active {
      display: flex;
    }

    li {
      margin: 0;
      text-align: center;
    }

    a {
      display: block;
      padding: 1rem;
    }
  }
</style>
