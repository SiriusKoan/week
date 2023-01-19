<template>
  <span v-if="isLoggedIn">
    <button @click="signOut">Logout</button>
  </span>
</template>

<script setup>
import { ref } from "vue";
import { getAuth } from "firebase/auth";
import { useRouter } from "vue-router";
const router = useRouter();
const isLoggedIn = ref(true);
const auth = getAuth();
auth.onAuthStateChanged(function (user) {
  if (user) {
    isLoggedIn.value = true;
  } else {
    isLoggedIn.value = false;
  }
});
const signOut = () => {
  auth.signOut();
  router.push("/");
};
</script>
