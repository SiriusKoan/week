<template>
  <h1>Login to Your Account</h1>
  <p><input type="text" placeholder="Email" v-model="email" /></p>
  <p><input type="password" placeholder="Password" v-model="password" /></p>
  <p v-if="errMsg">{{ errMsg }}</p>
  <p><button @click="signIn">Submit</button></p>
</template>

<script>
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import { useRouter } from "vue-router";
export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
      router: useRouter(),
      auth: getAuth(),
    };
  },
  methods: {
    signIn() {
      signInWithEmailAndPassword(this.auth, this.email, this.password)
        .then((data) => {
          this.$emit("notify", "success", "Successfully logged in!");
          this.router.push("/");
        })
        .catch((error) => {
          switch (error.code) {
            case "auth/invalid-email":
              this.$emit("notify", "error", "Invalid email.");
              break;
            case "auth/user-not-found":
              this.$emit(
                "notify",
                "error",
                "No account with that email was found"
              );
              break;
            case "auth/wrong-password":
              this.$emit("notify", "error", "Incorrect password");
              break;
            default:
              this.$emit("notify", "error", "Email or password was incorrect");
              break;
          }
        });
    },
  },
};
</script>
