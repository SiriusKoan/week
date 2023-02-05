<template>
  <main>
    <h1>Create an Account</h1>
    <p><input type="text" placeholder="Email" v-model="email" /></p>
    <p><input type="password" placeholder="Password" v-model="password" /></p>
    <p><button @click="register">Submit</button></p>
  </main>
</template>

<script>
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { useRouter } from "vue-router";
export default {
  name: "RegisterPage",
  data() {
    return {
      email: "",
      password: "",
      auth: getAuth(),
      router: useRouter(),
    };
  },
  methods: {
    register() {
      createUserWithEmailAndPassword(this.auth, this.email, this.password)
        .then((data) => {
          this.$emit("notify", "success", "Successfully registered!");
          this.router.push("/");
        })
        .catch((error) => {
          this.$emit("notify", "error", error.message);
        });
    },
  },
};
</script>
