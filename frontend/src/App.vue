<script lang="ts">
import axios from "axios";
import Day from "./components/Day.vue";
import TimeLabel from "./components/TimeLabel.vue";
export default {
  data() {
    return {};
  },
  components: {
    Day,
    TimeLabel,
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
@import "assets/time.css";

body {
    color: white;
    background-color: #353839;
}

main {
    display: flex;
    justify-content: center;
}
</style>
