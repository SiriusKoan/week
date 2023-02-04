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
    };
  },
  created() {
    const auth = getAuth();
    let token = "";
    auth.onAuthStateChanged((user) => {
      token = `${user.accessToken}`;
      let headers = { Authorization: `Bearer ${token}` };
      axios
        .get(`/api/${this.email}`, { headers: headers })
        .then((res) => {
            console.log(res);
          this.timetables = res.data;
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
