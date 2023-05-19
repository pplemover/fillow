<template>
  <div>
    <h1>맨 왼쪽 영화목록</h1>
    <MovieListItem/>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
}
</script>

<style>

</style>