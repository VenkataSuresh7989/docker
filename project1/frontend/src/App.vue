<template>
  <div id="app">
    <UserManagement />
  </div>
</template>

<script>
import UserManagement from './components/UserManagement.vue'

export default {
  components: { UserManagement }
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f7f6;
  margin: 0;
  padding: 20px;
}
</style>