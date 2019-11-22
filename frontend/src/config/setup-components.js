// Core Components

import Widget from '../components/Widget.vue';
import UserProfile from '../components/userProfile/UserProfile.vue';
import RankedInfo from '../components/userProfile/RankedInfo.vue';
import MatchInfo from '../components/userProfile/MatchInfo.vue';
import PieChart from '../components/chart/PieChart.vue';
import UserInfoSub from '../components/userProfile/UserInfoSub';


function setupComponents(Vue){
  // widget : test page 테스트가 필요한 곳에 사용
  Vue.component('widget', Widget);
  // userProfile : 유저 프로필 아이콘 , 레벨 등이 노출됨
  Vue.component('userProfile', UserProfile)
  // rankedInfo : 유저 티어 정보 노출됨
  Vue.component('rankedInfo', RankedInfo)
  // matchInfo : 매 경기마다 최종아이템 및 참여자 정보 노출됨
  Vue.component('matchInfo', MatchInfo)
  // pieChart : 솔로 랭크 승률 도넛 그래프로 노출됨
  Vue.component('pieChart', PieChart)
  // userInfoSub : 매 경기 검색자의 캐릭터, 레벨, kda, 사용 스펠 등이 노출됨
  Vue.component('userInfoSub', UserInfoSub)
}


export {
  setupComponents
}
