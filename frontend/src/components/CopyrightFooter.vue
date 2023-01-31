<template>
  <footer>
    <div>
      © <a href="https://github.com/SiriusKoan/week" target="_blank">Week</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "CopyrightFooter",
};
</script>

<style scoped>
footer {
  text-align: center;
  position: absolute;
  bottom: 10px;
}

a {
  color: var(--text-color);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>
