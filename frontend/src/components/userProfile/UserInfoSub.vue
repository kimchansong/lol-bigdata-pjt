<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-row>
          <v-container>
              <!-- start : match Info  매치별 검색한 유저 정보 -->
                <v-alert v-if="table"
                    id="valert"
                    outlined
                    color="grey"
                    border="left" 
                >   
                <center>
                    <h1 id="winCheckMessage" class="display-1">{{check_win(userData1.stats.win)}}</h1>
                </center>
                    <v-row>
                        <v-col>
                            <center>
                                <v-avatar size="72">
                                    <img :src="this.champImg+data1[0].id+'.png'"/>
                                </v-avatar>
                            </center>
                            <p class="mt-3 headline" align="center">{{data1[0].name}}({{data1[0].id}})</p>
                        </v-col>
                        <v-col>
                            <!-- 사용자 스펠 추가시 아래 코드 추가 -->
                            <!-- <p class="headline">{{userData1.spell1Id}} {{ userData1.spell2Id}}</p> -->
                            <p class="headline">Level : {{userData1.stats.champLevel}}</p>
                            <p class="headline">K/D/A : {{userData1.stats.kills}}/{{userData1.stats.deaths}}/{{userData1.stats.assists}}</p>
                            <p class="headline">평점 : {{check_kda(userData1.stats.kills, userData1.stats.deaths, userData1.stats.assists)}}</p>
                        </v-col>
                    </v-row>
                </v-alert>
                <!-- end : match info -->
          </v-container>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>
 
 
<script>
import axios from "axios";
const apiUrl = "/api";
export default {
    data () {
        return {
            table: false,
            data1 : "",
            userData1: {},
            info : [],
            user : {},
            winCheck : "",
            champImg: "https://ddragon.leagueoflegends.com/cdn/9.20.1/img/champion/"
        }
    }, 
    props:{
        champNum: { type: Number },
        userNum : { type: Number },
        userData: { type: Array },
        index : { type : Number }
    },
    watch: {
        index: function(newVal, oldVal) {
            this.convertName(newVal)
            console.log(this.winCheck)
           
        }
    },
    methods : { 
        async convertName(id, userNum) {    // 챔피언 숫자값 -> 이름으로 변경
            await axios.get(`${apiUrl}/lol-champion-list/?key=`+id)
                .then(response => {
                this.info = response.data;
            })
            this.data1 = this.info
            this.userData1 = this.userData[userNum]
            this.table = true;           
        },
        check_win(winOrLose){   //승리 여부 글자 반환
            if(winOrLose){
                // 글자 색 변경 코드
                // document.getElementById("winCheckMessage").style.color = "red";
                return "승리"
            }else{
                return "패배"
            }
        },
        check_kda( kill , death , assists ) {   // kda 계산
            return ((kill+assists)/death).toPrecision(2);
        }
    },
    created() {
        this.convertName(this.champNum, this.userNum)
        
    },
}
</script>
