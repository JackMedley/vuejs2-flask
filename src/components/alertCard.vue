<!-- <template>
  <div class="col-sm-4">
    <b-alert>
      Hello
    </b-alert>
  </div>
</template> -->

<template>
  <div class="col-sm-4">
<!--     <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title" v-on:click="shoutOut"> {{ battle.name }} </h3>
      </div> -->
      <!-- <b-alert show> -->
        <!-- Hello -->
      <!-- </b-alert> -->
    <div>
      <b-card header="Card Header"
              header-text-variant="white"
              header-tag="header"
              header-bg-variant="dark"
              footer="Card Footer"
              footer-tag="footer"
              footer-bg-variant="success"
              footer-border-variant="dark"
              title="Title">
              <!-- style="max-width: 20rem;"> -->
        <p class="card-text">Header and footers variants.</p>
      </b-card>
    </div>
<!--       <div class="panel-body" v-on:click="shoutOut">
        <p><span class="badge alert-info"> Sponsor: </span> {{ battle.sponsor }} </p>
        <p><span class="badge alert-danger"> SeedFund: </span><strong> ${{ battle.seedFund }} </strong></p>
      </div> -->
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import bAlert from 'bootstrap-vue/es/components/alert/alert';
import bCard from 'bootstrap-vue/es/components/card/card';

Vue.component('b-alert', bAlert);
Vue.component('b-card', bCard);

export default {
  name: 'alert-card',
  props: ['battle'],
  components: {
    bAlert,
    bCard,
  },
  data() {
    return {
      name: '',
      sponsor: '',
      seedFund: '',
    };
  },
  methods: {
    shoutOut() {
      console.log(this.battle.name);
    },
  },
};
</script>

<style scoped>
</style>
