<template>
<v-container>
    <v-layout>
        <v-flex>
            <v-row>
                <!-- tier talbe 유저 티어 정보 -->
                <v-container v-if="table">
                    <v-card class="mx-auto" outlined dark>
                        <v-list-item three-line>
                            <v-list-item-content>
                            <v-list-item-title><h2>솔로랭크</h2></v-list-item-title>
                               
                                 <v-row>
                                    <v-col>
                                        <div class="overline mb-4">{{rankSolo.tier}} {{rankSolo.rank}}</div>
                                        <v-list-item-subtitle><h3>승 : {{rankSolo.wins}} / 패 : {{rankSolo.losses}}</h3></v-list-item-subtitle>
                                        <v-list-item-subtitle><h3 class=".font-italic">승률 : {{checkWinRate(rankSolo.wins,rankSolo.losses)}}</h3></v-list-item-subtitle>
                                        </v-col>
                                    <v-col>
                                        <img style="width:100px; height:100px" :src="'./assets/'+rankSolo.tier+'.png'"/>
                                    </v-col>
                                </v-row>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>

                    <v-card class="mx-auto mt-3" outlined v-if="freeTable" dark>
                        <v-list-item three-line>
                            <v-list-item-content>
                                <v-list-item-title><h2>자유 5:5 랭크</h2></v-list-item-title>
                                <v-row>
                                    <v-col>
                                        <div class="overline mb-4">{{rankFree.tier}} {{rankFree.rank}}</div>
                                        <v-list-item-subtitle><h3>승 : {{rankFree.wins}} / 패 : {{rankFree.losses}}</h3></v-list-item-subtitle>
                                        <v-list-item-subtitle><h3>승률 : {{checkWinRate(rankFree.wins,rankFree.losses)}}</h3></v-list-item-subtitle>
                                    </v-col>
                                    <v-col>
                                        <img style="width:100px; height:100px" :src="'./assets/'+rankFree.tier+'.png'"/>
                                    </v-col>
                                </v-row>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card>
                </v-container>
                <!-- end : tier table -->
            </v-row>
        </v-flex>
    </v-layout>
</v-container>
</template>
 
 
<script>
export default {
    name : "rankedInfo",
    data () {
        return {
            rank: {
                //wins, losses, tier, summonerId, summonerName
            },
            rankFree : [],  // 5x5 자유 랭크 
            rankSolo : [],  // 솔로 랭크
            table: false,   // 솔로 랭크 테이블
            freeTable : false, // 자유 랭크 테이블
        }
    },
    methods: {
        checkWinRate(wins, losses) {    // 승률 퍼센트로 변환
            var totalgames = wins + losses;
            return ((wins / totalgames) * 100).toPrecision(2);
        },
        create_item_img(item_img) {     // 티어 이미지 정보 설정
            console.log(item_img)
            let url = "@/assets/" + item_img + ".png";
            return url;
        },
    },
    props : {
        rankInfo : { type : Array },
    },
    watch :{ 
        rankInfo: function(newVal, oldVal) { // solo 랭크만 할경우 5x5는 false
            this.freeTable = false;
            this.rankSolo = this.rankInfo[0]
            if(newVal.length===2){
                this.rankFree = this.rankInfo[1]
                this.freeTable = true;
            }
            this.table = true;
        }
    }
}
</script>
<style>
</style>