<template>
  <div class="info_card">
    <div class="d-flex" v-if="!isUpdating">
      <div>
        <div class="info_card_info">
          <!-- {{ movieLocationItem }} -->
          <div>
            <p class="fw-bold location_title marginadjust">{{ movieLocationItem.location_country }} </p> 
            <p class="fw-bold location_title marginadjust">{{ movieLocationItem.location_name }}</p>
          </div>
          <div>
            <span>수정한 FILLOW 회원 ID: {{ movieLocationItem.user }} </span>
            <span v-if="movieLocationItem.updated_at">마지막 수정 시간:{{ movieLocationItem.updated_at.slice(0,10) }} </span>
          </div>
          <button @click="goUpdate" class="moveto_btn">수정하기</button>
        </div>
      </div>
      <div class="location_container">
        <img :src="movieLocationItem.location_photo_url" alt="" class="location">
      </div>

    </div>

    <!-- 업데이트 할떄 -->
    <!-- <div v-if="isUpdating">
      <p>지명:<input type="text" v-model="updatingData.location_name"></p>
      <p>경도:<input type="text" v-model="updatingData.longitude"></p>
      <p>위도:<input type="text" v-model="updatingData.latitude"></p>
      <p>국가<input type="text" v-model="updatingData.location_country"></p>
      <p>영화장면 유튜브 URL<input type="text" v-model="updatingData.youtube_url"></p>
      <p>지역 사진 URL<input type="text" v-model="updatingData.location_photo_url"></p>
      <p>지역 설명<input type="text" v-model="updatingData.location_description"></p> 
      <button @click="updateMovieLocation">수정 완료</button>
    </div> -->

    <form class="form" v-if="isUpdating">
        <p class="title">영화 촬영지 정보 수정하기 </p>
        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.location_name">
            <span>지명</span>
        </label>
        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.longitude">
            <span>경도</span>
        </label>
        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.latitude">
            <span>위도</span>
        </label>    
        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.location_country">
            <span>국가</span>
        </label> 
            
        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.youtube_url">
            <span>영화장면 유튜브 URL</span>
        </label>

        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.location_photo_url">
            <span>지역사진 URL</span>
        </label>

        <label>
            <input required="" placeholder="" type="text" class="input" v-model="updatingData.location_description">
            <span>지역 설명</span>
        </label>
        <button class="submit" @click.prevent="updateMovieLocation">수정 완료</button>
    </form>


  </div>
</template>

<script>
import axios from 'axios'


export default {
  name:'InfoWindow',
  props: {
    movieLocationItem: Object,
  },
  data(){
    return{
      isUpdating:false,
      updatingData:{
        tmdb_id:               this.movieLocationItem.tmdb_id,
        location_name:         this.movieLocationItem.location_name,
        latitude:              this.movieLocationItem.latitude,
        longitude:             this.movieLocationItem.longitude,
        location_country:      this.movieLocationItem.location_country,
        youtube_url:           this.movieLocationItem.youtube_url,
        location_photo_url:    this.movieLocationItem.location_photo_url,
        location_description:  this.movieLocationItem.location_description,
      }
    }
  },
  methods:{

    goUpdate(){
      if(window.confirm('정보를 수정하시겠습니까?')){
        if (!this.$store.getters.isLogin) {
          this.$router.push({name:'LoginView'})
        }else{
          this.isUpdating = !this.isUpdating
        }
      }
    },
    updateMovieLocation(){
      this.updatingData.user = this.$store.state.user_detail.pk
      axios({
        method:'put',
        headers:`Token ${this.$store.state.token}`,
        url:`http://127.0.0.1:8000/api/v1/updatelocation/${this.movieLocationItem.id}/`,
        data: this.updatingData
      })
      .then((res)=>{
        console.log(res);
        this.isUpdating = false
        this.$store.dispatch('getMovieLocations')
        this.$emit('updatecomplete')
      })
      .catch((err)=>{
        console.log(err);
      })
      .finally(()=>{
      })
    }
  }
}
</script>

<style scoped>
.info_card {
  position: relative;
  font-family: 'Do Hyeon', sans-serif;
  padding: 5px;
  background-color: #282828;
  color: white;
}
.info_card_info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.location_container {
  /* position: absolute; */
  right: 5px;
}
.location {
  border-radius: 5px;
  width: 300px;
  background-size: cover;
}
.location_title{
  font-size: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 100%;
  background-color: #1f1f1f;
  padding: 10px;
  border-radius: 20px;
  position: relative;
}
.form p {
  color: white;
}
.title {
  font-size: 20px;
  color: #0fca66;
  font-weight: 600;
  letter-spacing: -1px;
  position: relative;
  display: flex;
  align-items: center;
  padding-left: 30px;
}

.title::before,.title::after {
  position: absolute;
  content: "";
  height: 16px;
  width: 100%;
  border-radius: 50%;
  left: 0px;
  background-color: #0fca66;
}

.title::before {
  width: 18px;
  height: 18px;
  background-color: royalblue;
}

.title::after {
  width: 18px;
  height: 18px;
  animation: pulse 1s linear infinite;
}

.signin {
  color: rgba(88, 87, 87, 0.822);
  font-size: 14px;
}
.signin {
  text-align: center;
}
.signin a {
  color: royalblue;
}

.signin a:hover {
  text-decoration: underline royalblue;
}

.flex {
  display: flex;
  width: 100%;
  gap: 6px;
}

.form label {
  position: relative;
}

.form label .input {
  width: 100%;
  padding: 10px 10px 20px 10px;
  outline: 0;
  border: 1px solid rgba(105, 105, 105, 0.397);
  border-radius: 10px;
}

.form label .input + span {
  position: absolute;
  left: 10px;
  top: 15px;
  color: grey;
  font-size: 0.9em;
  cursor: text;
  transition: 0.3s ease;
}

.form label .input:placeholder-shown + span {
  top: 15px;
  font-size: 0.9em;
}

.form label .input:focus + span,.form label .input:valid + span {
  top: 30px;
  font-size: 0.7em;
  font-weight: 600;
}

.form label .input:valid + span {
  color: green;
}

.submit {
  border: none;
  outline: none;
  background-color: #0fca66;
  padding: 10px;
  border-radius: 10px;
  color: #fff;
  font-size: 16px;
  transform: .3s ease;
}

.submit:hover {
  background-color: rgb(56, 90, 194);
}

.marginadjust {
  margin: 5px;
  padding: 10px;
}

@keyframes pulse {
  from {
    transform: scale(0.9);
    opacity: 1;
  }
  to {
    transform: scale(1.8);
    opacity: 0;
  }
}
</style>