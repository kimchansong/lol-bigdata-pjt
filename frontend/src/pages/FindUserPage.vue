<template>
<v-container fluid grid-list-xl>
    <v-flex>
        <v-row>
        <v-col>
            <!-- start : search bar (검색바) // 유저 검색-->
            <v-layout>
                <v-text-field
                dark
                v-model="userId"
                label="Outlined"
                outlined
                color="pink"
                clearable
                @keyup.enter = "btnEnter"
                ></v-text-field>
            </v-layout>
            <!-- end : search bar -->

            <!-- 광고 자리 -- >
            <!-- <v-layout row wrap>
                <v-flex d-flex>
                    <widget title="AD" subTitle= '광고 넣을 자리' supTitle="Today's Visits" color="#00b297"/>
                </v-flex>
            </v-layout> -->

            <!-- start : userInfo  유저 정보 출력--> 
            <v-layout row wrap>
                <v-card class="mx-auto mt-3" outlined dark v-if="userTable">
                    <v-progress-circular indeterminate color="white" :width="4" size="70" v-if="loading"/>
                    <v-row>
                        <v-col>
                            <v-flex d-flex>
                                <userProfile :userProfile="this.info.userProfile" :userInfo="this.info.userInfo"></userProfile>
                            </v-flex>
                        </v-col>
                        <v-col>
                            <v-list-item-content>
                                <pieChart :wins="this.wins" :losses="this.losses" :summonerName="this.summonerName"></pieChart>
                            </v-list-item-content>
                        </v-col>
                    </v-row>
                </v-card>
                <v-flex d-flex>
                    <rankedInfo :rankInfo="this.info.userInfo"></rankedInfo>
                </v-flex>
            </v-layout> 
            <!-- end : userInfo -->

        </v-col>
        <v-col>
            <!-- start : matchList  최근 전적 검색 -->
            <v-layout>
                <v-flex d-flex>
                    <matchInfo :matchInfo="this.info.matchList" :summonerName="this.summonerName" ></matchInfo>
                </v-flex>
            </v-layout>
            <!-- end : matchList -->

        </v-col>
        </v-row>
    </v-flex>        
</v-container>
</template>

<script>
import axios from "axios";
const apiUrl = "/api";

export default {
    name: 'findUserPage',
    data() {
        return {
            userId : "중소기업김대표",  //검색아이디- search bar 현재입력값
            userTable : false,  //유저정보 테이블 switch용
            summonerName : "",  //검색아이디- 저장값(enter 키 누를 시)
            loading : true,     //loading bar 검색시 로딩바
            wins : 0,           //승률 차트 승리 정보
            losses : 0,         //승률 차트 패배 정보
            info : { 
                //matchList : 최근 3경기 매치 정보 
                //userInfo : 랭크, 승패, id, rankgame 정보
                //userProfile : level, 프로필 아이콘
            },
        }
    },
    components : {
    },
    methods : {
        btnEnter() { // 유저 검색 엔터 키 누를 경우 이벤트
            this.loading = true;
            this.userTable = true;
            this.getUserInfo(this.userId);
        },
        async getUserInfo(userId){  // api로 유저 정보 검색
            await axios.get(`${apiUrl}/lol-user-info/?key=`+userId)
            .then(response => (this.info = response.data));
            console.log(this.info)
            this.summonerName = this.info.userProfile.name;
            this.wins = this.info.userInfo[0].wins;
            this.losses = this.info.userInfo[0].losses;
            this.loading = false;
            
        }
    },
    created() {
        this.EventBus.$on("send", res => {this.btnEnter();});
    }
}
</script>
<style>
</style>
