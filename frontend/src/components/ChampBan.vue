<template>
    <v-container>
        <v-layout>
            <v-flex>
                <!-- 추천 픽 컴포넌트 -->
                <v-card class="mx-auto" min-width="100%">
                    <v-container class="pa-2" fluid>
                        <v-app-bar color="rgb(46, 12, 92)">
                            <h3 class="font-weight-bold display-9" id="color1">Ban Pick</h3>
                        </v-app-bar>
                    <v-row> 
                        <v-col v-for="(item, i) in items" :key="i" style="min-width:100%">
                            <v-hover v-slot:default="{ hover }">
                                <v-card dark :elevation="hover ? 12 : 2">
                                    <v-list-item three-line>
                                    <v-list-item-content class="align-self-start">
                                        <v-list-item-title
                                        class="mb-4"
                                        v-text="item.char_name"
                                        ></v-list-item-title>

                                        <v-list-item-subtitle v-text="item.title"></v-list-item-subtitle>
                                        <v-list-item-subtitle v-text="item.tags"></v-list-item-subtitle>
                                        <v-list-item-subtitle v-text="item.range"></v-list-item-subtitle>
                                        <v-list-item-subtitle v-text="item.damage"></v-list-item-subtitle>
                                        
                                    </v-list-item-content>
                                    <h1 v-text="item.percent"></h1>
                                    <v-list-item-avatar
                                        size="100"
                                        tile
                                    >
                                        <v-img :src="item.src"></v-img>
                                    </v-list-item-avatar>
                                    </v-list-item>
                                    <!-- <v-card-actions>
                                    <v-btn text color="red">event button</v-btn>
                                    </v-card-actions> -->
                                </v-card>
                            </v-hover>
                        </v-col>
                    </v-row>
                    </v-container>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>


<script>
import axios from "axios";
const apiUrl = "/api"

export default {
    data: () => ({
        items: [],
        info:[]
    }),
    methods: {
        async dataInfo(){
            await axios.get(`${apiUrl}/lol-ban-count-list/?name=`+this.name)
            .then(response => (this.info=response.data))
            var len = this.info.length

            var total = 0
            for(let i=0; i<len; i++){
                if(this.info[i].name==this.name){
                    total+=this.info[i].cnt
                }
            }
            console.log(total)
            if(len<6){
                for(let i=0; i<len; i++){
                    var id = this.info[i].ban_char_id
                    var name1=""
                    await axios.get(`${apiUrl}/lol-champion-list/?key=`+id)
                    .then(response => (name1=response.data))
                    var name2 = name1[0].name
                    var title = "종족 : "+name1[0].title
                    var tags = "태그 : "+name1[0].tags
                    var range = "사거리 : "+name1[0].attackrange
                    var name3 = name1[0].id
                    var damage = "공격데미지 : "+name1[0].attackdamage
                    var desc = name1[0].blurb
                    var src = "//opgg-static.akamaized.net/images/lol/champion/"+name3+".png"
                    var percent = (i+1)+"위: "+((this.info[i].cnt/total)*100).toFixed(2)+" %"
                    this.items.push({desc:desc, percent:percent, char_name:name2, src: src, title:title, tags:tags, range:range, damage:damage})
                }
            }else{
                var idx=1
                for(let i=0; i<6; i++){
                    var id = this.info[i].ban_char_id
                    // console.log(id)
                    if(id!=-1){
                        var name = ""
                        await axios.get(`${apiUrl}/lol-champion-list/?key=`+id)
                        .then(response => (name1=response.data))
                        var name2 = name1[0].name
                        var title = "종족 : "+name1[0].title
                        var tags = "태그 : "+name1[0].tags
                        var range = "사거리 : "+name1[0].attackrange
                        var name3 = name1[0].id
                        var damage = "공격데미지 : "+name1[0].attackdamage
                        var desc = name1[0].blurb
                        var src = "//opgg-static.akamaized.net/images/lol/champion/"+name3+".png"
                        var number = ((this.info[i].cnt/total)*100).toFixed(2)
                        if(number>=100){
                            number = 100
                        }
                        var percent = (idx)+"위: "+number+" %"
                        idx++
                        this.items.push({desc:desc, percent:percent, char_name:name2, src: src, title:title, tags:tags, range:range, damage:damage})
                    }
                }
            }
        }
    },
    created(){
        this.dataInfo()
    },
    props:{
        name : { type: String }
  },
};
</script>
<style>
#color1 {
  color: white;
}
</style>
