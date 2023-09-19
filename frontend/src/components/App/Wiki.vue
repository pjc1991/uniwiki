<script>
import {defineComponent} from 'vue'
import {getCookie} from '../../utils.js'
import BasicButton from "../BasicButton.vue";
import WikiSideMenu from "./Wiki/WikiSideMenu.vue";
import WikiCurrentPage from "./Wiki/WikiCurrentPage.vue";
import MessageWindow from "../MessageWindow.vue";
import WikiWindow from "./Wiki/WikiWindow.vue";
import UniverseList from "./Wiki/UniverseList.vue";

export default defineComponent({
  components: {UniverseList, WikiWindow, MessageWindow, WikiCurrentPage, WikiSideMenu, BasicButton},
  props: [
    'user',
  ],
  name: "Wiki",
  data() {
    return {
      universeSelected: false,
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
  <div class="wiki-main h-full flex flex-col">
    <UniverseList
        v-if="!universeSelected"
        :user="user"
        class="universe-list-component">
    </UniverseList>
    <WikiWindow
        v-if="universeSelected"
        :user="user"
        class="wiki-window-component">
    </WikiWindow>
  </div>

</template>

<style scoped>

</style>