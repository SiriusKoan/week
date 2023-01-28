<script lang="ts">
import NavBar from "./components/NavBar.vue";
export default {
  data() {
    return {};
  },
  components: {
    NavBar,
  },
};
</script>

<template>
  <NavBar />
  <router-view />
</template>

<style>
@import "assets/base.css";
@import "assets/time.css";
</style>
