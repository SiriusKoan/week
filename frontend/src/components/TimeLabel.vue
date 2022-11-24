<template>
    <div class="time-label">
        {{ time }}
    </div>
</template>

<script>
export default {
    name: "TimeLabel",
    props: {
        time: Number,
    },
}
</script>

<style>
.time-label {
    text-align: center;
}
</style>
