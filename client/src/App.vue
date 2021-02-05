<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex">
        <v-img
          alt="World View Logo"
          class="shrink mr-2"
          contain
          src="./assets/WorldView_Logo_Color_on_Dark.png"
          transition="scale-transition"
          width="160"
          height="160"
        />
      </div>
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <v-row>
          <v-col>
            <div class="center text-large">
              HiRACS Control
            </div>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col>
            <Tasks></Tasks>
          </v-col>
          <v-col>
            <Focus></Focus>
          </v-col>
          <v-col>
            <Telemetry></Telemetry>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Focus from './components/Focus.vue';
import Tasks from './components/Tasks.vue';
import Telemetry from './components/Telemetry.vue';

export default {
  name: 'App',

  components: {
    Tasks,
    Focus,
    Telemetry,
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>
  .center {
    text-align: center;
    margin: auto;
  }

  .text-large {
    font-size: 200%;
    font-weight: bold;
  }
</style>
