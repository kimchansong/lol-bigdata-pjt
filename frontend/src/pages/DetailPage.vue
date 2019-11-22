<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap>
        <v-flex d-flex xs12 sm6 md6>
          <ChampInfo :name="champName" :id="id"></ChampInfo>
        </v-flex>
        <v-flex d-flex xs12 sm6 md6>
          <ChampBan :name="champName"/>
        </v-flex>
    </v-layout>
  </v-container>
</template>



<script>
import ChampInfo from "../components/ChampInfo.vue"
import ChampBan from "../components/ChampBan.vue"

export default {
  name: 'detailPage',
  props: ["champName","id"],
  
  data: () => ({
      champ: ""
  }),
  components:{
    ChampInfo,
    ChampBan
  }
};
</script>
