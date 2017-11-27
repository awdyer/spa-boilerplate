import Vue from 'vue';
import Vuex from 'vuex';
import config from '../../config/config';
import CognitoAuth from 'vue-auth-cognito';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        cognito: new CognitoAuth(config.aws.cognito)
    }
});
