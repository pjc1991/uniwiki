<script>
import {defineComponent} from 'vue'

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
      localStorage.removeItem('jwt')
      this.$emit('get-jwt', '')
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