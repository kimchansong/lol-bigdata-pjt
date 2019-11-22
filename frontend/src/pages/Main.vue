<template lang="html">
  <!-- <v-app id="app"> -->
  <div>

    <Search/>
    <ChampsInfo/>

  </div>
  <!-- </v-app> -->
</template>

<script>
import Search from "../components/func/search"
import ChampsInfo from "../components/ChampsInfo"

export default {
  components: {
    Search,
    ChampsInfo
  },
  data() {
    return {
      id: 1,
      url : ""
    }
  },
}
</script>

<style scoped>
/* #app {
  background-image : url('https://lolstatic-a.akamaihd.net/frontpage/apps/prod/kaisa-reveal/en_US/4b3ba0751b18398c0fe8d339207ba00a26309de1/assets/downloads/wallpapers/kaisa-1280x1024.jpg');
  background-repeat : no-repeat;
  background-size : cover;
} */
</style>