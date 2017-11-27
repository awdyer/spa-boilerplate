// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import ElementUI from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en';
import router from './router';
import store from './store';
import auth from './services/auth';
import api from './services/api';

import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false;

Vue.use(ElementUI, { locale });

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    template: '<App/>',
    components: { App }
});

auth.init(store, router);
api.init(store);
