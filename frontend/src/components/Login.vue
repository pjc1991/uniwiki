<template>
  <html>
  <form @submit.prevent="login">
    <basicForm :name="'email'" :description="'E-mail'" v-model="email"></basicForm>
    <basicForm :name="'password'" :description="'Password'" :is-secret="true" v-model="password"></basicForm>
    <button type="submit">login button</button>
  </form>
  </html>
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
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password
        })
      })
      .then(response => response.json())
      .then(data => {
        localStorage.setItem('jwt', data.access)
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  }
}

</script>

<style scoped>

</style>