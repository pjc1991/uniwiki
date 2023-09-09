<template>
<html>
<form action="">
  <basicForm :name="'username'" :description="'Username'"></basicForm>
  <basicForm :name="'password'" :description="'Password'" :is-secret="true"></basicForm>
</form>
</html>
</template>

<script>
import basicForm from './basicForm.vue'

export default {
  name: 'Login',
  components: {
    basicForm
  }
}

</script>

<style scoped>

</style>