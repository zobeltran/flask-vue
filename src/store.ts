import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || null,
    role: localStorage.getItem('role') || null,
  },
  mutations: {
    retrieveToken(state, data) {
      state.token = data.token;
      state.role = data.role;
    },
    destroyToken(state) {
      state.token = null;
    },
  },
  actions: {
    registerEmployee(context, data) {
      return new Promise((resolve, reject) => {
        axios.post('/api/user/register',
        {
          firstName: data.firstName,
          middleName: data.middleName,
          lastName: data.lastName,
          username: data.username,
          password: data.password,
          role: data.role,
        },
        {
          headers: {'X-CLIENT-TOKEN': localStorage.getItem('token')},
        })
        .then((response) => {
          resolve(response);
        })
        .catch((error) => {
          reject(error);
        });
      });
    },
    retrieveToken(context, credentials) {
      return new Promise((resolve, reject) => {
        axios.post('/api/users/auth/login', {
          username: credentials.username,
          password: credentials.password,
        })
        .then((response) => {
          const data = response.data;
          localStorage.setItem('token', data.token);
          localStorage.setItem('role', data.role);
          context.commit('retrieveToken', data);
          resolve(response);
        })
        .catch((error) => {
          localStorage.removeItem('token');
          reject(error.response);
        });
      });
    },
    destroyToken(context) {
      if (context.getters.loggedIn) {
        localStorage.removeItem('token');
        context.commit('destroyToken');
      }
    },
  },
  getters: {
    loggedIn(state) {
      return state.token !== null;
    },
    loggedAdmin(state) {
      return state.role === 'admin' && state.role !== null;
    },
    loggedReservationOfficer(state) {
      return state.role === 'RO' && state.role !== null;
    },
    loggedFinancialOfficer(state) {
      return state.role === 'FO' && state.role !== null;
    },
  },
});
