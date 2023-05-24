<template>
  <div>

    
    <!-- {{ detail_data }} -->
    <div v-if="detail_data">
      <div class="detail_card_wrapper" 
      :style="{backgroundImage: `linear-gradient( rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5) ), url(https://image.tmdb.org/t/p/w780${detail_data.backdrop_path})`}"
      >
        <div class="detail_card">
          
          
          
          <div class="m_title">{{ detail_data.title }}</div>     <!--영화 제목--> 
          <div class="various_info_box">
            <div class="row1">
              <div class="m_original_title"><span>원제       </span>{{ detail_data.original_title }}</div> <!-- 영화 원제-->
              <div class="m_release_date"><span>개봉일      </span>{{ detail_data.release_date }}  </div> <!-- 영화 개봉일-->
            </div>
            <div class="row2">
              <div class="m_runtime"><span>상영시간     </span>{{ detail_data.runtime }}분</div> <!-- 영화 러닝타임-->
              <div>
                <span>장르      </span> 
                <div class="m_genre" v-for="(genre, index) in detail_data.genres" :key="genre.id"> <!-- v-for로 genres 배열을 순회하면서 각 genre 출력 -->
                  <div>
                    {{ genre.name }}
                    <!-- {{ detail_data.genres.length }} -->
                    <span v-if="index !== detail_data.genres.length - 1">·</span>  <!-- v-if 로 마지막 genre인 경우에만 '·'이 나타나도록 함.--> 
                  </div>
                </div>
              </div> 
            </div>
          </div>
          <hr>
          <div class="m_summary">  {{ detail_data.overview }}</div> <!-- 영화 줄거리-->
          <hr>
          
          <span>영화 촬영지</span>
          <div class="m_location">
            {{ detail_data.title }} 의 대표적인 촬영지는
            {{detail_data.movielocation_set[current_location ].location_country}}의 
            {{detail_data.movielocation_set[current_location ].location_name}}입니다.
          </div>
          <div @click="moveTo" v-if="detail_data.movielocation_set.length > 1">  <!-- 지역 이동 버튼 (적어도 하나 이상의 지역이 있어야 함)-->
            <div class="moveto_btn">
              <div v-if="(detail_data.movielocation_set.length)-1">
                다른 {{(detail_data.movielocation_set.length)-1}}곳 보기
              </div>
            </div>
          </div>

          <!-- 영화 촬영 지 지역 추가 폼 -->
          <div class="flip-card-wrapper">
            <div class="card-switch">
                <label class="switch">
                  <span class="slider"></span>
                  <span class="card-side"></span>
                  <div class="flip-card__inner">
                    <div class="flip-card__front">
                      <div class="moveto_btn toggle" @click="goAdd">
                        내가 아는 {{ detail_data.title }} 영화 촬영지 추가하기
                      </div>
                      <div class="flip=card" v-if="isCreate">
                        <p class="flip-card__input">지명<input type="text" v-model="addLocationData.location_name"></p>
                        <p class="flip-card__input">경도<input type="text" v-model="addLocationData.longitude"></p>
                        <p class="flip-card__input">위도<input type="text" v-model="addLocationData.latitude"></p>
                        <p class="flip-card__input">국가<input type="text" v-model="addLocationData.location_country"></p>
                        <p class="flip-card__input">영화장면 유튜브 URL<input type="text" v-model="addLocationData.youtube_url"></p>
                        <p class="flip-card__input">지역 사진 URL<input type="text" v-model="addLocationData.location_photo_url"></p>
                        <p class="flip-card__input">지역 설명<input type="text" v-model="addLocationData.location_description"></p> 
                        <button class="submit__btn" @click="createMovieLocation(detail_data.movie_id)">제출하기</button>
                      </div>
                    </div>
                  </div>
                </label>
            </div>   
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
// import { mapState } from "vuex";

export default {
  name:'MovieDetail',
  props:{
    detail_data: Object,
  },
  watch:{
    detail_data(){
      this.moveTo()
    }
  },
  methods:{
    moveTo(){
      if (this.detail_data.movielocation_set.length !== 0) {
        this.current_location += 1
        this.current_location = this.current_location % this.detail_data.movielocation_set.length
        const payload = {
          lat:this.detail_data.movielocation_set[this.current_location].latitude,
          lng:this.detail_data.movielocation_set[this.current_location].longitude,
        }
        this.$store.dispatch('moveTo', payload)
      }
    },

    goAdd(){
      this.isCreate = !this.isCreate
    },
    createMovieLocation(movie_id){
      console.log(movie_id);
      this.addLocationData.tmdb_id = movie_id
      this.addLocationData.user = this.$store.state.user_detail.pk
      axios({
        method:'post',
        headers:`Token ${this.$store.state.token}`,
        url:`http://127.0.0.1:8000/api/v1/location/`,
        data: this.addLocationData
      })
      .then((res)=>{
        console.log(res);
      })
      .catch((err)=>{
        console.log(err);
        alert('폼을 정확히 입력해 주세요')
      })
      .finally(()=>{
        this.isCreate = false
        this.$store.dispatch('getMovieLocations')
        // 
        this.$emit('createData')
      })
    },
  },
  data(){
    return{
      backdrop_path: '{{}}',
      isCreate:false,
      current_location:0,
      addLocationData:{
        tmdb_id:               null,
        location_name:         null,
        latitude:              null,
        longitude:             null,
        location_country:      null,
        youtube_url:           null,
        location_photo_url:    null,
        location_description:  null,
      },
    }
  },

}
</script>

<style>
.detail_card_wrapper {
  position: relative;
  height: 100%;
  background-size: cover;
  background-position: center;

  display: flex;
  flex-direction: column;
  justify-content: center;
}
.detail_card {
  text-align: left;
  padding: 10px;
  margin: 15px;
}

.various_info_box {
  display: flex;
  justify-content: space-between;
}
.row1, .row2 {
  margin-right: 50px;
}
.m_title {
  font-size: 30px;
  color: rgba(200, 255, 255, 1)
}
.m_original_title, .m_release_date, .m_runtime, .m_genre, .m_summary, .m_location {
  color: rgba(255, 255, 255, 0.9);
}
.m_genre {
  display: inline-block;
}
.m_summary {
  margin: 10px;
  font-size: 0.7em;
  line-height: 1.8;
  font-family: 'Noto Sans KR', sans-serif;
}
span {
  color: rgba(200, 255, 255, 1)
}


.movieinfo_menu {
  display: flex;
  cursor: pointer;
}
.moveto_btn {
  --bg: #3B9E83;
  --hover-bg: #0fca66;
  --bg-color: #8AB97C;
  --hover-text: black;
  --main-color: #323232;

  margin: 5px;
  padding: 0.5em 0.5em;

  height: 40px;
  color: #323232;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);

  font-size: 15px;
  font-weight: 400;
  cursor: pointer;
}
.moveto_btn:hover {
  color: var(--hover-text);
  transform: translate(-0.25rem,-0.25rem);
  background: var(--hover-bg);
  box-shadow: 0.25rem 0.25rem var(--bg);
}
.moveto_btn:active {
  transform: translate(0);
  box-shadow: none;
}

/* 영화장소 추가 FORM */
.flip-card-wrapper {
  --input-focus: #2d8cf0;
  --font-color: #323232;
  --font-color-sub: #666;
  --bg-color: #fff;
  --bg-color-alt: #666;
  --main-color: #323232;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.flip-card__inner {
  height: 350px;
  position: relative;
  background-color: transparent;
  perspective: 1000px;
    width: 100%;
    height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}
.flip-card__front {
  display: flex;
  flex-direction: column;
  justify-content: center;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  background: lightgrey;
  gap: 20px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  box-shadow: 4px 4px var(--main-color);
}
.flip-card__form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.flip-card__input {
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
  outline: none;
}
.flip-card__input::placeholder {
  color: var(--font-color-sub);
  opacity: 0.8;
}
.flip-card__input:focus {
  border: 2px solid var(--input-focus);
}
.flip-card__btn:active, .button-confirm:active {
  box-shadow: 0px 0px var(--main-color);
  transform: translate(3px, 3px);
}
.submit__btn {
  margin: 20px 0 20px 0;
  width: 120px;
  height: 40px;
  border-radius: 5px;
  border: 2px solid var(--main-color);
  background-color: var(--bg-color);
  box-shadow: 4px 4px var(--main-color);
  font-size: 17px;
  font-weight: 600;
  color: var(--font-color);
  cursor: pointer;
} 
</style>