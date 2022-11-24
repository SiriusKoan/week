<template>
  <div class="day">
      <div v-if="!weekday">
          <div class="weekday"></div>
          <TimeLabel v-for="i in 18" :time="i + 5" />
      </div>
      <div v-else>
          <div class="weekday">{{ weekday }}</div>
          <Cell v-for="i in 18" :time="i + 5" />
      </div>
  </div>
</template>

<script>
import Cell from "./Cell.vue";
import TimeLabel from "./TimeLabel.vue";
export default {
  name: "Day",
  components: {
    Cell,
    TimeLabel,
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

#Sun .cell {
    background-color: #AD3333;
}
#Mon .cell {
    background-color: #3246F9;
}
#Tue .cell {
    background-color: #46CE6C;
}
#Wed .cell {
    background-color: #909C00;
}
#Thu .cell {
    background-color: #7B2AA1;
}
#Fri .cell {
    background-color: #008656;
}
#Sat .cell {
    background-color: #FF7A00;
}
</style>
