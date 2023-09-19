<script>
import {defineComponent} from 'vue'
import BasicForm from "../../BasicForm.vue";
import MessageWindow from "../../MessageWindow.vue";
import BasicButton from "../../BasicButton.vue";

export default defineComponent({
  components: {BasicButton, MessageWindow, BasicForm},
  props: [
    'user'
  ],
  name: "UniverseList"
  , data() {
    return {
      universes: []
      , universeCreateRequest: {
        name: ''
      }
    }
  }, mounted() {
    this.getUniverseList()
  },
  methods: {
    getUniverseList() {
      fetch('/api/wiki/universe/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
      })
          .then(response => response.json())
          .then(data => {
            this.universes = data
          })
          .catch((error) => {
            console.error('Error:', error);
          });
    },
    createUniverse() {
      const csrftoken = getCookie('csrftoken')
      fetch('/api/wiki/universe/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
          name: this.universeToCreate,
        })
      }).then(response => {
        if (response.status !== 200) {
          throw new Error('save failed')
        }
        return response.json()
      }).then(data => {
        this.universes.push(data)
        this.universeToCreate = ''
      }).catch((error) => {
        console.log(error)
      });
    },
  },
})
</script>

<template>
  <div>
    <ol>
      <li v-for="universe in universes" :key="universe.id">
        {{ universe.name }}
      </li>
    </ol>
    <div v-if="universes.length === 0">
      <MessageWindow
          :message="'No Universe available. '"/>
      <BasicForm
          v-model="universeToCreate"
          :name="'universeName'"
          :description="'Create Universe'"/>
      <BasicButton
          @click="createUniverse"
          :description="'Create!'"/>
    </div>
  </div>
</template>

<style scoped>

</style>