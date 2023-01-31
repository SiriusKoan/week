<template>
  <main>
    <input type="text" v-model="name" placeholder="Timetable Name" required />
    <CreateTimetableForm @add="addTimeCell" />
    <button @click="sendCreate">Create</button>
    <div id="timetable-container">
      <Day id="time-label" />
      <Day id="Sun" weekday="Sun" :schedule="schedule[0]" />
      <Day id="Mon" weekday="Mon" :schedule="schedule[1]" />
      <Day id="Tue" weekday="Tue" :schedule="schedule[2]" />
      <Day id="Wed" weekday="Wed" :schedule="schedule[3]" />
      <Day id="Thu" weekday="Thu" :schedule="schedule[4]" />
      <Day id="Fri" weekday="Fri" :schedule="schedule[5]" />
      <Day id="Sat" weekday="Sat" :schedule="schedule[6]" />
    </div>
  </main>
</template>

<script>
import Day from "../components/Day.vue";
import CreateTimetableForm from "../components/CreateTimetableForm.vue";
import { toRaw } from "vue";
import axios from "axios";
import { getAuth } from "firebase/auth";
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
      schedule: [...Array(7)].map((x) => []),
    };
  },
  methods: {
    addTimeCell(name, location, weekday, start_time, end_time) {
      start_time = start_time.split(":");
      let start_time_num =
        parseInt(start_time[0]) * 60 + parseInt(start_time[1]);
      end_time = end_time.split(":");
      let end_time_num = parseInt(end_time[0]) * 60 + parseInt(end_time[1]);
      this.timetable.push({
        name: name,
        location: location,
        day: weekday,
        start_time: start_time_num,
        end_time: end_time_num,
      });
      this.schedule[weekday].push([
        start_time_num,
        end_time_num,
        name,
        location,
      ]);
    },
    sendCreate() {
      const auth = getAuth();
      let token = "";
      let data = { name: this.name, timetable: toRaw(this.timetable) };
      auth.onAuthStateChanged((user) => {
        token = `${user.accessToken}`;
        let headers = { Authorization: `Bearer ${token}` };
        axios.post("/api/create", data, { headers: headers }).then((res) => {
          console.log(res);
        });
      });
    },
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
