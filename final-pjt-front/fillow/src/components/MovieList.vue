<template>
  <div @scroll="ScrollEvent" ref="scrollContainer" class="MovieList">

    <div class="black-box"></div>

    <div class="search-box">
      <input type="input" placeholder="영화 검색" name="text" class="input" @keyup.enter="getAnotherMovie" v-model.trim="query">
    </div>

    <div class="movie-list">
      <MovieListItem
      v-for="homemovieitem in homemovielist"
      :key="homemovieitem.movie_id"
      :movieitem="homemovieitem"
      :class="{selected : homemovieitem.movie_id === $store.state.homemovieselect_id}"
      />
      <!-- v-for을 사용하여 MovieListItem 컴포넌트를 여러번 렌더링. -->
      <!-- movieitem를 사용하여 해당 요소를 MovieListItem 컴포넌트에 전달  -->
    </div>
    <div v-if="queryerror">제대로 입력하세요</div>

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
      // console.log(scrollPosition, scrollHeight, '##################');
      // 컴포넌트 안에서 아래쪽에 닿았는지 확인 해야 됨.
      if (scrollPosition >= scrollHeight) {
        console.log(true);
        this.page+=1
        this.getMovieList(this.page)
      }
    },
    getMovieList(page){
      this.queryerror = false
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
        // console.log(res.data.length);
        if (res.data.length === 0) {
          this.queryerror = true
        } else if (this.homemovielist) {
          for (const movie of res.data) {
            this.homemovielist.push(movie)
          }
        } else{
          this.homemovielist = res.data
          // console.log(this.homemovielist);
          this.$store.dispatch('selectThisItem', this.homemovielist[0].movie_id)
        }
        // console.log(res.data);
        this.beforequery = this.query
        this.query = null
      })
      .catch((err)=>{
        console.log(err);
      })
      .finally(()=>{
      })
    },
  },
  data(){
    return{
      homemovielist:null,
      query:null,
      beforequery : null,
      page:1,
      queryerror: false,
    }
  }
}
</script>

<style>
.MovieList {
  position: relative;
}

/* 검색창 */
.search-box {
  position: absolute;
  left: 10px;
  right: 10px;
}

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

.movie-list {
  margin-top: 60px;
}

.selected {
  background-color: #f8f4f4;
}
</style>