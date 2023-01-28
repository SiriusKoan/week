<template>
  <main>
    <Day id="time-label" />
    <Day id="Sun" weekday="Sun" :schedule="schedule[0]" />
    <Day id="Mon" weekday="Mon" :schedule="schedule[1]" />
    <Day id="Tue" weekday="Tue" :schedule="schedule[2]" />
    <Day id="Wed" weekday="Wed" :schedule="schedule[3]" />
    <Day id="Thu" weekday="Thu" :schedule="schedule[4]" />
    <Day id="Fri" weekday="Fri" :schedule="schedule[5]" />
    <Day id="Sat" weekday="Sat" :schedule="schedule[6]" />
  </main>
</template>

<script>
import Day from "../components/Day.vue";
import { getAuth } from "firebase/auth";
import axios from "axios";
export default {
  name: "TimetablePage",
  components: {
    Day,
  },
  props: {
    email: String,
    name: String,
  },
  data() {
    return {
      schedule: [...Array(7)].map((x) => []),
    };
  },
  created() {
    const auth = getAuth();
    let token = "";
    auth.onAuthStateChanged((user) => {
      token = `${user.accessToken}`;
      let headers = { Authorization: `Bearer ${token}` };
      axios
        .get(`/api/${this.email}/${this.name}`, { headers: headers })
        .then((res) => {
          let data = res.data["timetable"];
          for (let i = 0; i < data.length; i++) {
            let d = data[i];
            this.schedule[d["day"]].push([
              d["start_time"],
              d["end_time"],
              d["name"],
              d["location"],
            ]);
          }
        });
    });
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
