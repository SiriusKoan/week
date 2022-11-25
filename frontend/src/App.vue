<script lang="ts">
import axios from "axios";
import Day from "./components/Day.vue";
export default {
  data() {
    return {};
  },
  components: {
    Day,
  },
};
</script>

<template>
  <main>
    <Day id="time-label" />
    <Day id="Sun" weekday="Sun" />
    <Day id="Mon" weekday="Mon" />
    <Day id="Tue" weekday="Tue" />
    <Day id="Wed" weekday="Wed" />
    <Day id="Thu" weekday="Thu" />
    <Day id="Fri" weekday="Fri" />
    <Day id="Sat" weekday="Sat" />
  </main>
</template>

<style>
@import "assets/base.css";
@import "assets/time.css";

body {
  margin: 0;
  color: var(--text-color);
  background-color: var(--bg-color);
}

main {
  position: absolute;
  margin: auto 0;
  width: 100%;
  display: flex;
  justify-content: center;
}
</style>
