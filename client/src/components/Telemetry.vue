<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col
        align="end"
        class="grey lighten-5 text-center"
        style="height: 550px;"
      >
        <v-card raised style="display: block">
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">NFOV Camera</div>
              <v-list-item-title class="headline mb-1">Camera Telemetry</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
         <v-row align-content="start" justify="start">
            <v-col align-self="start">
                <span>Date/Time</span>
            </v-col>
            <v-col align-self="start">
                <span>{{timestamp}}</span>
            </v-col>
          </v-row>
          <v-row align-content="start" justify="start">
              <v-col align-self="start">
                  <span>Position</span>
              </v-col>
              <v-col align-self="start">
                  <span>{{position}}</span>
              </v-col>
          </v-row>
          <v-row align-content="start" justify="start">
              <v-col align-self="start">
                  <span>Dist. from Min.</span>
              </v-col>
              <v-col align-self="start">
                  <span>{{minDist}} &mu;</span>
              </v-col>
          </v-row>
           <v-row align-content="start" justify="start">
              <v-col align-self="start">
                  <span>Dist. from Max.</span>
              </v-col>
              <v-col align-self="start">
                  <span>{{maxDist}} &mu;</span>
              </v-col>
          </v-row>
           <v-row align-content="start" justify="start">
              <v-col align-self="start">
                  <span>Step Size</span>
              </v-col>
              <v-col align-self="start">
                  <span>Calc</span>
              </v-col>
          </v-row>
          <v-row align-content="start" justify="start">
            <v-col align-self="start">
            <span>Temperature (C)</span>
            </v-col>
            <v-col align-self="start">
            <span>{{ temp }}</span>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
</v-container>
</template>

<script>
export default {
  data() {
    return {
      timestamp: '05/14/2020 12:10:34',
      position: '56000',
      temp: '0',
      stepSize: 1,
    };
  },
  computed: {
    maxDist() {
      return (112000 - this.position) * 0.08;
    },
    minDist() {
      return this.position * 0.08;
    },
  },
};

</script>

<style scoped>

</style>
