<template>
  <div>

    <h1>LoginView</h1>
    <input type="text" v-model="username">
    <br>
    <input type="text" v-model="password">
    <br>
    <button @click="Login">Login</button>


  </div>
</template>

<script>

export default {
  name:'LoginView',
  data(){
    return{
      username:null,
      password:null,
    }
  },
  methods:{
    Login(){
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  }

}
</script>

<style>

</style>