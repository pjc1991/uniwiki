<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "BasicButton",
  props: [
      'description'
  ]
})
</script>

<template>
<div>
  <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    <slot>{{ description }}</slot>
  </button>
</div>
</template>

<style scoped>

</style>