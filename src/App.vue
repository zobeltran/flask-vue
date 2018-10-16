<template>
  <v-app>
    <div v-if="!loggedIn">
        <v-navigation-drawer v-model="drawer" absolute temporary>
          <v-list dense>
            <v-list-tile v-for="(menu,index) in menus" :key="index" :to="{name: menu.route}">
              <v-list-tile-action>
                <v-icon>{{ menu.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{ menu.name }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
        <v-toolbar color="indigo" dark fixed app>
          <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
          <v-toolbar-title>{{ title }}</v-toolbar-title>
        </v-toolbar>
    </div>
    <div v-else-if="loggedIn && loggedAdmin">
        <v-navigation-drawer v-model="drawer" absolute temporary>
          <v-list dense>
            <v-list-tile v-for="(menu,index) in menusAdmin" :key="index" :to="{name: menu.route}">
              <v-list-tile-action>
                <v-icon>{{ menu.icon }}</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>{{ menu.name }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
        <v-toolbar color="indigo" dark fixed app>
          <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
          <v-toolbar-title>{{ titleEmployee }}</v-toolbar-title>
        </v-toolbar>
    </div>
    <v-content>
      <transition name="router-animation" leave-active-class="animate fadeOutLeftBig faster" enter-active-class="animated fadeInRightBig faster" mode="out-in">
        <router-view/>
      </transition>
    </v-content>
    <div v-if="!loggedIn">
      <v-footer height="auto" color="primary lighten-1">
        <v-layout justify-center row wrap>
          <v-btn color="white" flat round :to="{name: 'login'}">
            Employee? Click here
          </v-btn>
          <v-flex primary lighten-2 py-3 text-xs-center white--text xs12>
            &copy;2018 — <strong>Vuetify</strong>
          </v-flex>
        </v-layout>
      </v-footer>
    </div>
    <div v-else>
      <v-footer height="auto" color="primary lighten-1">
        <v-layout justify-center row wrap>
          <v-btn color="white" flat round :to="{name: 'logout'}">
            Logout and Return to the Customer Page
          </v-btn>
          <v-flex primary lighten-2 py-3 text-xs-center white--text xs12>
            &copy;2018 — <strong>Vuetify</strong>
          </v-flex>
        </v-layout>
      </v-footer>
    </div>
  </v-app>
</template>

<style scoped>
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.2/animate.min.css";

.custom-loader {
    animation: loader 1s infinite;
    display: flex;
  }
  @-moz-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-webkit-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @-o-keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }
  @keyframes loader {
    from {
      transform: rotate(0);
    }
    to {
      transform: rotate(360deg);
    }
  }

</style>


<script>
export default {
  data() {
    return {
      drawer: false,
      title: 'First Choice Travel Hub',
      titleEmployee: 'First Choice Travel Hub Employee Dashboard',
      menus: [
        {name: 'Home', icon: 'home', route: 'home'},
        {name: 'Packages', icon: 'mdi-shopping', route: 'customerPackage'},
        {name: 'Tickets', icon: 'mdi-airport', route: 'customerTicket'},
        {name: 'Hotels', icon: 'hotel', route: 'customerHotel'},
        {name: 'Inquiries', icon: 'mdi-comment-alert', route: 'customerInquiries'},
      ],
      menusAdmin: [
        {name: 'Home', icon: 'home', route: 'employeehome'},
        {name: 'Packages', icon: 'mdi-shopping', route: 'employeePackage'},
        {name: 'Tickets', icon: 'mdi-airport', route: 'employeeTicket'},
        {name: 'Hotels', icon: 'hotel', route: 'employeeHotel'},
        {name: 'Inquiries', icon: 'mdi-comment-alert', route: 'employeeInquiries'},
        {name: 'Register Employee', icon: 'mdi-account-plus', route: 'register'},
        {name: 'Logout', icon: 'mdi-account-remove', route: 'logout'},
      ],
    };
  },
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn;
    },
    loggedAdmin() {
      return this.$store.getters.loggedAdmin;
    },
  },
};
</script>
