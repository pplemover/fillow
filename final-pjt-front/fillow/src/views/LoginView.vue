<template>
  <div>
    <section class="signin">
    <h1>로그인</h1>
    <div class="signin__card">
      <h2>
        <strong>Welcome!</strong> Fillow에 오신 것을 환영합니다.
      </h2>
      <form>
        <input type="text" placeholder="아이디를 입력하세요." v-model="username">
        <input type="password" placeholder="비밀번호를 입력하세요." v-model="password">
        <input type="submit" value="SignIn" @click.prevent="Login">
        <router-link :to="{ name: 'SignUpView' }" class="movetosignup">회원가입하기</router-link>
        <!-- SignUpView.vue 로 이동하는 링크를 생성 -->
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
.signin {
  margin-top: 60px;
  padding: 100px 0 150px;
  background-image: url("@/assets/images/bg_login.jpg");
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
  background-size: cover;
}
.signin h1 {
  color: #528265;
  font-size: 30px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 10px;
}
.signin__card {
  width: 500px;
  margin: 0 auto;
  border-radius: 10px;
  background-color: #F6F5F0;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, .3);
  color: #555;
}
.signin__card h2 {
  padding: 30px;
  font-size: 18px;
  text-align: center;
  border-bottom: 1px solid #ddd;
}

.signin__card h2 strong {
  font-weight: 700;
  color: #006633;
}

.signin__card form {
  padding: 30px 22px;
}
.signin__card form input {
  width: 100%;
  margin-bottom: 12px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  outline: none;
  box-sizing: border-box;
  font-size: 14px;
}
.signin__card form [type="submit"] {
  background-color: #006633;
  border: none;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
}
.signin__card form p {
  font-size: 12px;
  color: #006633;
  text-align: center;
}
.signin__card .actions {
  display: flex;
  border-top: 1px solid #ddd;
}
.signin__card .actions a {
  flex-grow: 1;
  flex-basis: 0;
  text-align: center;
  padding: 20px;
  color: #555;
  font-size: 14px;
  border-right: 1px solid #ddd; 
}
.signin__card .actions a:last-child {
  border-right: none;
}
.signin__card .actions a:hover {
  text-decoration: underline;
}

.movetosignup{
  color: black;
}
</style>