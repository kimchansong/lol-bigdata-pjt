<template>
    <v-container>
        <v-layout>
            <div style="margin: auto; padding:7px;">
                <center>
                    <img src="../../public/images/QuestionBox.png" id="pickedImage1" class=mr-2>
                    <img src="../../public/images/QuestionBox.png" id="pickedImage2">
                </center>
                <v-col>
                        <v-btn dark outlined class=mr-6
                          v-on:click= "lolgatingGo()"
                          >Lolting</v-btn>
                        <v-btn @click="cancel" dark outlined>Remove</v-btn>
                </v-col>
            </div>
        </v-layout>
        <v-layout id="bg">
            <v-flex>
                <v-progress-circular indeterminate color="primary" v-if="loading"/>
                    <v-container fluid>
                        <v-row>
                            <v-col v-for="champName in champList" :key="champName.id" @click="btnClick(champName.id)">
                            <div class="d-flex flex-column mb-4" style="max-width:120px; max-height:120px">
                                <img :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+champName.id+'.png'"/>
                                <center id="fontColor">{{champName.name}}</center>
                            </div>
                            </v-col>
                        </v-row>
                    </v-container>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios'


const apiUrl = '/api'
export default {
    data() {
        return {
            champList : [],
            bot:[],
            loading: true,
            name: "",
            image1Bool : false,
            iamge2Bool : false,
            bot1:"",
            bot2:"",

        }
    },

    methods: {
        btnClick(champName){
            alert(champName + "을 선택하셨습니다.")
            var img1 = document.getElementById("pickedImage1")
            var img2 = document.getElementById("pickedImage2")

            if(this.image1Bool===false){
                img1.src = "https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/"+ champName + ".png"
                this.bot1 = champName
                this.image1Bool=true;
            }
            else{
                img2.src = "https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/"+ champName + ".png"
                this.bot2 = champName
                this.image2Bool=true;
            }
        },
        cancel(){
            var img1 = document.getElementById("pickedImage1");
            var img2 = document.getElementById("pickedImage2");
            img1.src = "/img/QuestionBox.00304c77.png"
            img2.src = "/img/QuestionBox.00304c77.png"
            this.image1Bool=false;
            this.image2Bool=false;
            this.bot1 = "";
            this.bot2 = "";

        },
        lolgatingGo(){

          if(this.bot1=="" || this.bot2==""){
            alert("챔피언을 두명 선택해 주세요")
            return;
          }

          console.log(this.bot1,this.bot2)
          let array = [this.bot1, this.bot2]
          this.$store.commit("setBot",array)
          this.$router.push("lolgating")

        },

    },
    computed: {
        getN () {   // 챔피언 리스트 변경이 감지되면 리로딩
            return this.$store.getters.getChampList
        }
    },
    watch: {    // 챔피언 리스트 값이 변하는지 확인
        getN (val, oldVal) {
            this.loading = true;
            this.champList = val;
            this.loading = false;
            this.EventBus.$emit("send", this.champList);
        }
    },
    created() {
        this.loading = true;
        this.champList = this.$store.getters.getChampList
        this.loading = false;
    },

}
</script>

<style>
#bg {
    background-color:#071041;
}

#fontColor {
    color:white;
}
</style>
