<script>
import {defineComponent} from 'vue'

export default defineComponent({
  props: [
    'message'
  ],
  name: "MessageWindow"
})
</script>

<template>
  <div class="flex flex-col items-start mt-5">
    <p class="text-gray-700 text-base mb-4 truncate hover:underline font-serif" v-text="message"></p>
  </div>
</template>

<style scoped>

</style>