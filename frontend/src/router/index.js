import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../pages/Main'
import DetailPage from '../pages/DetailPage'
import Lolting from '../pages/LoltingPage'
import Main from '../pages/Main'
import Lolgating from '../pages/lolgating'
import Analysis from '../pages/PickBanChartPage' 
import FindUserPage from '../pages/FindUserPage'
import RFChartPage from '../pages/RFChartPage'


Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {path:"/", name:"main" ,component: Main},
    {path:"/home", name:"home" ,component: Home},
    {path:"/lolting", name:"loltingPage", component: Lolting},
    {path:"/lolgating", name:"lolgating", component: Lolgating},
    {path:"/analysis", name:"analysis", component: Analysis},
    {path:"/champDetail/:champName/",name:'detail', component: DetailPage, props:true },
    {path:"/findUserPage",name:'findUserPage', component: FindUserPage, props:true },
    {path:"/rfchartPage",name:'rfchartPage', component: RFChartPage, props:true },
    
  ]
})
