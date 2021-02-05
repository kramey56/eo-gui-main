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
              <v-list-item-title class="headline mb-1">Camera Focus</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-container>
            <v-row align-content="start" justify="start">
              <v-col align-self="start">
                <span>Moving</span>
              </v-col>
              <v-col class="text-left">
                <span v-if="moving === '0'">
                  <v-img src="../assets/red-led-on.png"
                  class="indicator"
                  height="40"
                  width="40"
                />
                </span>
                <span v-if="moving === '1'">
                  <v-img src="../assets/green-led-on.png"
                  class="indicator"
                  height="40"
                  width="40"
                />
                </span>
              </v-col>
            </v-row>
            <v-row align-content="start" justify="start">
              <v-col align-self="start">
                <span>Position</span>
              </v-col>
              <v-col align-self="start">
                <span>{{ position }}</span>
              </v-col>
            </v-row>
            <v-row align-content="center" justify="center">
              <v-col cols="6" align-self="center">
                <v-text-field
                  v-model="stepSize"
                  label="Step Size"
                  @input="calcStep"
                  persistent-hint
                  suffix="microns">
                </v-text-field>
              </v-col>
            </v-row>
            <v-row align-content="center" justify="center">
              <v-col cols="6" align-self="center">
                <v-text-field
                  v-model="stepCount"
                  label="Step Count"
                >
              </v-text-field>
              </v-col >
            </v-row>
          </v-container>
          <v-card-actions>
            <v-btn large bottom color="primary" v-on:click.native="focusHome">
            Home</v-btn>
            <v-spacer></v-spacer>
            <v-btn large bottom color = "primary" v-on:click.native="focusIn">In</v-btn>
            <v-spacer></v-spacer>
            <v-btn large bottom color="primary" v-on:click.native="focusCenter">
            Center</v-btn>
            <v-spacer></v-spacer>
            <v-btn large bottom color="primary" v-on:click.native="focusOut">Out</v-btn>
            <v-spacer></v-spacer>
            <v-btn large bottom color="primary" v-on:click.native="focusZero">
            Zero</v-btn>
          </v-card-actions>
          <v-snackbar
            v-model="snackbar"
            top
          >
            {{ snackbarText }}
            <v-btn
              color="blue"
              text
              @click="snackbar = false"
            >
              Close
            </v-btn>
          </v-snackbar>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      msg: '',
      moving: '0',
      position: '0',
      polling: null,
      stepSize: 1.04,
      stepCount: 1,
      physSteps: 13,
      snackbar: false,
      snackbarText: '',
    };
  },
  methods: {
    calcStep() {
      this.physSteps = Math.trunc(this.stepSize / 0.08) * this.stepCount;
      this.stepSize = this.physSteps * 0.08;
    },
    focusZero() {
      const path = 'http://localhost:5000/zero';
      axios.get(path)
        .then((res) => {
          this.snackbarText = res.data;
          this.snackbar = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    focusHome() {
      const path = 'http://localhost:5000/home';
      axios.get(path)
        .then((res) => {
          this.snackbarText = res.data;
          this.snackbar = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    focusCenter() {
      const path = 'http://localhost:5000/center';
      axios.get(path)
        .then((res) => {
          this.snackbarText = res.data;
          this.snackbar = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    focusStatus() {
      const path = 'http://localhost:5000/status';
      axios.get(path)
        .then((res) => {
          if (res.data.IsMoving === undefined) {
            this.snackbarText = 'HiRACS not responding';
            this.snackbar = true;
          } else {
            this.moving = res.data.IsMoving;
            this.position = res.data.CurrPos;
            this.temp = res.data.TempC;
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
        });
    },
    focusOut() {
      const path = 'http://localhost:5000/move';
      const bodyFormData = new FormData();
      const realSteps = this.physSteps * this.stepCount;
      const dest = parseInt(this.position, 10) + realSteps;
      bodyFormData.set('target', dest);
      axios.post(path, bodyFormData)
        .then((res) => {
          this.snackbarText = res.data;
          this.snackbar = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
        });
    },
    focusIn() {
      const path = 'http://localhost:5000/move';
      const bodyFormData = new FormData();
      const realSteps = this.physSteps * this.stepCount;
      const dest = parseInt(this.position, 10) - realSteps;
      bodyFormData.set('target', dest);
      axios.post(path, bodyFormData)
        .then((res) => {
          this.snackbarText = res.data;
          this.snackbar = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
        });
    },
  },
};
</script>

<style scoped>
  .databox {
    max-width: 600px;
    max-height: 600px;
    margin: auto;
  }

  .indicator {
    position: absolute;
    margin: 0 0 0 0;
  }
</style>
