<script>
import {defineComponent} from 'vue'
import {getCookie} from '../utils'

export default defineComponent({
  props: [
    'user'
  ],
  name: "Wiki",
  data () {
    return {
    }
  },
  methods: {
    signOff() {
      const csrftoken = getCookie('csrftoken')
      fetch('/api/common/auth/logout/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({})
      }).then(response => {
        if (response.status !== 200) {
          throw new Error('logout failed')
        }
      }).then(data => {
        this.$emit('get-logged-in', '')
      }).catch((error) => {
        console.log(error)
      });

    }
  },
})
</script>

<template>
<div class="wiki-main">
  yes, i am logged in as {{ user.username }}
  <button
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      @click="signOff">
    Sign off
  </button>
</div>
</template>

<style scoped>

</style>