<template>
  <div>
    <section class="sign">
      <h1>회원가입</h1>
      <div class="sign__card">
        <h2>
          <strong>Welcome!</strong> Fillow에 오신 것을 환영합니다.
        </h2>
        <form @submit.prevent="signUp">
          <input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요."><br>
          <input type="password" id="password1" v-model="password1" placeholder="비밀번호를 입력하세요."><br>
          <input type="password" id="password2" v-model="password2" placeholder="비밀번호를 재입력하세요.">
          
          <input type="submit" value="Sign Up">
        </form>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return{
      username:null,
      password1:null,
      password2:null,
    }
  },
  methods: {
    signUp(){
      // console.log('');
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        'username': username,
        'password1': password1,
        'password2': password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
</style>