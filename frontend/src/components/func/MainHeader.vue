<template>
  <div id="header">
    <div>
      <v-toolbar style="background:#444444; opacity: 0.5;">
        <v-toolbar-title id="fontColor" >LOL 개팅</v-toolbar-title>

        <div class="flex-grow-1"></div>
        <v-toolbar-items>
          <v-btn text id="fontColor" to="/">홈</v-btn>
          <!-- <v-btn text id="fontColor" to="/lolting">롤개팅</v-btn> -->
          <v-btn text id="fontColor" to="/analysis">전략분석</v-btn>
          <v-btn text id="fontColor" to="/rfchartPage">승패분석</v-btn>
          <v-btn text id="fontColor" to="/findUserPage">유저</v-btn>
        </v-toolbar-items>

        <template v-if="$vuetify.breakpoint.smAndUp">
          <v-btn icon>
            <v-icon color=white>mdi-export-variant</v-icon>
          </v-btn>
          <v-btn icon color=white>
            <v-icon>mdi-delete-circle</v-icon>
          </v-btn>
          <v-btn icon color=white>
            <v-icon>mdi-plus-circle</v-icon>
          </v-btn>
        </template>
      </v-toolbar>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const apiUrl = '/api'
export default {
  data(){
    return{
      champNames: [],
      champ: [],
      info: []
    }
  },
  methods:{},
  created(){
      this.$store.dispatch('getChampName')
  }
}
</script>
<style>
#fontColor {
  color: white;
}
</style>
