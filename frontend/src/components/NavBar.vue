<template>
  <nav>
    <router-link to="/" class="nav-item" active-class="activate">Home</router-link>
    <router-link to="/about" class="nav-item" active-class="activate">About</router-link>
    <router-link to="/login" class="nav-item" active-class="activate">Login</router-link>
    <router-link to="/register" class="nav-item" active-class="activate">Register</router-link>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-around;
  background-color: #464857;
  padding: 10px;
}

.nav-item {
  color: #CCCC6E;
  text-decoration: none;
}

.activate {
  color: #CF6E6E;
}
</style>