
<template>
  <label :for="name">{{ description }}:</label><br>
  <input :type="isSecret ? 'password' : 'text'" :id="name" :name="name" /><br>
</template>

<script>


export default {
  props: [
      'name'
      , 'description'
      , 'isSecret'
  ],
  name: 'basicForm',
  components: {
  },
}

</script>

<style scoped>

</style>