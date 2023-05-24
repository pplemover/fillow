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

            <!-- 영화 줄거리-->
            <hr>
            <span style="color: lightcoral">영화 줄거리</span>
            <div class="m_summary">  {{ detail_data.overview }}</div> 
            <hr>
            
            <!-- 영화 촬영지-->
            <span style="color: lightcoral">영화 촬영지</span>
            <div class="m_location" v-if="detail_data.movielocation_set.length !== 0">
              {{ detail_data.title }} 의 대표적인 촬영지는
              {{detail_data.movielocation_set[current_location ].location_country}}의 
              {{detail_data.movielocation_set[current_location ].location_name}}입니다.

              <div class="m_summary" v-if="(detail_data.movielocation_set[current_location].location_description)">
                {{ detail_data.movielocation_set[current_location ].location_description }}
              </div>
            </div>

            <!-- 지역 이동 버튼 -->
            <div @click="moveTo" v-if="detail_data.movielocation_set.length > 1">
              <div class="moveto_btn">
                <div v-if="(detail_data.movielocation_set.length)-1">
                  다른 {{ detail_data.title }} 촬영지 {{(detail_data.movielocation_set.length)-1}}곳 보기
                </div>
              </div>
            </div>

            <!-- 영화 촬영지 지역 추가 폼 -->
            <div class="submit_wrapper">
              <div class="moveto_btn" @click="goAdd">
                내가 아는 다른 {{ detail_data.title }} 영화 촬영지 추가하기
              </div>
              <!-- <div class="flip=card" v-if="isCreate">
                <p class="flip-card__input">지명<input type="text" v-model="addLocationData.location_name"></p>
                <p class="flip-card__input">경도<input type="text" v-model="addLocationData.longitude"></p>
                <p class="flip-card__input">위도<input type="text" v-model="addLocationData.latitude"></p>
                <p class="flip-card__input">국가<input type="text" v-model="addLocationData.location_country"></p>
                <p class="flip-card__input">영화장면 유튜브 URL<input type="text" v-model="addLocationData.youtube_url"></p>
                <p class="flip-card__input">지역 사진 URL<input type="text" v-model="addLocationData.location_photo_url"></p>
                <p class="flip-card__input">지역 설명<input type="text" v-model="addLocationData.location_description"></p> 
              </div> -->

              <div class="form" v-if="isCreate">
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.location_name">
                  <span class="highlight-span"></span>
                  <label class="input_label"> 
                    지명
                  </label>
                </div>
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.longitude">
                  <span class="highlight-span"></span>
                  <label class="input_label">
                    경도
                  </label>
                </div>
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.latitude">
                  <span class="highlight-span"></span>
                  <label class="input_label">
                    위도
                  </label>
                </div>
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.location_country">
                  <span class="highlight-span"></span>
                  <label class="input_label">
                    국가
                  </label>
                </div>
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.youtube_url">
                  <span class="highlight-span"></span>
                  <label class="input_label">
                    유튜브 URL
                  </label>
                </div>
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.location_photo_url">
                  <span class="highlight-span"></span>
                  <label class="input_label">
                    지역사진
                  </label>
                </div>
                <div class="group">
                  <input required="true" class="main-input" type="text" v-model="addLocationData.location_description">
                  <span class="highlight-span"></span>
                  <label class="input_label">
                    지역설명
                  </label>
                </div>
                <button class="moveto_btn submit_btn" @click="createMovieLocation(detail_data.movie_id)">제출하기</button>
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
    // 이게 진짜 있네?
    detail_data(newValue,oldValue){
      if (newValue && oldValue) {  // 전, 후 둘다 있으면(없으면 생성시에 오류 뜸)
        console.log(newValue, oldValue);
        if (newValue.movie_id !== oldValue.movie_id) {  // 만약 선택 영화가 바뀐 경우
          this.current_location = this.detail_data.movielocation_set.length-1
          this.moveTo()
          this.isCreate = false
        // 영화 장소 리스트 길이가 바뀐 경우(추가되거나 삭제된 경우 똑같이 시행)
        } else if(newValue.movielocation_set.length !== oldValue.movielocation_set.length){ 
          this.current_location = this.detail_data.movielocation_set.length-1
          this.moveTo()
          this.isCreate = false
        } else{  // 그대로인 경우(데이터가 바뀌었는데 길이는 그대로 === 수정된 경우)
          // console.log(123);
          let update_index = 0
          for (let index = 0; index < newValue.movielocation_set.length; index++) {
            // console.log(newValue.movielocation_set[index]);
            if (JSON.stringify(newValue.movielocation_set[index]) !== JSON.stringify(oldValue.movielocation_set[index])) {
              update_index = index
              break
            }
          }
          this.current_location = update_index
          console.log(this.current_location);
          this.moveTo()
          this.isCreate = false
        }
      }
      // console.log(123);
      // detail data 변경, 즉 이 폼 채우는 데이터 변경 감지되서 실행되면 데이터가 가진 마지막 location_set 요소 가져오게 해서 지도 이동
      // 데이터 수정시에도 시행되서 역시 마지막 데이터로 이동
      // 수정된 데이터로 이동할 수 있는 방법???????
      else{
        this.current_location = this.detail_data.movielocation_set.length-1
        this.moveTo()
        this.isCreate = false
      }
    }
  },
  methods:{
    moveTo(){
      if (this.detail_data.movielocation_set.length !== 0) {
        const payload = {
          lat:this.detail_data.movielocation_set[this.current_location].latitude,
          lng:this.detail_data.movielocation_set[this.current_location].longitude,
        }
        // console.log('#######################################################');
        // console.log(this.detail_data);
        // console.log(this.current_location);
        // console.log('#######################################################');
        this.$store.dispatch('moveTo', payload)
        // 순환
        this.current_location += 1
        this.current_location = this.current_location % this.detail_data.movielocation_set.length
        // 순환
      }
    },

    goAdd(){
      console.log(this.$store.getters.isLogin);
      if (!this.$store.getters.isLogin) {
        this.$router.push({name:'LoginView'})
      }
      else{
        this.isCreate = !this.isCreate
      }
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
  border-radius: 10px;

  display: flex;
  flex-direction: column;
  justify-content: center;
}
.detail_card {
  text-align: left;
  padding: 10px;
  margin: 15px;
  position: relative;
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
  color: darkgrey;
  font-weight: 500;
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
.group {
  position: relative;
  padding-bottom: 15px;
}
.form {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  padding: 15px;
  margin: 5px 20px;
  background-color: black;
  border-radius: 5px;
  position: relative;
}
.main-input {
  font-size: 16px;
  padding: 5px;
  display: block;
  width: 350px;
  border: none;
  border-bottom: 1px solid #6c6c6c;
  background: transparent;
  color: #ffffff;
}
.main-input:focus {
  outline: none;
  border-bottom-color: #42ff1c;
}
.input_label {
  color: #999999;
  font-size: 16px;
  font-weight: normal;
  position: absolute;
  pointer-events: none;
  left: 5px;
  top: 10px;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}

.main-input:focus ~ .input_label,
.main-input:valid ~ .input_label {
  top: -20px;
  font-size: 16px;
  color: #42ff1c;
}
.highlight-span {
  position: absolute;
  height: 60%;
  width: 0px;
  top: 25%;
  left: 0;
  pointer-events: none;
  opacity: 0.5;
}

.main-input:focus ~ .highlight-span {
  -webkit-animation: input-focus 0.3s ease;
  animation: input-focus 0.3s ease;
}

@keyframes input-focus {
  from {
    background: #42ff1c;
  }
  to {
    width: 500px;
  }
}
.submit {
  margin-top: 1.2rem;
  padding: 10px 20px;
  border-radius: 10px;
}
</style>