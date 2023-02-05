<script lang="ts">
import NavBar from "./components/NavBar.vue";
import CopyrightFooter from "./components/CopyrightFooter.vue";
import FloatingNotification from "./components/FloatingNotification.vue";
export default {
  data() {
    return {
      notify_status: "",
      notify_msg: "",
    };
  },
  components: {
    NavBar,
    CopyrightFooter,
    FloatingNotification,
  },
  methods: {
    notify(notify_status, notify_msg) {
      this.notify_status = notify_status;
      this.notify_msg = notify_msg;
    },
  },
  watch: {
    $route(to, from) {
      this.notify_status = "";
      this.notify_msg = "";
    },
  },
};
</script>

<template>
  <NavBar />
  <FloatingNotification :status="notify_status" :msg="notify_msg" />
  <router-view @notify="notify" />
  <CopyrightFooter />
</template>

<style>
@import "assets/base.css";
@import "assets/time.css";

body {
  min-height: 100vh;
}
</style>
