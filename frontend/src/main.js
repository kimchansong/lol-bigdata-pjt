import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'
import { setupComponents } from './config/setup-components';

Vue.config.productionTip = false
Vue.prototype.EventBus = new Vue();
setupComponents(Vue);

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
