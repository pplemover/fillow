<template>
  <div class="addmovie_bg">

      <div class="addmovie_container">
        <!-- 첫 화면의 요소 (showInitialContent 데이터 속성을 사용하여 초기 컨텐츠 표시하거나 숨기기)-->
        <div class="black-box"></div>
        <div v-if="showInitialContent" class="addmovie__front"> 
          <div>
            <div aria-label="Orange and tan hamster running in a metal wheel" role="img" class="wheel-and-hamster">
              <div class="wheel"></div>
              <div class="hamster">
                <div class="hamster__body">
                  <div class="hamster__head">
                    <div class="hamster__ear"></div>
                    <div class="hamster__eye"></div>
                    <div class="hamster__nose"></div>
                  </div>
                  <div class="hamster__limb hamster__limb--fr"></div>
                  <div class="hamster__limb hamster__limb--fl"></div>
                  <div class="hamster__limb hamster__limb--br"></div>
                  <div class="hamster__limb hamster__limb--bl"></div>
                  <div class="hamster__tail"></div>
                </div>
              </div>
              <div class="spoke"></div>
            </div>
          </div>
          <div class="addmovie_select">
            <h1 @click="toggleContent">영화 추가 제안하기</h1>
            <span>"어서 오세요! 영화 촬영지 정보 메카, Fillow에 오신 여러분을 환영합니다. 
            <br>
            하지만, 당신이 찾는 영화나 촬영지 정보를 찾지 못했다면 걱정하지 마세요! Fillow는 계속해서 성장하고 발전하고 있습니다. 
            Fillow에 없는 영화나 관련 정보를 추가하고 싶으시다면, 당신의 기여를 환영합니다! 이 위키는 공동체의 힘으로 이루어지는 것이니, 두 손을 모아 함께 만들어봅시다!</span>
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
  cursor: pointer;
  position: relative;
  border: none;
  background: none;
  text-transform: uppercase;
  transition-timing-function: cubic-bezier(0.25, 0.8, 0.25, 1);
  transition-duration: 400ms;
  transition-property: color;
}
.addmovie_select h1:focus,
.addmovie_select h1:hover {
  color: #fff;
}
.addmovie_select h1:focus:after,
.addmovie_select h1:hover:after {
  width: 100%;
  left: 0%;
}
.addmovie_select h1:after {
  content: "";
  pointer-events: none;
  bottom: -2px;
  left: 50%;
  position: absolute;
  width: 0%;
  height: 2px;
  background-color: #fff;
  transition-timing-function: cubic-bezier(0.25, 0.8, 0.25, 1);
  transition-duration: 400ms;
  transition-property: width, left;
}

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

/* HAMSTER ====================== */
.wheel-and-hamster {
  --dur: 1s;
  position: relative;
  width: 200px;
  height: 200px;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  margin: 50px auto;
}

.wheel,
.hamster,
.hamster div,
.spoke {
  position: absolute;
}

.wheel,
.spoke {
  border-radius: 50%;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.wheel {
  background: radial-gradient(100% 100% at center,hsla(0,0%,60%,0) 47.8%,hsl(0,0%,60%) 48%);
  z-index: 2;
}

.hamster {
  animation: hamster var(--dur) ease-in-out infinite;
  top: 50%;
  left: calc(50% - 3.5em);
  width: 7em;
  height: 3.75em;
  transform: rotate(4deg) translate(-0.8em,1.85em);
  transform-origin: 50% 0;
  z-index: 1;
}

.hamster__head {
  animation: hamsterHead var(--dur) ease-in-out infinite;
  background: hsl(30,90%,55%);
  border-radius: 70% 30% 0 100% / 40% 25% 25% 60%;
  box-shadow: 0 -0.25em 0 hsl(30,90%,80%) inset,
		0.75em -1.55em 0 hsl(30,90%,90%) inset;
  top: 0;
  left: -2em;
  width: 2.75em;
  height: 2.5em;
  transform-origin: 100% 50%;
}

.hamster__ear {
  animation: hamsterEar var(--dur) ease-in-out infinite;
  background: hsl(0,90%,85%);
  border-radius: 50%;
  box-shadow: -0.25em 0 hsl(30,90%,55%) inset;
  top: -0.25em;
  right: -0.25em;
  width: 0.75em;
  height: 0.75em;
  transform-origin: 50% 75%;
}

.hamster__eye {
  animation: hamsterEye var(--dur) linear infinite;
  background-color: hsl(0,0%,0%);
  border-radius: 50%;
  top: 0.375em;
  left: 1.25em;
  width: 0.5em;
  height: 0.5em;
}

.hamster__nose {
  background: hsl(0,90%,75%);
  border-radius: 35% 65% 85% 15% / 70% 50% 50% 30%;
  top: 0.75em;
  left: 0;
  width: 0.2em;
  height: 0.25em;
}

.hamster__body {
  animation: hamsterBody var(--dur) ease-in-out infinite;
  background: hsl(30,90%,90%);
  border-radius: 50% 30% 50% 30% / 15% 60% 40% 40%;
  box-shadow: 0.1em 0.75em 0 hsl(30,90%,55%) inset,
		0.15em -0.5em 0 hsl(30,90%,80%) inset;
  top: 0.25em;
  left: 2em;
  width: 4.5em;
  height: 3em;
  transform-origin: 17% 50%;
  transform-style: preserve-3d;
}

.hamster__limb--fr,
.hamster__limb--fl {
  clip-path: polygon(0 0,100% 0,70% 80%,60% 100%,0% 100%,40% 80%);
  top: 2em;
  left: 0.5em;
  width: 1em;
  height: 1.5em;
  transform-origin: 50% 0;
}

.hamster__limb--fr {
  animation: hamsterFRLimb var(--dur) linear infinite;
  background: linear-gradient(hsl(30,90%,80%) 80%,hsl(0,90%,75%) 80%);
  transform: rotate(15deg) translateZ(-1px);
}

.hamster__limb--fl {
  animation: hamsterFLLimb var(--dur) linear infinite;
  background: linear-gradient(hsl(30,90%,90%) 80%,hsl(0,90%,85%) 80%);
  transform: rotate(15deg);
}

.hamster__limb--br,
.hamster__limb--bl {
  border-radius: 0.75em 0.75em 0 0;
  clip-path: polygon(0 0,100% 0,100% 30%,70% 90%,70% 100%,30% 100%,40% 90%,0% 30%);
  top: 1em;
  left: 2.8em;
  width: 1.5em;
  height: 2.5em;
  transform-origin: 50% 30%;
}

.hamster__limb--br {
  animation: hamsterBRLimb var(--dur) linear infinite;
  background: linear-gradient(hsl(30,90%,80%) 90%,hsl(0,90%,75%) 90%);
  transform: rotate(-25deg) translateZ(-1px);
}

.hamster__limb--bl {
  animation: hamsterBLLimb var(--dur) linear infinite;
  background: linear-gradient(hsl(30,90%,90%) 90%,hsl(0,90%,85%) 90%);
  transform: rotate(-25deg);
}

.hamster__tail {
  animation: hamsterTail var(--dur) linear infinite;
  background: hsl(0,90%,85%);
  border-radius: 0.25em 50% 50% 0.25em;
  box-shadow: 0 -0.2em 0 hsl(0,90%,75%) inset;
  top: 1.5em;
  right: -0.5em;
  width: 1em;
  height: 0.5em;
  transform: rotate(30deg) translateZ(-1px);
  transform-origin: 0.25em 0.25em;
}

.spoke {
  animation: spoke var(--dur) linear infinite;
  background: radial-gradient(100% 100% at center,hsl(0,0%,60%) 4.8%,hsla(0,0%,60%,0) 5%),
		linear-gradient(hsla(0,0%,55%,0) 46.9%,hsl(0,0%,65%) 47% 52.9%,hsla(0,0%,65%,0) 53%) 50% 50% / 99% 99% no-repeat;
}

/* Animations */
@keyframes hamster {
  from, to {
    transform: rotate(4deg) translate(-0.8em,1.85em);
  }

  50% {
    transform: rotate(0) translate(-0.8em,1.85em);
  }
}

@keyframes hamsterHead {
  from, 25%, 50%, 75%, to {
    transform: rotate(0);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(8deg);
  }
}

@keyframes hamsterEye {
  from, 90%, to {
    transform: scaleY(1);
  }

  95% {
    transform: scaleY(0);
  }
}

@keyframes hamsterEar {
  from, 25%, 50%, 75%, to {
    transform: rotate(0);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(12deg);
  }
}

@keyframes hamsterBody {
  from, 25%, 50%, 75%, to {
    transform: rotate(0);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(-2deg);
  }
}

@keyframes hamsterFRLimb {
  from, 25%, 50%, 75%, to {
    transform: rotate(50deg) translateZ(-1px);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(-30deg) translateZ(-1px);
  }
}

@keyframes hamsterFLLimb {
  from, 25%, 50%, 75%, to {
    transform: rotate(-30deg);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(50deg);
  }
}

@keyframes hamsterBRLimb {
  from, 25%, 50%, 75%, to {
    transform: rotate(-60deg) translateZ(-1px);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(20deg) translateZ(-1px);
  }
}

@keyframes hamsterBLLimb {
  from, 25%, 50%, 75%, to {
    transform: rotate(20deg);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(-60deg);
  }
}

@keyframes hamsterTail {
  from, 25%, 50%, 75%, to {
    transform: rotate(30deg) translateZ(-1px);
  }

  12.5%, 37.5%, 62.5%, 87.5% {
    transform: rotate(10deg) translateZ(-1px);
  }
}

@keyframes spoke {
  from {
    transform: rotate(0);
  }

  to {
    transform: rotate(-1turn);
  }
}
</style>