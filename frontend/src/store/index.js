import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
const apiUrl = '/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    champList : {},
    champDropList : [],
    bot : [],
  },
  getters: {
    //챔피언 리스트 불러오기
    getChampList(state) {
      return state.champList;
    },
    getChampDropList(state) {
      return state.champDropList;
    },
    getBot(state) {
      return state.bot;
    }
  },
  // actions
  actions: {
    async getChampName({ commit }){
      var info = new Object();
      await axios.get(`${apiUrl}/lol-champion-list/`)
      .then(response => (this.info=response.data))
      commit("setChampList", this.info)
      var len = this.info.length
      var champInfo = [len-1];
      for(var i=0; i<len; i++){
        champInfo[i] = this.info[i].name
      }
      commit("setDropList", champInfo)
    }
  },
  // mutations
  mutations: {
    //챔피언 리스트 설정
    setChampList(state, payload){
      state.champList = payload;
    },
    setDropList(state, payload){
      state.champDropList = payload;
    },
    setBot(state, payload){
      state.bot[0] = payload[0]
      state.bot[1] = payload[1]
    }
  }
})
