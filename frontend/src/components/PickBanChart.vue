<template>
    <v-container>
        <v-layout>
            <v-flex>
                <v-card class="mx-auto" min-width="80%">
                    <v-container class="pa-2" fluid>
                        <v-app-bar color="rgb(46, 12, 92)">
                            <h3 class="font-weight-bold display-9" id="color1">캐릭터별 Ban vs Pick</h3>
                        </v-app-bar>
                    <v-row> 
                        <v-col>
                            <v-hover v-slot:default="{ hover }">
                                <v-card dark :elevation="hover ? 12 : 2">
                                    <v-list-item three-line>
                                    <!-- <v-list-item-content class="align-self-start">
                                        <v-list-item-title
                                        class="mb-4"
                                        v-text="item.title"
                                        ></v-list-item-title>

                                        <v-list-item-subtitle v-text="item.champInfo"></v-list-item-subtitle>
                                    </v-list-item-content>

                                    <v-list-item-avatar
                                        size="100"
                                        tile
                                    >
                                        <v-img :src="item.src"></v-img>
                                    </v-list-item-avatar> -->
                                    
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
export default {
  data: () => ({
    items: [
        {
            color: 'basil',
            src: '//opgg-static.akamaized.net/images/lol/champion/Yasuo.png',
            title: '챔피언 이름',
            champInfo: '챔피언 설명이 들어갈곳',
        }
    ],
  }),
  components:{
  },
  methods: {
  },
};
</script>
<style>
#color1 {
  color: white;
}
</style>