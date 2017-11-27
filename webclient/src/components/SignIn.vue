<template>
<div>
    <h1>Sign in</h1>
    <el-form :model="form" label-width="120px">
        <el-form-item label="Username">
            <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Password">
            <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">Sign in</el-button>
        </el-form-item>
    </el-form>
</div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                username: '',
                password: ''
            }
        };
    },
    methods: {
        // onSubmit() {
        //     console.log('submit');
        //     this.$store.dispatch('authenticateUser', {
        //         username: this.form.username,
        //         password: this.form.password
        //     })
        //     .then(() => {
        //         console.log('success');
        //         this.$store.dispatch('getUserAttributes');
        //     })
        //     .catch(err => console.log(err));
        // },
        async onSubmit() {
            console.log('submit');

            try {
                await this.$store.dispatch('authenticateUser', {
                    username: this.form.username,
                    password: this.form.password
                });

                await this.$store.dispatch('getUserAttributes');

                console.log('success');

                this.$router.push('/');
            } catch (err) {
                console.log(err.code);
                if (err.code === 'UserNotConfirmedException') {
                    this.$router.push('/registerconfirm');
                }
            }
        }
    }
};
</script>
