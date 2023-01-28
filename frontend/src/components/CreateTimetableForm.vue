<template>
    <form v-on:click.prevent="">
        <div>
            <input type="text" name="name" placeholder="Name" v-model="name" required>
        </div>
        <div>
            <input type="text" name="location" placeholder="Location" v-model="location" required>
        </div>
        <div>
            <input type="number" min="0" max="6" name="weekday" placeholder="Weekday" v-model="weekday" required>
        </div>
        <div>
            <span>Start Time</span>
            <input type="time" name="start_time" v-model="start_time" required>
        </div>
        <div>
            <span>End Time</span>
            <input type="time" name="end_time" v-model="end_time" required>
        </div>
        <button @click="sendAdd">Add</button>
    </form>
</template>

<script>
export default {
    name: "CreateTimetableForm",
    data() {
        return {
            name: "",
            location: "",
            weekday: 0,
            start_time: "10:00",
            end_time: "10:00",
        }
    },
    methods: {
        sendAdd() {
            this.$emit("add", this.name, this.location, this.weekday, this.start_time, this.end_time);
        }
    },
};
</script>

<style scoped>
form {
    margin: 5px;
}

span {
    margin: 3px;
}

input {
    min-width: 100px;
}
</style>
