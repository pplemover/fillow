<template>
  <div class="addmovie_bg">

      <div class="addmovie_container">
        <!-- 첫 화면의 요소 (showInitialContent 데이터 속성을 사용하여 초기 컨텐츠 표시하거나 숨기기)-->
        <div class="black-box"></div>
        <div v-if="showInitialContent" @click="toggleContent" class="addmovie__front"> 
          <div>
            ICON
          </div>
          <div class="addmovie_select">
            <h1>내가 좋아하는 영화 추가하기</h1>
            <span>"어서 오세요! Fillow에 오신 여러분을 환영합니다. 여기에서는 다양한 영화의 촬영지 정보를 공유하고 있습니다. 
            하지만, 당신이 찾는 영화나 정보를 찾지 못했다면 걱정하지 마세요! 우리 위키는 계속해서 성장하고 발전하고 있습니다. 
            우리 DB에 없는 영화나 관련 정보를 추가하고 싶으시다면, 당신의 기여를 환영합니다! 
            이 위키는 공동체의 힘으로 이루어지는 것이니, 두 손을 모아 함께 만들어봅시다!</span>
          </div>
        </div>

        <!-- 진짜 보여줄 내용 -->
        <div v-if="!showInitialContent" class="addmovie__back"> 
          <div class="black-box"></div>

          <div class="search-box" @keyup.enter="CheckMovie">
            <input type="input" placeholder="영화 검색" name="text" class="input"  v-model="query">
            <button class="check_btn" @click="CheckMovie">확인</button>
          </div>
          <div v-if="search_result">
            <div v-if="!search_result.poster_path">
              <p>{{ search_result.title }}</p>
              <p>{{ search_result.overview }}</p>
            </div>

            <div class="three-body" v-if="isload">
              <div class="three-body__dot"></div>
              <div class="three-body__dot"></div>
              <div class="three-body__dot"></div>
            </div>

            <img v-if="search_result.poster_path" :src="`https://image.tmdb.org/t/p/original/${search_result.poster_path}`" alt="" width="500px" @load="loadingcomplete">
            <br>
            <button @click="addMovietoDB(search_result.id)">이 영화 추가하기</button>
          </div>
        </div>
      </div>

  </div>
</template>

<script>
import axios from 'axios';
const TMDB_API_KEY = '6aee34be99bb1d1b3fa358b709332b7e'

export default {
  name:'AddMovieView',
  data(){
    return{
      isload:false,
      query: null,
      search_result:null,
      showInitialContent: true,
    }
  },
  methods:{
    loadingcomplete(){
      this.isload = false
    },
    CheckMovie(){
      this.isload = true
      this.search_result = null
      axios({
        method:'get',
        url:`https://api.themoviedb.org/3/search/movie`,
        params:{
          api_key:TMDB_API_KEY,
          query:this.query,
          language:'ko',
        },
      })
      .then((res)=>{
        // console.log(res.data.results);
        if (res.data.results.length !== 0) {
          this.search_result = res.data.results[0]
        } else{
          alert('제대로 입력하세요')
        }
        this.query = null
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    addMovietoDB(movie_id){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/api/v1/movies/?id=${movie_id}`
      })
      .then((res)=>{
        console.log(res);
        this.$router.push({name:'RecommendView'})
      })
      .catch((err)=>{
        alert('이미 있는 영화입니다');
        console.log(err);
      })
    },
    // 클릭 이벤트 발생 시 'showInitialContent'를 false로 설정하여 초기 컨텐츠를 숨김.
    toggleContent() {
      this.showInitialContent = false;
    }
  }
}
</script>

<style>
.addmovie_bg {
  background-color: #1f1f1f;
  min-height: 100vh; 
  display: flex;
  justify-content: center;
  align-items: center;
}
.addmovie_container {
  display: flex;
  align-items: center;
  justify-content: center;
}
.addmovie_select {
  width: 500px;
  font-family: 'Black Han Sans', sans-serif;
}
.addmovie_select h1 {
  color: white;
}

/* loader 크기는 가로세로 200px */

/* 검색창  */
.input {
  position: relative;
  --input-focus: #2d8cf0;
  --font-color: #323232;
  --font-color-sub: #666;
  --bg-color: #fff;
  --main-color: #323232;
  width: 100%;
  height: 40px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);
  font-size: 15px;
  font-weight: 600;
  color: var(--font-color);
  padding: 5px 10px;
  margin-top: 5px;
  outline: none;
}
.input::placeholder {
  color: var(--font-color-sub);
  opacity: 0.8;
}
.input:focus {
  border: 2px solid var(--input-focus);
}

.check_btn {
  --bg: #3B9E83;
  --hover-bg: #0fca66;
  --bg-color: #3B9E83;
  --hover-text: black;
  --main-color: #323232;
  
  margin: 5px;
  padding: 0.2em 0.2em;
  
  width: 50px;
  height: 40px;
  color: whitesmoke; 
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);
  
  font-size: 15px;
  font-weight: 400;
}
.check_btn:hover {
  color: var(--hover-text);
  transform: translate(-0.25rem,-0.25rem);
  background: var(--hover-bg);
  box-shadow: 0.25rem 0.25rem var(--bg);
}
.check_btn:active {
  transform: translate(0);
  box-shadow: none;
}

/* LOADER ====================== */
.three-body {
 --uib-size: 35px;
 --uib-speed: 0.8s;
 --uib-color: #5D3FD3;
 position: relative;
 display: inline-block;
 height: var(--uib-size);
 width: var(--uib-size);
 animation: spin78236 calc(var(--uib-speed) * 2.5) infinite linear;
}
.three-body__dot {
 position: absolute;
 height: 100%;
 width: 30%;
}
.three-body__dot:after {
 content: '';
 position: absolute;
 height: 0%;
 width: 100%;
 padding-bottom: 100%;
 background-color: var(--uib-color);
 border-radius: 50%;
}
.three-body__dot:nth-child(1) {
 bottom: 5%;
 left: 0;
 transform: rotate(60deg);
 transform-origin: 50% 85%;
}
.three-body__dot:nth-child(1)::after {
 bottom: 0;
 left: 0;
 animation: wobble1 var(--uib-speed) infinite ease-in-out;
 animation-delay: calc(var(--uib-speed) * -0.3);
}
.three-body__dot:nth-child(2) {
 bottom: 5%;
 right: 0;
 transform: rotate(-60deg);
 transform-origin: 50% 85%;
}
.three-body__dot:nth-child(2)::after {
 bottom: 0;
 left: 0;
 animation: wobble1 var(--uib-speed) infinite
    calc(var(--uib-speed) * -0.15) ease-in-out;
}

.three-body__dot:nth-child(3) {
 bottom: -5%;
 left: 0;
 transform: translateX(116.666%);
}
.three-body__dot:nth-child(3)::after {
 top: 0;
 left: 0;
 animation: wobble2 var(--uib-speed) infinite ease-in-out;
}
@keyframes spin78236 {
 0% {
  transform: rotate(0deg);
 }
 100% {
  transform: rotate(360deg);
 }
}
@keyframes wobble1 {
 0%,
  100% {
  transform: translateY(0%) scale(1);
  opacity: 1;
 }
 50% {
  transform: translateY(-66%) scale(0.65);
  opacity: 0.8;
 }
}
@keyframes wobble2 {
 0%,
  100% {
  transform: translateY(0%) scale(1);
  opacity: 1;
 }
 50% {
  transform: translateY(66%) scale(0.65);
  opacity: 0.8;
 }
}
/*  ============= */
</style>