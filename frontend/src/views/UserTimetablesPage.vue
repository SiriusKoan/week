<template>
  <main>
    <h1>Timetable for {{ email }}</h1>
    <div v-for="timetable in timetables">
      <a :href="'/' + email + '/' + timetable">{{ timetable }}</a>
    </div>
  </main>
</template>

<script>
import { getAuth } from "firebase/auth";
import axios from "axios";
export default {
  name: "UserTimetablesPage",
  props: {
    email: String,
  },
  data() {
    return {
      timetables: [],
      auth: getAuth(),
    };
  },
  created() {
    let token = "";
    this.auth.onAuthStateChanged((user) => {
      token = `${user.accessToken}`;
      let headers = { Authorization: `Bearer ${token}` };
      axios
        .get(`/api/${this.email}`, { headers: headers })
        .then((res) => {
          this.timetables = res.data;
        })
        .catch((error) => {
          let status_code = error.response.status;
          if (status_code == 401) {
            this.$emit("notify", "error", "You need to login first.");
          } else if (status_code == 403) {
            this.$emit(
              "notify",
              "error",
              "You do not have permission to view others' timetables."
            );
          }
        });
    });
  },
};
</script>

<style scoped>
main {
  width: 50vw;
  margin: 0 auto;
}

a {
  text-decoration: none;
  color: var(--text-color);
}

a:hover {
  text-decoration: underline;
}

h1 {
  text-align: center;
}
</style>
