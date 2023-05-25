<template>
  <div>
    <div class="recommend_card_container">

      <div class="recommend_card" v-if="movie">
        <div class="content">
          <div class="back">
            
            <div class="back-content" v-if="item.data.location_photo_url" >
              <img :src="item.data.location_photo_url" alt="해당 촬영지에 대해 사용지가 추가한 이미지가 없습니다" width="800px">
            </div>
            
          </div>

          <div class="front">
            <img :src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`" alt="" width="250px" height="350px">
          </div>
        </div>

        <div class="distance_card">
        <p>영화  <span>&lt;{{movie.title}}&gt;</span>의 대표적인 촬영지인 {{item.data.location_country}}
          {{item.data.location_name}}은 
          나로부터 {{ item.distance_from_me | metersToKilometers }} km 만큼 떨어져 있습니다.</p>
        <!-- {{ movie }} -->
        <!-- <p>location id {{item.data}}</p> -->
        </div>
      </div>


    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'RecommendItem',
  props:{
    item:Object,
  },
  data(){
    return{
      movie:null,
    }
  },
  filters: {
    metersToKilometers(value){
      // 미터(m)를 킬로미터(kliometer)로 변환
      return (value/1000).toFixed(2);
    }
  },
  methods:{
    getMovie(){
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/v1/movie/${this.item.data.tmdb_id}/`
      })
      .then((res)=>{
        console.log(res);
        this.movie = res.data
      })
      .catch((err)=>{
        console.log(err);
      })
    },
  },
  created(){
      this.getMovie()
  },
}
</script>

<style scoped>
.recommend_card {
  overflow: visible;
  width: 250px;
  height: 350px;
  margin: 30px;
}

.content {
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 300ms;
  box-shadow: 0px 0px 10px 1px #000000ee;
  border-radius: 5px;
}

.front, .back {
  background-color: #151515;
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: 5px;
  overflow: hidden;
}

.back {
  width: 100%;
  height: 100%;
  justify-content: center;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.back::before {
  position: absolute;
  content: ' ';
  display: block;
  width: 160px;
  height: 150%;
  background: linear-gradient(90deg, transparent, #ff9966, #ff9966, #ff9966, #ff9966, transparent);
  animation: rotation_481 5000ms infinite linear;
}

.back-content {
  position: absolute;
  width: 99%;
  height: 99%;
  background-color: #151515;
  border-radius: 5px;
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 30px;
}
.back-content img {
  background-size: cover;
}

.recommend_card:hover .content {
  transform: rotateY(180deg);
}

@keyframes rotation_481 {
  0% {
    transform: rotateZ(0deg);
  }

  0% {
    transform: rotateZ(360deg);
  }
}

.front {
  transform: rotateY(180deg);
  color: white;
}

.front .front-content {
  position: absolute;
  width: 100%;
  height: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.front-content .badge {
  background-color: #00000055;
  padding: 2px 10px;
  border-radius: 10px;
  backdrop-filter: blur(2px);
  width: fit-content;
}

.description {
  box-shadow: 0px 0px 10px 5px #00000088;
  width: 100%;
  padding: 10px;
  background-color: #00000099;
  backdrop-filter: blur(5px);
  border-radius: 5px;
}

.title {
  font-size: 11px;
  max-width: 100%;
  display: flex;
  justify-content: space-between;
}

.title p {
  width: 50%;
}

.recommend_card-footer {
  color: #ffffff88;
  margin-top: 5px;
  font-size: 8px;
}

@keyframes floating {
  0% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(10px);
  }

  100% {
    transform: translateY(0px);
  }
}

.distance_card {
  color: white;
  margin-top: 30px;
}
</style>