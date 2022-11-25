<template>
  <div
    class="schedule"
    :style="{
      height: (time_end - time_start) * 0.75 + 'px',
      top: (time_start - 360) * 0.75 + 25 + 'px',
    }"
  >
    test
  </div>
</template>

<script>
export default {
  name: "Schedule",
  props: {
    time_start: Number,
    time_end: Number,
  },
};
</script>
