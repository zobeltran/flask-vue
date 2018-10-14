<template>
    
</template>
<script>
export default {
    data() {
        return {
            firstName: null,
            middleName: null,
            lastName: null,
            username: null,
            email: null,
            password: null,
            confirmPassword: null,
            role: null,
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
    computed: {
        comparePasswords() {
            return this.password !== this.confirmPassword ? 'Passwords do not match' : '';
        },
    },
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
