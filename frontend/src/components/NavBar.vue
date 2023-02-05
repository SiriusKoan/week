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
    <div v-if="authed" id="logout-btn" @click="logout">Logout</div>
  </nav>
</template>

<script>
import { getAuth } from "firebase/auth";
import { useRouter } from "vue-router";
export default {
  name: "NavBar",
  data() {
    return {
      authed: false,
      auth: getAuth(),
      router: useRouter(),
    };
  },
  created() {
    this.auth.onAuthStateChanged((user) => {
      if (user) {
        this.authed = true;
      } else {
        this.authed = false;
      }
    });
  },
  methods: {
      logout() {
          this.auth.signOut();
          this.router.push("/");
      },
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

nav a:hover {
    text-decoration: underline;
}

.activate {
  color: #cf6e6e;
}

#logout-btn {
    color: #cccc6e;
    cursor: pointer;
}

#logout-btn:hover {
    text-decoration: underline;
}
</style>
