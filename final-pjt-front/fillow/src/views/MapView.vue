<template>
  <div>

    <gmap-map
        :zoom="3"    
        :center="center"
        style="width:100%;  height: 855px;"
      >
      <gmap-marker
        :key="index"
        v-for="(m, index) in locationMarkers"
        :position="m.position"
      ></gmap-marker>
    </gmap-map>

  </div>
</template>

<script>
export default {
  name: "MapView",
  data() {
    return {
      center: { lat: 37.5642135, lng: 127.0016985 },
      // locationMarkers: [
      //   {
      //     position: { lat: 37.5642135 ,lng: 127.0016985 },
      //   },
      // ],
      locPlaces: [],
      existingPlace: null
    };
  },
  computed: {
    locationMarkers() {
      const MovieLocations = this.$store.state.movieLocations
      // console.log(MovieLocations)
      // console.log(MovieLocations[0].latitude)

      let latlngs = [] 

      for (const MovieLocation of MovieLocations) {
        // console.log('MovieLocation', MovieLocation)
        latlngs.push({position: { lat: parseFloat(MovieLocation.latitude) ,lng: parseFloat(MovieLocation.longitude) },})
        // latlngs.push({position: { lat: MovieLocation.latitude ,lng: MovieLocation.longitude },})
      }
      
      return latlngs
    }
  },
  created() {
    console.log(this.locationMarkers)
  }
};
</script>