<template>
  <div>
    <section class="sign">
      <h1>로그인</h1>
      <div class="sign__card">
        <h2>
          <strong>Welcome!</strong> Fillow에 오신 것을 환영합니다.
        </h2>
        <form>
          <input type="text" placeholder="아이디를 입력하세요." v-model="username">
          <input type="password" placeholder="비밀번호를 입력하세요." v-model="password">
          <input type="submit" value="Sign In" @click.prevent="Login">
          <router-link :to="{ name: 'SignUpView' }">회원가입하기</router-link>
          <!-- signinView.vue 로 이동하는 링크를 생성 -->
          <hr>
          <p>
            * 비밀번호를 타 사이트와 같이 사용할 경우 도용 위험이 있으니,<br>
            정기적으로 비밀번호를 변경하세요!
          </p>
        </form>
      </div>
  </section>


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