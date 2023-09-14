
<template>
  <label
      class="block text-gray-700 font-bold mt-2 text-lg"
      :for="name">
    {{ description }}:
  </label>
  <input
      :type="isSecret ? 'password' : 'text'"
      :id="name"
      :name="name"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      class="rounded-lg px-4 py-3 mt-3 focus:outline-none bg-gray-300 w-full"
  />
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