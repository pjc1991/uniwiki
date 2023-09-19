<script>
import {defineComponent} from 'vue'
import WikiCurrentPage from "./WikiCurrentPage.vue";
import MessageWindow from "../../MessageWindow.vue";
import BasicButton from "../../BasicButton.vue";

export default defineComponent({
  name: "WikiWindow",
  components: {BasicButton, MessageWindow, WikiCurrentPage}
})
</script>

<template>
  <div class="wiki-window-component">
    <div class="wiki-main-content flex flex-grow">
      <WikiCurrentPage class="wiki-current-page-component"></WikiCurrentPage>
    </div>

    <div class="flex flex-col items-start mt-5">
      <p class="text-gray-700 text-base mb-4 truncate hover:underline font-serif">
        <MessageWindow :message="`Yes I\'m logged in as ${user.email}`"></MessageWindow>
      </p>
    </div>
    <div class="wiki-main-button flex justify-end mt-auto">
      <BasicButton
          @click="signOff"
          :description="'Sign off'"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
      </BasicButton>
    </div>
  </div>
</template>

<style scoped>

</style>