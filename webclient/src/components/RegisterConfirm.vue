<template>
<div>
    <h1>Confirm registration</h1>
    <p>You should receive an email with a verification code. Please enter the code below.</p>
    <el-form :model="form" label-width="120px">
        <el-form-item label="Username">
            <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Code">
            <el-input v-model="form.code"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onConfirm">Confirm</el-button>
        </el-form-item>
    </el-form>
    <p>Didn't receive an email?</p>
    <el-form :inline="true" :model="resendForm">
        <el-form-item label="Username">
            <el-input v-model="resendForm.username"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onResend">Resend confirmation email</el-button>
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
                code: ''
            },
            resendForm: {
                username: ''
            }
        };
    },
    methods: {
        async onConfirm() {
            console.log('submit');
            try {
                await this.$store.dispatch('confirmRegistration', {
                    username: this.form.username,
                    code: this.form.code
                });

                console.log('success');

                this.$router.push('/');
            } catch (err) {
                console.log(err);
            }
        },
        async onResend() {
            console.log('resend');
            try {
                await this.$store.dispatch('resendConfirmationCode', {
                    username: this.resendForm.username
                });

                console.log('confirmation email sent');
            } catch (err) {
                console.log(err);
            }
        }
    }
};
</script>
