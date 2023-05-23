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
              <div class="m_original_title"><span>원제       </span>{{ detail_data.original_title }}</div> <!-- 영화 원제-->
              <div class="m_release_date"><span>개봉일      </span>{{ detail_data.release_date }}  </div> <!-- 영화 개봉일-->
            </div>
            <div class="row3">
              <div class="m_original_title"><span>원제       </span>{{ detail_data.original_title }}</div> <!-- 영화 원제-->
              <div class="m_release_date"><span>개봉일      </span>{{ detail_data.release_date }}  </div> <!-- 영화 개봉일-->
            </div>
          </div>
          <hr>
          <div class="m_summary"><span>줄거리       </span>{{ detail_data.overview }}</div> <!-- 영화 줄거리-->
      

          <!-- {{((detail_data.vote_avg)/2).toFixed(1)}}

          <span>언어</span>{{movieitem.original_language}} -->
          
        </div>

        <div v-if="detail_data.movielocation_set.length > 0" @click="moveTo">  <!-- 지역 이동 버튼 (적어도 하나 이상의 지역이 있어야 함)-->
          <div class="moveto_btn">영화 촬영지인 {{detail_data.movielocation_set[current_location ].location_name}}로 바로 이동하기</div>
        </div>
        <div class="moveto_btn" @click="goAdd">영화 촬영지 추가하기</div>
          
      </div>
    </div>

    <!-- 지역 추가 폼 -->
    <div v-if="isCreate">
      <p>지명<input type="text" v-model="addLocationData.location_name"></p>
      <p>위도<input type="text" v-model="addLocationData.longitude"></p>
      <p>경도<input type="text" v-model="addLocationData.latitude"></p>
      <p>국가<input type="text" v-model="addLocationData.location_country"></p>
      <p>영화장면 유튜브 URL<input type="text" v-model="addLocationData.youtube_url"></p>
      <p>지역 사진 URL<input type="text" v-model="addLocationData.location_photo_url"></p>
      <p>지역 설명<input type="text" v-model="addLocationData.location_description"></p> 
      <button @click="createMovieLocation(detail_data.movie_id)">지역 추가</button>
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
  methods:{
    moveTo(){
      this.current_location += 1
      this.current_location = this.current_location % this.detail_data.movielocation_set.length
      const payload = {
        lat:this.detail_data.movielocation_set[this.current_location].latitude,
        lng:this.detail_data.movielocation_set[this.current_location].longitude,
      }
      this.$store.dispatch('moveTo', payload)
    },

    goAdd(){
      this.isCreate = !this.isCreate
    },
    createMovieLocation(movie_id){
      console.log(movie_id);
      this.addLocationData.tmdb_id = movie_id
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
        this.$emit('updateData')
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
}
.detail_card {
  text-align: left;
  padding: 10px;
}

.various_info_box {
  display: flex;
}
.row1, .row2 {
  margin-right: 15px;
}
.m_title {
  font-size: 25px;
  color: rgba(255, 255, 255, 1)
}
.m_original_title, .m_release_date, .m_summary {
  color: rgba(255, 255, 255, 0.8)
}

.movieinfo_menu {
  display: flex;
  cursor: pointer;
}
.moveto_btn {
  --bg: #3B9E83;
  --hover-bg: #0fca66;
  --bg-color: #3B9E83;
  --hover-text: black;
  --main-color: #323232;

  margin: 5px;
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

span {
  color: rgba(255, 255, 255, 1)
}
</style>