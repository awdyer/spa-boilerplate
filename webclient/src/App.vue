<template>
<!-- <div id="app" class="full-height">
    <topbar></topbar>
    <el-row class="full-height">
        <el-col :span="4" class="full-height">
            <sidebar></sidebar>
        </el-col>
        <el-col :span="20" class="container">
            <router-view></router-view>
        </el-col>
    </el-row>
</div> -->

<el-container>
    <el-header>
        <topbar></topbar>
    </el-header>
    <el-container>
        <el-aside width="200px"></el-aside>
        <el-container>
            <el-main>
                <router-view></router-view>
            </el-main>
            <el-footer></el-footer>
        </el-container>
    </el-container>
</el-container>
</template>

<style>
@import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700');

html,
body {
    margin: 0;
    padding: 0;
    height: 100%;
    font-family: 'Source Sans Pro', 'Helvetica Neue', sans-serif;
}

.pull-right {
    float: right;
}

a:active,
a:hover,
a:visited,
a:link {
    text-decoration: none;
}

.el-container {
    /* width: 100%; */
    height: 100%;
}

/* .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
} */

.el-aside {
    background-color: #D3DCE6;
    color: #333;
    /* text-align: center; */
    /* line-height: 200px; */
}

.el-main {
    background-color: #E9EEF3;
    color: #333;
    /* text-align: center; */
    /* line-height: 160px; */
}

/* body > .el-container {
    margin-bottom: 40px;
} */

/* .el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 320px;
} */
</style>

<script>
import Topbar from './components/Topbar';
// import Sidebar from './components/Sidebar';

export default {
    name: 'app',
    components: { Topbar }
};
</script>
