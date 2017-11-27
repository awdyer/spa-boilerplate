import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Register from '@/components/Register';
import RegisterConfirm from '@/components/RegisterConfirm';
import SignIn from '@/components/SignIn';
import Protected from '@/components/Protected';
import NotFound from '@/components/NotFound';
import Account from '@/components/Account';

Vue.use(Router);

export default new Router({
    // mode: 'history',
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/register',
            component: Register,
            meta: {
                auth: false
            }
        },
        {
            path: '/registerconfirm',
            component: RegisterConfirm,
            meta: {
                auth: false
            }
        },
        {
            path: '/signin',
            component: SignIn,
            meta: {
                auth: false
            }
        },
        {
            path: '/protected',
            component: Protected,
            meta: {
                auth: true
            }
        },
        {
            path: '/account',
            component: Account,
            meta: {
                auth: true
            }
        },
        {
            path: '*',
            component: NotFound
        }
    ]
});
