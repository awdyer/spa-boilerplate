<template>
<div>
    This is a protected page.
    <el-button type="danger" @click="dangerous">Do restricted action</el-button>
</div>
</template>

<script>
import api from '@/services/api';

export default {
    methods: {
        async dangerous() {
            console.log('doing something dangerous');
            try {
                let res = await api.doSomethingDangerous();
                console.log(res.data);
            } catch (err) {
                console.log(err);
            }
        }
    }
};
</script>
