import Vue from 'vue';
import VueRouter from 'vue-router';
import Focus from '../components/Focus.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/focus',
      name: 'Focus',
      component: Focus,
    },
  ],
});
