<template>
  <main>
    <Day id="time-label" />
    <Day
      id="Sun"
      weekday="Sun"
      :schedule="[
        [480, 720, 'test 1'],
        [1000, 1200, 'test 2'],
      ]"
    />
    <Day id="Mon" weekday="Mon" :schedule="[[360, 420, 'event a']]" />
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
  name: "TimetablePage",
  components: {
    Day,
  },
  props: {
      email: String,
      name: String,
  },
  created() {
      console.log(this.email, this.name);
  }
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
