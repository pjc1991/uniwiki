<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Signup",
  data () {
    return {
    }
  },
  methods: {
    turnoffSignup() {
      this.$emit('set-signup', false)
    }
  },
})
</script>

<template>
  <div>
  <p class="text-gray-700 text-base">
    this is signup.
  </p>
    <button
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        @click="turnoffSignup">
      Go back to login
    </button>
  </div>
</template>

<style scoped>

</style>