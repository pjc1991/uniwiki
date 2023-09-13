<template>
  <Login v-if="!loggedIn" @get-jwt="loginCheck"></Login>
  <p v-if="loggedIn">yes i'm logged in as {{ user.username }}</p>
</template>

<script>
import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    Login
  },
  data() {
    return {
      loggedIn: false,
      user: '',
      jwt: ''
    }
  },
  methods: {
    loginCheck(jwt) {
      this.getUserData(jwt)
    },
    getUserData(jwt) {
      fetch('/api/common/users/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + jwt
        },
      }).then(response => response.json())
          .then(data => {
            console.log(data)
            this.loggedIn = true
            this.user = data[0]
          })

    }
  }
}
</script>

<style>
#app {
}
</style>
