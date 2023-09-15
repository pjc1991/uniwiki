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
        <WikiSideMenu></WikiSideMenu>
        <WikiCurrentPage></WikiCurrentPage>
      </div>
      <div class="justify-start mt-5">
        <p class="text-gray-700 text-base mb-4 truncate hover:underline font-serif">
          Yes I'm logged in as {{ user.email }}
        </p>
      </div>
      <div class="wiki-main-button flex justify-end">
        <BasicButton @click="signOff" :description="'Sign off'"></BasicButton>
      </div>
    </div>
</template>

<style scoped>

</style>