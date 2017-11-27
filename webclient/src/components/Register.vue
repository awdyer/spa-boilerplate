<template>
<div>
    <h1>Register</h1>
    <el-form :model="form" label-width="120px">
        <el-form-item label="Username">
            <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Email">
            <el-input v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item label="Password">
            <el-input type="password" v-model="form.password"></el-input>
        </el-form-item>
        <el-form-item label="Confirm password">
            <el-input type="password" v-model="form.passwordConfirmation"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">Register</el-button>
        </el-form-item>
    </el-form>
</div>
</template>

<script>
const defaultRole = 'user';

export default {
    data() {
        return {
            form: {
                username: '',
                email: '',
                password: '',
                passwordConfirmation: ''
            }
        };
    },
    methods: {
        // onSubmit() {
        //     console.log('submit');
        //     this.$store.dispatch('signUp', {
        //         username: this.form.username,
        //         password: this.form.password,
        //         attributes: {
        //             email: this.form.email,
        //             'custom:role': defaultRole
        //         }
        //     })
        //     .then(() => console.log('success'))
        //     .catch(err => console.log(err));
        // }
        async onSubmit() {
            console.log('submit');

            try {
                await this.$store.dispatch('signUp', {
                    username: this.form.username,
                    password: this.form.password,
                    attributes: {
                        email: this.form.email,
                        'custom:role': defaultRole
                    }
                });

                console.log('success');

                this.$router.push('/registerconfirm');
            } catch (err) {
                console.log(err);
            }
        }
    }
};
</script>
