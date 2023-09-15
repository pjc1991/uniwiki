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
  <div class="flex w-full">
    <div class="justify-between items-center bg-gray-200 rounded p-2 my-2">
      <p class="text-gray-700 truncate hover:underline">
        {{ item.description }}
      </p>
    </div>
  </div>
</template>

<style scoped>

</style>