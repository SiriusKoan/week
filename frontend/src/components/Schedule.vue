<template>
  <div
    class="schedule"
    :style="{
      height: (time_end - time_start) * 0.75 + 'px',
      top: (time_start - 360) * 0.75 + 23 + 'px',
    }"
  >
    <div>{{ content }}</div>
    <div>@ {{ location }}</div>
  </div>
</template>

<script>
export default {
  name: "Schedule",
  props: {
    time_start: Number,
    time_end: Number,
    content: String,
    location: String,
  },
};
</script>
