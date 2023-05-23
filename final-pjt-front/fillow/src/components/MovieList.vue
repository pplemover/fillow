<template>
  <div @scroll="ScrollEvent" ref="scrollContainer">

    <div class="func_menu">
      <input type="input" placeholder="영화 검색" name="text" class="input" @keyup.enter="getAnotherMovie" v-model.trim="query">
      <div @click="goAddMovie" class="func_btn">영화 추가</div>
      <div @click="goRecommend" class="func_btn">내 위치를 기반으로 추천받기</div>
    </div>

    <div class="movie-list">
      <MovieListItem
      v-for="homemovieitem in homemovielist"
      :key="homemovieitem.movie_id"
      :movieitem="homemovieitem"
      />
      <!-- v-for을 사용하여 MovieListItem 컴포넌트를 여러번 렌더링. -->
      <!-- movieitem를 사용하여 해당 요소를 MovieListItem 컴포넌트에 전달  -->
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  created() {
    this.getMovieList(this.page)
  },
  destroyed(){
  },
  methods:{
    getAnotherMovie(){
      this.homemovielist = null
      this.page = 1
      this.getMovieList(this.page)
    },
    ScrollEvent(){
      const container = this.$refs.scrollContainer;
      const scrollPosition = container.scrollTop + container.clientHeight;
      const scrollHeight = container.scrollHeight;
      // 컴포넌트 안에서 아래쪽에 닿았는지 확인 해야 됨.
      if (scrollPosition === scrollHeight) {
        console.log(true);
        this.beforequery = null
        this.page+=1
        this.getMovieList(this.page)
      }
    },
    getMovieList(page){
      let current = null
      if (this.beforequery) {
        current = this.beforequery
      }
      else{
        current = this.query
      }
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/api/v1/movies/",
        params:{
          query:current,
          page:page,
        }
      })
      .then((res)=>{
        if (this.homemovielist) {
          for (const movie of res.data) {
            this.homemovielist.push(movie)
          }
        } else{
          this.homemovielist = res.data
          // console.log(this.homemovielist);
          this.$store.dispatch('selectThisItem', this.homemovielist[0].movie_id)
        }
        // console.log(res.data);
      })
      .catch((err)=>{
        console.log(err);
      })
      .finally(()=>{
        // this.beforequery = this.query
        // this.query = null
      })
    },
    goRecommend(){
      this.$router.push({name:'RecommendView'})
    },
    goAddMovie(){
      this.$router.push({name:'AddMovieView'})
    },
  },
  data(){
    return{
      homemovielist:null,
      query:null,
      beforequery : null,
      page:1,
    }
  }
}
</script>

<style>
/* 상단 메뉴 버튼 (위치 기반 추천 버튼, 영화추가 버튼) */
/* .func_menu {
  position: fixed;
  display: flex;
  left: 10px;
  right: 15px;
  width: 490px;
  cursor: pointer;
  background-color: white;
}
.func_btn {
  --bg: #3B9E83;
  --hover-bg: #0fca66;
  --bg-color: #3B9E83;
  --hover-text: black;
  --main-color: #323232;

  margin: 5px 5px 5px;
  padding: 0.5em 0.5em;

  height: 40px;
  color: whitesmoke; 
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);

  font-size: 15px;
  font-weight: 400;
}
.func_btn:hover {
  color: var(--hover-text);
  transform: translate(-0.25rem,-0.25rem);
  background: var(--hover-bg);
  box-shadow: 0.25rem 0.25rem var(--bg);
}
.func_btn:active {
  transform: translate(0);
  box-shadow: none;
} */

/* 검색창 */
.input {
  --input-focus: #2d8cf0;
  --font-color: #323232;
  --font-color-sub: #666;
  --bg-color: #fff;
  --main-color: #323232;
  width: 200px;
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

.movie-list {
  margin-top: 60px;
}
</style>