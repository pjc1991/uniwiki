<template>
  <div class="bg-blue-600 flex items-center justify-center min-h-screen">
    <div
        v-if="!loading"
        class="bg-white text-black p-6 rounded-lg">
      <Login v-if="!loggedIn && !signup" @get-logged-in="loginCheck" @set-signup="setSignup"></Login>
      <Wiki v-if="loggedIn" :user="user" @get-logged-in="loginCheck"></Wiki>
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
      loading: true,
      user: '',
    }
  },
  mounted() {
    this.getUserData()
  },
  methods: {

    loginCheck(user) {
      if (user === ''){
        this.loggedIn = false
        this.user = ''
        return
      }
      this.loggedIn = true
      this.user = user
    },

    getUserData() {
      fetch('/api/common/users', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(response => {
        if (response.status !== 200) {
          throw new Error('login failed')
        }
        return response.json()
      }).then(data => {
        this.loggedIn = true
        this.user = data[0]
      }).catch((error) => {
        this.$emit('get-jwt', '')
      }).finally(() => {
        this.loading = false
      });
    },

    setSignup(bool) {
      this.signup = !!bool
    },

  }
}
</script>

<style>
#app {
}
</style>
