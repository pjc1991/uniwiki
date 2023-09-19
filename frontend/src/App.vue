<template>
  <div class="bg-blue-600 flex items-center justify-center h-screen transition-all duration-200 ease-in-out">
    <div
        v-if="!loading"
        class="main-container bg-white text-black p-6 rounded-lg shadow-lg w-full md:w-2/3 lg:w-1/2 xl:w-1/3 h-5/6 transition-all duration-200 ease-in-out">
      <Login
        v-if="!loggedIn && !signup"
        @get-logged-in="loginCheck"
        @set-signup="setSignup"
        class="login-component">
      </Login>

      <Wiki
        v-if="loggedIn && !signup"
        :user="user"
        @get-logged-in="loginCheck"
        class="wiki-component">
      </Wiki>

      <Signup
        v-if="signup"
        @set-signup="setSignup"
        class="signup-component">
      </Signup>
    </div>
  </div>
</template>

<script>
import Login from './components/App/Login.vue'
import Wiki from "./components/App/Wiki.vue";
import Signup from "./components/App/Signup.vue";
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
