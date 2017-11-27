import axios from 'axios';

export default {
    init,
    doSomethingDangerous
};

function init(store) {
    // axios.defaults.baseURL = 'http://localhost:6001';
    axios.defaults.baseURL = 'https://7acxxqof9g.execute-api.ap-southeast-2.amazonaws.com/dev';

    axios.interceptors.request.use(config => {
        // If user is logged in, send access token in Authorization header
        const user = store.state.cognito.user;
        if (user) {
            config.headers['Authorization'] = 'Bearer: ' + user.tokens.AccessToken;
        }

        return config;
    })
}

function doSomethingDangerous() {
    return axios.get('/protected');
}
