<template>
  <v-container fluid>
    <v-form>
      <v-row align="end" justify="center">
        <v-col cols="12" sm="6">
          <v-combobox
            outlined
            dark
            id="fieldColor"
            color="white"
            :items="champDropList"
            label="소환사명을 입력하세요"
            v-model="value"
            @keyup.enter="btnEnter()"
          ></v-combobox>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      champDropList: [],
      champList: [],
      value: ""
    };
  },
  methods: {
    btnEnter() {
      var champName = this.value;
      var id;
      var list = this.$store.getters.getChampList;
      for (let i = 0; i < list.length; i++) {
        if (champName === list[i].name) {
          id = list[i].id;
          break;
        }
      }

      this.$router.push({ name: "detail", params: { champName, id }});
    }
  },
  created() {
    //eventbus 를 통해 header에서 챔피언리스트 변경이 감지될 경우 챔피언 리스트 갱신
    this.EventBus.$on("send", res => {
      this.champList = res;
      this.champDropList = this.$store.getters.getChampDropList;
    });
    this.champDropList = this.$store.getters.getChampDropList;
  }
};
</script>
<style>
#fieldColor {
  color: antiquewhite;
}
</style>
