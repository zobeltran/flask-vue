<template>
    <v-container>
        <!-- <loading :active.sync="load" :height="128" :width="128" color="teal"></loading> -->
        <v-layout align-center justify-center>
            <v-flex xs12 sm12 md12>
                <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Register Employee</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form>
                            <v-container fluid grid-list-lg>
                                <v-layout wrap row>
                                    <v-flex xs12 sm4 md4>
                                        <v-text-field v-model="firstName" label="First Name"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm4 md4>
                                        <v-text-field v-model="middleName" label="Middle Name"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm4 md4>
                                        <v-text-field v-model="lastName" label="Last Name"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6 md6>
                                        <v-text-field v-model="email" label="Email" type="Email"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6 md6>
                                        <v-text-field v-model="username" label="Username"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6 md6>
                                        <v-text-field v-model="password" label="Password" type="password"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6 md6>
                                        <v-text-field v-model="confirmPassword" label="Confirm Password" type="password"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12>
                                        <v-combobox :item="roles" label="Role" v-model="role"></v-combobox>
                                    </v-flex>
                                </v-layout>
                            </v-container>
                        </v-form>
                        <v-card-action>

                        </v-card-action>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
// import Loading from 'vue-loading-overlay';
// import 'vue-loading-overlay/dist/vue-loading.css';

export default {
    data() {
        return {
            load: false,
            firstName: null,
            middleName: null,
            lastName: null,
            username: null,
            email: null,
            password: null,
            confirmPassword: null,
            role: null,
            roles: [
                {identifier: 'AD', text:'Admin'},
                {identifier: 'RO', text: 'Reservation Officer'},
                {identifier: 'FO', text: 'Financial Officer'},
            ],
            ruleFirstName: [
                (v) => !!v || 'First Name is required',
            ],
            middleName: [
                (v) => !!v || 'Middle Name is required',
            ],
            lastName: [
                (v) => !!v || 'Last Name is required',
            ],
            email: [
                (v) => !!v || 'Email is required',
            ],
            password: [
                (v) => !!v || 'Password is required',
                comparePasswords,
            ],
            role: [
                (v) => !!v || 'Role is required',
            ],
        };
    },
    // computed: {
    //     comparePasswords() {
    //         return this.password !== this.confirmPassword ? 'Passwords do not match' : '';
    //     },
    // },
    methods: {
        register() {
            this.$store.dispatch('registerEmployee', {
                firstName: this.firstName,
                middleName: this.middleName,
                lastName: this.lastName,
                email: this.email,
                username: this.username,
                password: this.password,
                role: this.role,
            })
            .then((response) => {
                this.$route.push({name: 'employee'});
            });
        },
    },
};
</script>
