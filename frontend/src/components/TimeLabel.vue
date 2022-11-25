<template>
  <div class="time-label">{{ time }}:00</div>
</template>

<script>
export default {
  name: "TimeLabel",
  props: {
    time: Number,
  },
};
</script>
