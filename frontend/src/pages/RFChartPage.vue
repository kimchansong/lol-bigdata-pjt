<template>
    <v-container>
        <v-layout>
            <v-flex>
                <!-- 추천 픽 컴포넌트 -->
                <v-card class="mx-auto" min-width="80%" id= "height_control">
                    <v-container class="pa-2" fluid>
                        <v-app-bar color="rgb(46, 12, 92)">
                            <h3 class="font-weight-bold display-9" id="color1">오브젝트 컨트롤에 따른 승/패 분석</h3>
                        </v-app-bar>
                    <v-row class="mt-5 pt-5">
                        <v-card class="mx-auto my-auto" min-width="85%">
                      <v-hover v-slot:default="{ hover }" id= "height_control2" >
                          <v-card color="rgb(115, 115, 115)" :elevation="hover ? 12 : 2">
                              <v-list-item three-line style="color:white!important">
                                  <Randomforest/>
                              </v-list-item>
                          </v-card>
                      </v-hover>
                      </v-card>
                    </v-row>
                    </v-container>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>


<script>

import Randomforest from '../components/Randomforest'
export default {
    components:{

        Randomforest
    }
};
</script>
<style>
#color1 {
  color: white;
}

#height_control{
    height:100vh
}
#height_control2{
    height:70vh
}
</style>
