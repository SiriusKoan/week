<template>
  <main>
      <input type="text" v-model="name" placeholder="Timetable Name" required>
      <CreateTimetableForm @add="addTimeCell" />
      <button @click="sendCreate">Create</button>
      <div id="timetable-container">
          <Day id="time-label" />
          <Day id="Sun" weekday="Sun" />
          <Day id="Mon" weekday="Mon" />
          <Day id="Tue" weekday="Tue" />
          <Day id="Wed" weekday="Wed" />
          <Day id="Thu" weekday="Thu" />
          <Day id="Fri" weekday="Fri" />
          <Day id="Sat" weekday="Sat" />
      </div>
  </main>
</template>

<script>
import Day from "../components/Day.vue";
import CreateTimetableForm from "../components/CreateTimetableForm.vue";
export default {
    name: "CreateTimetablePage",
    components: {
        Day,
        CreateTimetableForm,
    },
    data() {
        return {
            name: "",
            timetable: [],
        }
    },
    methods: {
        addTimeCell(name, location, weekday, start_time, end_time) {
            start_time = start_time.split(":");
            let start_time_num = parseInt(start_time[0]) * 60 + parseInt(start_time[1]);
            end_time = end_time.split(":");
            let end_time_num = parseInt(end_time[0]) * 60 + parseInt(end_time[1]);
            this.timetable.push({"name": name, "location": location, "weekday": weekday, "start_time": start_time_num, "end_time": end_time_num});
        },
        sendCreate() {
            console.log(this.name, this.timetable);
        }
    },
};
</script>

<style scoped>
#timetable-container {
    position: absolute;
    margin: auto 0;
    width: 100%;
    display: flex;
    justify-content: center;
}
</style>
