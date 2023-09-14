<template>
  <div class="bg-blue-600 flex items-center justify-center min-h-screen">
    <div
        class="bg-white text-black p-6 rounded-lg">
      <Login v-if="!loggedIn && !signup" @get-jwt="loginCheck" @set-signup="setSignup"></Login>
      <Wiki v-if="loggedIn" :user="user" @get-jwt="loginCheck"></Wiki>
      <Signup v-if="signup" @set-signup="setSignup"></Signup>
    </div>
  </div>
</template>

<script>
import Login from './components/Login.vue'
import Wiki from "./components/Wiki.vue";
import Signup from "./components/Signup.vue";

export default {
  name: 'App',
  components: {
    Login,
    Wiki,
    Signup,
  },
  data() {
    return {
      loggedIn: false,
      signup: false,
      user: '',
      jwt: ''
    }
  },
  mounted() {
    this.jwt = localStorage.getItem('jwt')
    this.loginCheck(this.jwt)
  },
  methods: {
    loginCheck(jwt) {
      if (jwt === '') {
        this.loggedIn = false
        this.user = ''
        return
      }
      this.getUserData(jwt)
    },
    getUserData(jwt) {
      fetch('/api/common/users/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + jwt
        },
      }).then(response => {
        if(response.status !== 200) {
          throw new Error('login failed')
        }
        return response.json()
      }).then(data => {
        this.loggedIn = true
        this.user = data[0]
      }).catch((error) => {
        localStorage.removeItem('jwt')
        this.$emit('get-jwt', '')
      });

    },
    setSignup(bool) {
      this.signup = !!bool
    }
  }
}
</script>

<style>
#app {
}
</style>
