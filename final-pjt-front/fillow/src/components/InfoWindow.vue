<template>
  <div>

    <h1>infowindow</h1>
    {{movieLocationItem}}
    <img :src="movieLocationItem.location_photo_url" alt="" width="200px" height="150px">

  </div>
</template>

<script>
export default {
  name:'InfoWindow',
  props: {
    movieLocationItem: Object,
  },
}
</script>

<style>

</style>