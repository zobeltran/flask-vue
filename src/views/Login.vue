<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex x12 sm8 md4>
                    <v-card class='elevation-12'>
                        <v-toolbar dark color="primary">
                            <v-toolbar-title>Login</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <br>
                        <v-card-text>
                            <v-flex xs9 offset-xs1>
                                <v-form ref="form" v-model="valid">
                                    <v-text-field prepend-icon="person" v-model="username" label="Username" type="text" :rules="usernameRules"></v-text-field>
                                    <v-text-field prepend-icon="lock" v-model="password" label="Password" type="password" :rules="passwordRules"></v-text-field>
                                </v-form>
                            </v-flex>
                        </v-card-text>
                        <v-card-actions>
                            <v-flex xs4 offset-xs4>
                                <v-btn block round color="primary" @click="login()">Login</v-btn>
                            </v-flex>
                        </v-card-actions>
                        <br>
                     </v-card>
                </v-flex>
            </v-layout>
            <v-snackbar v-model="snackbar.isError" :color="snackbar.color" :bottom="snackbar.y" :multi-line="snackbar.mode" :right="snackbar.x" :timeout="snackbar.timeout">
                {{snackbar.text}}
            <v-btn flat @click="snackbar.isError = false">
                Close
            </v-btn>
            </v-snackbar>
        </v-container>
    </v-content>
</template>

<script>
export default {
    data() {
        return{
            snackbar: {
                isError: false,
                y: true,
                x: true,
                mode: true,
                timeout: 6000,
                text: null,
                color: 'error',
            },
            valid: false,
            username: null,
            password: null,
            usernameRules: [
                (v) => !!v || 'Username is Required',
            ],
            passwordRules: [
                (v) => !!v || 'Password is Required',
            ],
        };
    },
    methods: {
        login() {
            if (this.$refs.form.validate()) {
                this.$store.dispatch('retrieveToken', {
                    username: this.username,
                    password: this.password,
                })
                .then((response) => {
                    this.$router.push({name: 'employee'});
                })
                .catch((error) => {
                    if (error.status === 500) {
                        this.snackbar.isError = true;
                        this.snackbar.text = 'Sorry, we\'re slightly having a server error. Please hang on there.';
                    } else {
                        this.snackbar.isError = true;
                        this.snackbar.text = error.data.errors.errorCodes +' ' + error.data.errors.message;
                    }
                });
            }
        },
    },
};
</script>
