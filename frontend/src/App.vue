<script lang="ts">
import NavBar from "./components/NavBar.vue";
import CopyrightFooter from "./components/CopyrightFooter.vue";
export default {
  data() {
    return {};
  },
  components: {
    NavBar,
    CopyrightFooter,
  },
};
</script>

<template>
  <NavBar />
  <router-view />
  <CopyrightFooter />
</template>

<style>
@import "assets/base.css";
@import "assets/time.css";

body {
  min-height: 100vh;
}
</style>
