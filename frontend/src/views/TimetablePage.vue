<template>
  <main>
    <h1>{{ name }}</h1>
    <div class="container">
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
      auth: getAuth(),
    };
  },
  created() {
    let token = "";
    this.auth.onAuthStateChanged((user) => {
      if (!user) {
        this.$emit("notify", "error", "You need to login first.");
        return;
      }
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
        })
        .catch((error) => {
          let status_code = error.response.status;
          if (status_code == 401) {
            this.$emit("notify", "error", "You need to login first.");
          } else if (status_code == 403) {
            this.$emit(
              "notify",
              "error",
              "You do not have permission to view this timetable."
            );
          } else if (status_code == 404) {
            this.$emit("notify", "error", "The timetable cannot be found.");
          }
        });
    });
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}

.container {
  position: absolute;
  margin: auto 0;
  width: 100%;
  display: flex;
  justify-content: center;
}
</style>
