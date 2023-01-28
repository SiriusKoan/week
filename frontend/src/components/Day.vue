<template>
  <div class="day">
    <div v-if="!weekday">
      <div class="weekday"></div>
      <TimeLabel v-for="i in 18" v-bind:time="i + 5" v-bind:key="i + 5" />
    </div>
    <div v-else>
      <div class="weekday">{{ weekday }}</div>
      <TimeCell v-for="i in 18" v-bind:time="i + 5" v-bind:key="i + 5" />
      <Schedule
        v-for="(sche, i) in schedule"
        :time_start="sche[0]"
        :time_end="sche[1]"
        :content="sche[2]"
        :location="sche[3]"
      />
    </div>
  </div>
</template>

<script>
import TimeCell from "./TimeCell.vue";
import TimeLabel from "./TimeLabel.vue";
import Schedule from "./Schedule.vue";
export default {
  name: "Day",
  components: {
    TimeCell,
    TimeLabel,
    Schedule,
  },
  props: {
    weekday: String,
    schedule: Array,
  },
};
</script>

<style scoped>
.day {
  display: flex;
  flex-direction: column;
  margin: 0;
}

.weekday {
  text-align: center;
  padding: 2px 0;
  height: 20px;
}

#Sun .schedule {
  background-color: var(--sun-color);
}
#Mon .schedule {
  background-color: var(--mon-color);
}
#Tue .schedule {
  background-color: var(--tue-color);
}
#Wed .schedule {
  background-color: var(--wed-color);
}
#Thu .schedule {
  background-color: var(--thu-color);
}
#Fri .schedule {
  background-color: var(--fri-color);
}
#Sat .schedule {
  background-color: var(--sat-color);
}
</style>
