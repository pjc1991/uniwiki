<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "WikiCurrentPage",
  props: [
      'page_id'
  ],
  methods: {
    getWikiContent(page_id) {
    }
  }
})
</script>

<template>
  <div class="flex flex-col w-3/4">
    <textarea
        class="w-full h-full border border-gray-200 rounded-lg px-4 py-2 bg-gray-200 resize-none focus:outline-none font-serif overscroll-auto"
    >This is wiki contents.</textarea>
  </div>
</template>

<style scoped>

</style>