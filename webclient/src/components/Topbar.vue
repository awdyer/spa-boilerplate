<template>
<div>
    <div class="pull-right">
        <!-- <router-link v-if="!signedIn" to="register">Register</router-link>
        <router-link v-if="!signedIn" to="signin">Sign in</router-link>
        <a href="#" v-if="signedIn" @click.prevent="signOut">Sign out</a>
        <!-- <router-link to="/">Home</router-link>
        <router-link to="protected">Protected</router-link>
        <router-link to="register">Register</router-link>
        <router-link to="signin">Sign in</router-link>
        <a href="#" @click.prevent="signOut">Sign out</a> -->
    </div>

    <el-menu mode="horizontal" :router="true">
        <el-menu-item index="/">Home</el-menu-item>
        <el-menu-item v-if="signedIn" index="/protected">Protected</el-menu-item>
        <div class="pull-right">
            <el-menu-item v-if="!signedIn" index="/register">Register</el-menu-item>
            <el-menu-item v-if="!signedIn" index="/signin">Sign in</el-menu-item>
            <el-submenu v-if="signedIn" index="#">
                <template slot="title">{{ username }}</template>
                <el-menu-item index="/account">My account</el-menu-item>
                <el-menu-item index="" @click="signOut">Sign out</el-menu-item>
            </el-submenu>
        </div>
    </el-menu>
</div>
</template>

<script>
export default {
    computed: {
        signedIn() {
            return this.$store.state.cognito.user;
        },
        username() {
            return this.$store.state.cognito.user.username;
        }
    },
    methods: {
        signOut() {
            this.$store.dispatch('signOut')
                .catch(err => console.log(err));
        },
        onSelect(key, keyPath) {
            console.log(key, keyPath);
        }
    }
};
</script>
