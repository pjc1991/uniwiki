<script>
import {defineComponent} from 'vue'
import {getCookie} from '../../../utils.js'

export default defineComponent({
  name: "WikiCurrentPage",
  props: [
      'page_id'
  ],
  created() {

  },
  mounted() {

    if(this.wiki_content === '') {
      this.getTheLatestWikiPage()
    }

    window.addEventListener('keydown', this.enterListener)
  }
  , unmounted() {
    // remove the event listener
    window.removeEventListener('keydown', this.enterListener)
  },
  data() {
    return {
      wiki_content: ''
    }
  },
  methods: {
    getTheLatestWikiPage() {
      fetch('/api/wiki/latest/')
          .then(response => response.json())
          .then(data => {
            this.wiki_content = '#' + data.name + '\n' + data.description
          })
    },
    enterListener(event) {
      // the first line is always the title and start with #. if # is deleted, add it back
      if (this.wiki_content.charAt(0) !== '#') {
        this.wiki_content = '# ' + this.wiki_content
      }

      // check if it is enter key
      if (event.key === 'Enter') {
        this.inputHandler()
      }
    },
    inputHandler() {
      // get the content of the textarea
      this.wiki_content = this.wiki_content
      const content = this.wiki_content

      // the first line is always the title and start with #
      const name = getTheFirstLine(content)
      const description = getTheDescription(content)

      // if the name or description is empty, do nothing
      if (name === '' || description === '') {
        return
      }

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

function getTheFirstLine(content) {
      return content.split('\n')[0].substring(1)
}
function getTheDescription(content) {
      return content.substring(content.split('\n')[0].length + 1)
}


</script>

<template>
  <div class="flex flex-col w-full">
    <textarea name="wiki-content" id="wiki-content" cols="30" rows="10" v-model="wiki_content"
        class="w-full h-full border border-gray-200 rounded-lg px-4 py-2 bg-gray-200 resize-none focus:outline-none font-serif overscroll-auto"
    ># New Page</textarea>
  </div>
</template>

<style scoped>

</style>