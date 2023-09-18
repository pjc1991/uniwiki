<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "WikiCurrentPage",
  props: [
      'page_id'
  ],
  data() {
    return {
      wiki_content: ''
    }
  },
  methods: {
    getWikiContent(page_id) {
    },
    inputHandler() {
      // get the content of the textarea
      const content = this.wiki_content

      // the first line is always the title and start with #
      // get the data with the first line
      const name = content.split('\n')[0].replace('#', '').trim()
      const description = content.replace(title, '').trim()

      // send the data to the backend
      const csrftoken = getCookie('csrftoken')
      fetch('/api/wiki/wikidocs/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
          name: name,
          description: description
        })
      }).then(response => {
        if (response.status !== 200) {
          throw new Error('save failed')
        }
      }).then(data => {
        console.log(data)
      }).catch((error) => {
        console.log(error)
      });
    }
  }
})
</script>

<template>
  <div class="flex flex-col w-3/4">
    <textarea name="wiki-content" id="wiki-content" cols="30" rows="10" v-model="wiki_content" @input="inputHandler"
        class="w-full h-full border border-gray-200 rounded-lg px-4 py-2 bg-gray-200 resize-none focus:outline-none font-serif overscroll-auto"
    ># New Page</textarea>
  </div>
</template>

<style scoped>

</style>