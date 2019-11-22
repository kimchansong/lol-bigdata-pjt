<template>
    <v-container id="background">
        <v-layout>
            <v-flex>
                <!-- 챔피언 분석 컴포넌트 -->
                <v-row>
                  <v-card color="rgb(46, 12, 92)" class="mx-auto" min-width="100%">
                    <v-card-title class="text-center justify-center py-6">
                        <h3 class="font-weight-bold display-9 white--text">{{name}} ({{id}})</h3>
                    </v-card-title>
                    <!-- 캐릭터 정보 -->
                    <div>
                        <v-list-item>
                          <span><img id="border1" :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+ id +'.png'"/></span>
                          <span id="sSize">
                            종족 : {{title}}
                            <br />
                            태그 : {{tags}}
                            <br />
                            공격데미지 : {{attackdamage}}
                            <br />
                            사거리 : {{range}}

                          </span>
                          <!-- <v-img src="//opgg-static.akamaized.net/images/lol/champion/Garen.png?image=w_80&v=1"></v-img> -->
                        </v-list-item>
                        <br/>
                        <v-list-item>
                          <div id="Ttext" class="text1">{{desc}}</div>
                          <div @click="plus"><v-icon color="yellow">mdi-chevron-double-down</v-icon></div>
                        </v-list-item>
                    </div>
                    <!-- Top mid jungle 탭 -->
                    <br />
                    <v-tabs
                    v-model="tab"
                    background-color="#595bb8"
                    color="white"
                    grow
                    >
                    <v-tab
                    v-for="item in items"
                    :key="item"
                    >
                    {{ item }}
                    </v-tab>
                    </v-tabs>
                    <!-- 리스트 출력 // 아이템 빌드 , 룬 세팅 등-->
                    <v-tabs-items v-model="tab">
                      <v-tab-item
                          v-for="item in items"
                          :key="item"
                      >
                          <v-card flat color="white">
                          <v-card-text>{{ text }}</v-card-text>
                          </v-card>
                      </v-tab-item>
                      <v-data-table
                          :headers="headers"
                          :items="contents"
                          class="elevation-1"
                          hide-default-footer
                      >
                        <template v-slot:item.img="{ item }">
                          <v-list-item-avatar class="avatar">
                            <img :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/item/'+item.image+'.png'"/>
                          </v-list-item-avatar>
                        </template>
                      </v-data-table>

                    </v-tabs-items>
                  </v-card>
                </v-row>
            </v-flex>
            <div>
            </div>
        </v-layout>
    </v-container>
</template>



<script>
import axios from "axios";
const apiUrl = "/api"

export default {
  data: () => ({
      tab: null,
      items: [
        'Top', 'Mid', 'Bot', 'Jungle',
      ],
      text: '포지션별 통계 정보( 기준 : 5:5 랭크 중 상위권 경기 )',
      headers: [
        {
          text: 'Item build',
          align: 'left',
          sortable: false,
          value: 'number',
        },
        { text: '템트리' , value: 'img'},
        { text: 'Pick Rate (%)', value: 'pickRate' },
        { text: '이름', value: 'name' }
      ],
      headers_2: [
        {
          text: 'Rune Setting',
          align: 'left',
          sortable: false,
          value: 'number',
        },
        { text: 'img' , value: 'image'},
        { text: 'Pick Rate (%)', value: 'pickRate' },
        { text: '이름', value: 'name' }
      ],
      contents: [
      ],
      info:[],
      item_info:[],
      item_name:[],
      title: "",
      tags: "",
      desc: "",
      attackdamage: "",
      range:"",
      key : ""

  }),
  props:{
    name : { type: String },
    id : {type:String}
  },
  methods: {
    async dataInfo(){
      await axios.get(`${apiUrl}/lol-champion-list/?name=`+this.name)
      .then(response => (this.info=response.data))
      // console.log(this.info)
      this.title = this.info[0].title
      this.tags = this.info[0].tags
      this.desc = this.info[0].blurb
      this.attackdamage = this.info[0].attackdamage
      this.range = this.info[0].attackrange
      this.key = this.info[0].key
      // console.log(this.key)
      await axios.get(`${apiUrl}/lol-item-list/?char_id=`+this.key)
      .then(response => (this.item_info=response.data))
      // console.log(this.item_info)
      var total_cnt=0
      for(let i=0; i<10; i++){
        total_cnt+=this.item_info[i].item_cnt
      }
      for(let i=0; i<10; i++){
        var tem_id = (this.item_info[i].item_cnt/total_cnt)*100
        var tem_id2 = this.item_info[i].item_id
        if (tem_id >= 100)
          tem_id = 100
        
        await axios.get(`${apiUrl}/lol-item-name-list/?key=`+tem_id2)
        .then(response => (this.item_name=response.data))
        let name1 = this.item_name[0].name
        this.contents.push({number : i+1, image: tem_id2, pickRate :tem_id.toFixed(2)+'%', name:name1 })
      }
      // console.log(this.contents)
      // console.log(this.contents[0].image)
    },
    plus() {
    }
  },
  created() {
    this.dataInfo()
  }
};
</script>
<style>
.avatar {
    left: 16px;
    top: 0;
    width: 180px;
    height: 180px;
}
#Ttext {
  /* color: #595bb8 !important; */
  color: white;
}
#sSize {
  padding : 30px;
  color: white;
}
#border1 {
  border: 3px solid white;
}
.basil--text{
  color:white !important;
}
.text1 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

</style>
