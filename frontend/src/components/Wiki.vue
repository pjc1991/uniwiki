<script>
import {defineComponent} from 'vue'
import {getCookie} from '../utils'
import BasicButton from "./BasicButton.vue";
import WikiSideMenu from "./WikiSideMenu.vue";
import WikiCurrentPage from "./WikiCurrentPage.vue";

export default defineComponent({
  components: {WikiCurrentPage, WikiSideMenu, BasicButton},
  props: [
    'user'
  ],
  name: "Wiki",
  data() {
    return {}
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
<div class="wiki-main h-full flex flex-col">
  <div class="wiki-main-content flex flex-grow">
    <WikiSideMenu class="wiki-side-menu-component"></WikiSideMenu>
    <WikiCurrentPage class="wiki-current-page-component"></WikiCurrentPage>
  </div>

  <div class="flex flex-col items-start mt-5">
    <p class="text-gray-700 text-base mb-4 truncate hover:underline font-serif">
      Yes I'm logged in as {{ user.email }}
    </p>
  </div>

  <div class="wiki-main-button flex justify-end mt-auto">
    <BasicButton
      @click="signOff"
      :description="'Sign off'"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
    >
    </BasicButton>
  </div>
</div>

</template>

<style scoped>

</style>