<template>
<v-container>
    <v-layout>
        <v-flex>
            <v-row>
                <!-- start : userInfo table 유저 정보 테이블-->
                <v-container v-if="table">
                    <v-card class="mx-auto" outlined dark>
                        <v-list-item three-line>
                            <v-list-item-avatar tile size="80" color="grey">
                                <img id="profileImg" :src="profileImg" />
                            </v-list-item-avatar>
                            <v-list-item-content>
                            <v-list-item-title class="headline mb-1">{{profile.name}}</v-list-item-title>
                            <p class="title">Level : {{profile.summonerLevel}}</p>
                            </v-list-item-content>
                        </v-list-item>
                    <!-- <v-card-actions>
                    <v-btn @click="reset()" text>Button</v-btn>
                    </v-card-actions> -->
                    </v-card>
                <!-- end : userInfo table -->
                </v-container>
            </v-row>
        </v-flex>
    </v-layout>

</v-container>
</template>
 
 
<script>
export default {
    data () {
        return {
            profile : {
                //summonerLevel, profileIconId
            },
            info : {
                //summonerName, tier, wins, losses, rank, leaguePoints
            },
            table : false,
            imgUrl: "http://ddragon.leagueoflegends.com/cdn/9.20.1/img/profileicon/",
            profileImg : "",
        }
    },
    methods : {},
    props : {
        userProfile : { type : Object },
    },
    watch :{
        userProfile: function(newVal, oldVal) {
            this.profile = newVal,
            this.profileImg = this.imgUrl + newVal.profileIconId + ".png"
            this.table =true;
        },
    }
}
</script>
