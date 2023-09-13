
<template>
  <label :for="name">{{ description }}:</label><br>
  <input
      :type="isSecret ? 'password' : 'text'"
      :id="name"
      :name="name"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
  />
  <br>
</template>

<script>


export default {
  props: [
      'name'
      , 'description'
      , 'isSecret'
      , 'modelValue'
  ],
  name: 'basicForm',
  components: {
  },
}

</script>

<style scoped>

</style>