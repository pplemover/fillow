<template>
  <div>
    <section class="signup">
      <h1>회원가입</h1>
      <div class="signup__card">
        <h2>
          <strong>Welcome!</strong> Fillow에 오신 것을 환영합니다.
        </h2>
        <form @submit.prevent="signUp">
          <label for="username">아이디를 입력하세요 :</label>
          <input type="text" id="username" v-model="username"><br>

          <label for="password1">비밀번호를 입력하세요 : </label>
          <input type="password" id="password1" v-model="password1"><br>

          <label for="password2">비밀번호를 재입력하세요 :</label>
          <input type="password" id="password2" v-model="password2">
          
          <input type="submit" value="SignUp">
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
.signup {
  padding: 93px;
  background-image: url("@/assets/images/bg_login.jpg");
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
  background-size: cover;
}
.signup h1 {
  color: #528265;
  font-size: 30px;
  font-weight: 700;
  text-align: center;
  margin-bottom: 10px;
}
.signup__card {
  width: 500px;
  margin: 0 auto;
  border-radius: 10px;
  background-color: #F6F5F0;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, .3);
  color: #555;
}
.signup__card h2 {
  padding: 30px;
  font-size: 18px;
  text-align: center;
  border-bottom: 1px solid #ddd;
}

.signup__card h2 strong {
  font-weight: 700;
  color: #006633;
}

.signup__card form {
  padding: 30px 22px;
}
.signup__card form input {
  width: 100%;
  margin-bottom: 12px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  outline: none;
  box-sizing: border-box;
  font-size: 14px;
}
.signup__card form [type="submit"] {
  background-color: #528265;
  border: none;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
}
.signup__card form p {
  font-size: 12px;
  color: #006633;
  text-align: center;
}
.signup__card .actions {
  display: flex;
  border-top: 1px solid #ddd;
}
.signup__card .actions a {
  flex-grow: 1;
  flex-basis: 0;
  text-align: center;
  padding: 20px;
  color: #555;
  font-size: 14px;
  border-right: 1px solid #ddd; 
}
.signup__card .actions a:last-child {
  border-right: none;
}
.signup__card .actions a:hover {
  text-decoration: underline;
}
</style>