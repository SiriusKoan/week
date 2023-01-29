<template>
  <nav>
    <router-link to="/" active-class="activate">Home</router-link>
    <router-link to="/about" active-class="activate">About</router-link>
    <router-link v-if="!authed" to="/login" active-class="activate">
      Login
    </router-link>
    <router-link v-if="!authed" to="/register" active-class="activate">
      Register
    </router-link>
    <router-link v-if="authed" to="/create" active-class="activate">
      Create
    </router-link>
    <router-link v-if="authed" to="/logout" active-class="activate">
      Logout
    </router-link>
  </nav>
</template>

<script>
import { getAuth } from "firebase/auth";
export default {
  name: "NavBar",
  data() {
    return {
      authed: false,
    };
  },
  created() {
    const auth = getAuth();
    auth.onAuthStateChanged((user) => {
      if (user) {
        this.authed = true;
      } else {
        this.authed = false;
      }
    });
  },
};
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-around;
  background-color: #464857;
  padding: 10px;
}

nav a {
  color: #cccc6e;
  text-decoration: none;
}

.activate {
  color: #cf6e6e;
}
</style>
