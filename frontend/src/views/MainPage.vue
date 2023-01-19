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

<style scoped>
main {
  position: absolute;
  margin: auto 0;
  width: 100%;
  display: flex;
  justify-content: center;
}
</style>
