<template>
  <div>
    
    <div @click="selectThisItem"> <!-- class="item-box" <= 잠깐만 빼놓을게요--> 
      <h3>{{movieitem.movie_id}}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movieitem: Object,
  },
  methods: {
    selectThisItem(){
      // console.log(this.movieitem.movie_id);
      this.$store.dispatch('selectThisItem', this.movieitem.movie_id)
    } 
  }
}
</script>

<style>
.item-box {
  width: 500px;
  height: 30px;
  margin: auto;
  line-height: 30px;
  text-align: center;
}
</style>