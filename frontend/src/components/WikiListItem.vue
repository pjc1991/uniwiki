<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "WikiListItem",
  props: [
    'item'
  ]
})
</script>

<template>
  <div
      class="flex justify-between items-center bg-gray-200 rounded p-2 my-2 cursor-pointer hover:bg-gray-300 transition ease-in-out duration-150">
    <p
        class="text-gray-700 truncate hover:underline font-serif">
      {{ item.description }}
    </p>
  </div>
</template>

<style scoped>

</style>