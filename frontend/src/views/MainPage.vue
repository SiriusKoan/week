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

<script>
import Day from "../components/Day.vue";
export default {
  name: "MainPage",
  components: {
    Day,
  },
};
</script>
