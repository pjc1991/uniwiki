<template>
  <div class="content-center">
    <form @submit.prevent="login">
      <basicForm :name="'email'" :description="'E-mail'" v-model="email"></basicForm>
      <basicForm :name="'password'" :description="'Password'" :is-secret="true" v-model="password"></basicForm>
      <div class="flex justify-end">
        <button
            type="submit"
            class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold
            py-2 px-4 rounded"
        >
          Login!
        </button>
      </div>
    </form>
    <div class="justify-center flex">
      <p class="mt-4 text-blue-500 hover:text-blue-800 cursor-pointer"
         @click="toggleSignup">
        Are you new here?
      </p>
    </div>

  </div>
</template>

<script>
import basicForm from './basicForm.vue'

export default {
  name: 'Login',
  components: {
    basicForm
  },
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login() {
      fetch('/api/common/auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
        })
      })
      .then(response => {
        if (response.status !== 200) {
          console.log("login failed")
          throw new Error('login failed')
        }
        return response.json()
      })
      .then(data => {
        this.$emit('get-logged-in', data.user)
      })
      .catch((error) => {
        this.$emit('get-logged-in', '')
      });
    },
    toggleSignup(){
      this.$emit('set-signup', true)
    },
  }
}

</script>

<style scoped>

</style>