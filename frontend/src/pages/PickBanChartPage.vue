<template>
    <v-container>
        <v-layout>
            <v-flex>
                <!-- 추천 픽 컴포넌트 -->
                <v-card class="mx-auto" min-width="80%">
                    <v-container class="pa-2" fluid>
                        <v-app-bar color="rgb(46, 12, 92)">
                            <h3 class="font-weight-bold display-9" id="color1">전략 분석</h3>
                        </v-app-bar>
                    <v-row>
                        <v-col>
                            <v-hover v-slot:default="{ hover }">
                                <v-card dark :elevation="hover ? 12 : 2">
                                    <v-card-title>
                                        캐릭터 Ban vs Pick
                                    </v-card-title>
                                    <v-list-item three-line>
                                        <PickAndBan/>
                                    </v-list-item>
                                </v-card>
                            </v-hover>
                        </v-col>
                        <v-col>
                            <v-hover v-slot:default="{ hover }">
                                <v-card dark :elevation="hover ? 12 : 2">
                                    <v-card-title>
                                        캐릭터 아이템 Pick
                                    </v-card-title>
                                    <v-list-item three-line>
                                        <itemPick/>
                                    </v-list-item>
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
import PickAndBan from '../components/Analysis'
import itemPick from '../components/ItemChart'
export default {
    components:{
        PickAndBan,
        itemPick,
    }
};
</script>
<style>
#color1 {
  color: white;
}
</style>
