import 'bootstrap/dist/css/bootstrap.css';
import Antd from 'ant-design-vue';
import Icon from '@ant-design/icons';
import 'ant-design-vue/dist/antd.css';
import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js'


Vue.config.productionTip = false
Vue.use(Antd);

new Vue({//实例
  router,
  render: h => h(App)
}).$mount('#app')

