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

    <footer>
      <ul class="menu">
        <li><a href="javascript:void(0)" class="green">개인정보처리방침</a></li>
        <li><a href="javascript:void(0)">영상정보처리기기 운영관리 방침</a></li>
        <li><a href="javascript:void(0)">홈페이지 이용약관</a></li>
        <li><a href="javascript:void(0)">위치정보 이용약관</a></li>
        <li><a href="javascript:void(0)">윤리경영 핫라인</a></li>
      </ul>

      <div class="btn-group">
        <a href="javascript:void(0)" class="btn btn--white">찾아오시는 길</a>
        <a href="javascript:void(0)" class="btn btn--white">사이트 맵</a>
      </div>

      <div class="info">
        <span>1학기 최종 프로젝트</span>
        <span>개인정보 책임자 : 임휘진</span>
      </div>

      <p class="copyright">
        &copy; <span class="this-year"></span> Starbucks Coffee Company. All Rights Reserved.
      </p>
      <!-- <img src="@/assets/images/logo.png" alt="logo" class="logo" /> -->
    </footer>

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