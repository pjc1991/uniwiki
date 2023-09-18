<script>
import {defineComponent} from 'vue'
import WikiListItem from "./WikiListItem.vue";
import BasicButton from "./BasicButton.vue";

export default defineComponent({
  name: "WikiSideMenu",
  components: {BasicButton, WikiListItem},
  data() {
    return {
      wikiItems: [{
        'page_id': 1,
        'description': 'this is wiki item 1'
      }
      , {
        'page_id': 2,
        'description': 'this is wiki item 2'
      }]
    }
  },
})
</script>

<template>
  <div class="flex flex-col-full">
    <div class="flex flex-col w-full">
      <WikiListItem
          class="mx-2"
          v-for="item of wikiItems" :item="item"></WikiListItem>
      <BasicButton class="mx-auto text-sm" :description="'New Document'"></BasicButton>
    </div>
  </div>
</template>

<style scoped>

</style>