<template>
<div style="margin: auto; padding:7px;">
  <center>
    <img id="border1" :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+ this.bot[0] +'.png'" class=mr-2>
    <img id="border1" :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+ this.bot[1] +'.png'">
    <br />
    <v-btn @click="click">확인</v-btn>
    <v-btn @click="back">돌아가기</v-btn>
    <br />
    <center id="result">
      <transition name="bounce">
        <div v-if="this.resultdata[0]=='bad'" id="bad">
          <p>
            BAD
            <br />
            추천하진 않는 조합입니다.
          </p>
        </div>
        <div v-if="this.resultdata[0]=='good'" id="ok">
          GOOD
          <br />
          쓸만한 조합이네요!!
        </div>
      </transition>
    </center>

    <br />
    <img id="border1" :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+ this.bot[0] +'.png'" class=mr-2>
    <div id="info">
      {{this.title1}}
      {{this.tags1}}
    </div>
    <!-- 두번째케릭 -->
    <img id="border1" :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+ this.bot[1] +'.png'" class=mr-2>
    <div id="info">
      {{this.title2}}
      {{this.tags2}}
    </div>



  </center>

</div>
</template>

<script>
import axios from "axios"
const apiUrl = "/api"


import Vue from 'vue'
import Vuetify from 'vuetify/lib'


export default {

  created() {
    // this.EventBus.$on("namegogo", res => {
    //     console.log("here is my code : ")
    //     this.bot = res;
    //     console.log("---------------------" + this.bot)

    //   }),
      this.bot = this.$store.getters.getBot;
  },

  data() {
    return {
      bot: [],
      bot1: 0,
      bot2: 0,
      result: "",
      champdata: [],
      title1: "",
      tags1: "",
      title2: "",
      tags2: "",
      resultdata:[]
    }
  },
  methods: {

    async back() {
      this.$router.push("/")
    },
    async click() {
      await axios.get(`${apiUrl}/lol-champion-list/`)
        .then(response => (this.champdata = response.data))

      for (var i in this.champdata) {
        if (this.champdata[i].id == this.bot[0]) {
          this.bot1 = this.champdata[i].key
          this.title1 = this.champdata[i].title
          this.tags1 = this.champdata[i].tags
        }
        if (this.champdata[i].id == this.bot[1]) {
          this.bot2 = this.champdata[i].key
          this.title2 = this.champdata[i].title
          this.tags2 = this.champdata[i].tags
        }
      }
      await axios.get(`${apiUrl}/lol-lolgating-list?bot1=${this.bot1}&bot2=${this.bot2}`)
        .then(response => (this.result = response.data))
      this.resultdata = this.result
      console.log(this.bot1, this.bot2, this.resultdata[0], "check")
      console.log(this.resultdata[1])
    }
  },

}
</script>
<style>
#ok {
  color: blue;
}
#bad {
  color: red;
}
#result {
  font-family: times;
  font-weight: bold;
  font-size: 4em
}
#info {
  background-color: gray;
}

#border1 {
  border: 3px solid white;
}


.bounce-enter-active {
  animation: bounce-in .5s;
}

.bounce-leave-active {
  animation: bounce-in .5s reverse;
}

@keyframes bounce-in {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.5);
  }

  100% {
    transform: scale(1);
  }
}
</style>
