<template>
  <div class="container" v-if="status">
    <div :class="status" class="notification">
      {{ msg }}
    </div>
  </div>
</template>

<script>
export default {
  name: "FloatingNotification",
  props: {
    status: String,
    msg: String,
  },
};
</script>

<style scoped>
.container {
  display: flex;
  position: absolute;
  justify-content: center;
  width: 100%;
  z-index: 100;
  margin: 0;
}

.notification {
  color: var(--text-color);
  -webkit-box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.5);
  -moz-box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.5);
  box-shadow: 5px 5px 5px 0px rgba(0, 0, 0, 0.5);
  width: 50vw;
  padding: 10px;
  margin: 3px auto;
  text-align: center;
}

.error {
  background-color: #f44336;
}

.warning {
  background-color: #ffeb3b;
}

.success {
  background-color: #4caf50;
}
</style>
