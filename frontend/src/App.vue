<template>
  <v-app id="app">
    <v-content>
      <MainHeader id="header1"/>
      <router-view />
    </v-content>
    <Footer />
  </v-app>
</template>

<script>
import router from "./router";
import Main from "./pages/Main.vue"
import MainHeader from "./components/func/MainHeader.vue"

export default {
  components:{
    MainHeader,
    Main
  },
  data() {
    return {
      path:""
    }
  },
  mounted() {
    this.path = this.$route.path;
  },
  watch: {
    '$route' : 'setBackground'
  },
  methods: {

    setBackground() { // router 경로별로 background 설정
      console.log(this.$route.path)
      // if(this.$route.path=="/home"){
        document.getElementById('app').style.backgroundImage="url('https://lolstatic-a.akamaihd.net/frontpage/apps/prod/kaisa-reveal/en_US/4b3ba0751b18398c0fe8d339207ba00a26309de1/assets/downloads/wallpapers/kaisa-1280x1024.jpg')"
      // }
      // else if(this.$route.path="/champInfo"){
      //   document.getElementById('app').style.backgroundImage="url('https://vignette.wikia.nocookie.net/leagueoflegends/images/1/1b/Pyke_OriginalSkin.jpg/revision/latest?cb=20181021052139')"
        // document.getElementById('header1').style.backgroundImage="url("+this.background+")"
      // }else{
      //   document.getElementById('app').style.backgroundImage=""
        // document.getElementById('header1').style.backgroundImage="url("+this.background+")"
      // }
    }
  },
  mounted() {
    this.setBackground()
  }
};
</script>
<style>
</style>
