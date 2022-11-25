<template>
  <div class="day">
      <div v-if="!weekday">
          <div class="weekday"></div>
          <TimeLabel v-for="i in 18" :time="i + 5" />
      </div>
      <div v-else>
          <div class="weekday">{{ weekday }}</div>
          <Cell v-for="i in 18" :time="i + 5" />
          <Schedule :time_start="360" :time_end="600" />
      </div>
  </div>
</template>

<script>
import Cell from "./Cell.vue";
import TimeLabel from "./TimeLabel.vue";
import Schedule from "./Schedule.vue";
export default {
  name: "Day",
  components: {
    Cell,
    TimeLabel,
    Schedule,
  },
  props: {
      weekday: String,
  },
};
</script>

<style>
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
    background-color: #AD3333;
}
#Mon .schedule {
    background-color: #3246F9;
}
#Tue .schedule {
    background-color: #46CE6C;
}
#Wed .schedule {
    background-color: #909C00;
}
#Thu .schedule {
    background-color: #7B2AA1;
}
#Fri .schedule {
    background-color: #008656;
}
#Sat .schedule {
    background-color: #FF7A00;
}
</style>
