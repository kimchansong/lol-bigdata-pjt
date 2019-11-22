<template>
<v-container>
    <v-layout>
        <v-flex>
            <v-row>
              <!-- start : match info 경기 별 사용자 아이템 및 같이 플레이한 플레이어 출력 -->
                <v-container v-if="table">
                <v-expansion-panels v-model="panel" multiple dark>
                <v-expansion-panel v-for="(match, index) in matchList" :key="match.gameId">
                  <v-expansion-panel-header>
                    <userInfoSub
                      :champNum="match.participants[myNum].championId"
                      :userData="match.participants"
                      :userNum="myNum"
                      :index="index"
                    ></userInfoSub>

                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <v-alert 
                        outlined 
                        color="grey"
                        type="success"
                      >
                        <h5 class="headline">경기시간 : {{secondToMinute(match.gameDuration)}}</h5>
                          <tr>
                            <td>
                              <v-alert text color="info">
                                <h2>최종아이템</h2>
                                <img
                                  :src="create_item_img(match.participants[myNum].stats.item0)"
                                  style="max-width:50px; max-height:50px"
                                />
                                <img
                                  :src="create_item_img(match.participants[myNum].stats.item1)"
                                  style="max-width:50px; max-height:50px"
                                />
                                <img
                                  :src="create_item_img(match.participants[myNum].stats.item2)"
                                  style="max-width:50px; max-height:50px"
                                />
                                <img
                                  :src="create_item_img(match.participants[myNum].stats.item3)"
                                  style="max-width:50px; max-height:50px"
                                />
                                <img
                                  :src="create_item_img(match.participants[myNum].stats.item4)"
                                  style="max-width:50px; max-height:50px"
                                />
                                <img
                                  :src="create_item_img(match.participants[myNum].stats.item5)"
                                  style="max-width:50px; max-height:50px"
                                />
                              </v-alert>
                            </td>
                          </tr>
                          <tr>
                            <td>
                              <div
                                v-for="(member, index) in match.participantIdentities"
                                :key="member.participantId"
                              >
                                <v-row class="mt-1">
                                  <img class="ml-4"
                                    :src="change_img(member.player.profileIcon)"
                                    style="max-width:30px; max-height:30px"
                                  />
                                  <h4 class="ml-1">{{member.player.summonerName}}</h4>
                                </v-row>
                              </div>
                            </td>
                          </tr>
                        </v-alert>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </v-container>
                <!-- end : match info -->
            </v-row>
        </v-flex>
    </v-layout>

</v-container>
</template>
 
 
<script>
export default {
  
    data () {
        return {
            matchList : {},
            userName : "",
            table: false,
            panel: [0],
            myNum: 0,
            img: {
                profileIcon:
                "http://ddragon.leagueoflegends.com/cdn/9.20.1/img/profileicon/"
            },
        }
    },
    methods : {
        secondToMinute(second) {
          let min = (second / 60).toPrecision(4).toString();
          let array = min.split(".");
          return array[0] + "분 " + array[1] + "초";
        },
        myInfo(match) {
            var participantId = null;
            for (var i = 0; i < match.participantIdentities.length; i++) {
                if (this.userName === match.participantIdentities[i].player.summonerName) {
                    participantId = match.participants[i].participantId-1;
                    this.myNum = participantId;
                    return participantId;
                }
            }
        },
        change_img(value) {
            return this.img.profileIcon + value + ".png";
        },
        create_item_img(item_img) {
            if (item_img === 0) {
                return "https://cdn.pixabay.com/photo/2012/04/24/12/29/no-symbol-39767_1280.png";
            } else {
                return (
                    "https://ddragon.leagueoflegends.com/cdn/9.20.1/img/item/" +
                    item_img +
                    ".png"
                    );
            }
        },
    },
    props : {
        matchInfo : { type : Array },
        summonerName : { type : String }
    },
    watch :{ 
        matchInfo: function(newVal, oldVal) {
          this.matchList = newVal
          this.userName = this.summonerName;
          this.table = true;
        }

    }
    
}
</script>
