<template>
  <div>
    <app-nav></app-nav>
    <h3 class="text-center">Daily Startup Battles</h3>
    <button class="btn btn-info log" v-on:click="updateBattles()">Update Battles</button>
    <hr/>
    <div class="row">
      <battle-card v-for="battle in publicBattles" v-bind:battle="battle" v-bind:key="battle.id"></battle-card>
    </div>
<!--     <div class="row">
      <alert-card v-for="battle in publicBattles" v-bind:battle="battle" v-bind:key="battle.id"></alert-card>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios';
import AppNav from './AppNav';
import BattleCard from './battleCard';
// import AlertCard from './alertCard';
import { getPublicStartupBattles } from '../../utils/battles-api';

export default {
  name: 'publicBattles',
  components: {
    AppNav,
    BattleCard,
    // AlertCard,
  },
  data() {
    return {
      publicBattles: '',
    };
  },
  methods: {
    getPublicStartupBattles() {
      getPublicStartupBattles().then((battles) => {
        this.publicBattles = battles;
      });
    },
    updateBattles() {
      axios.get('http://localhost:3333/api/battles/public')
        .then((response) => { this.publicBattles = response.data; })
        .catch((e) => { this.errors.push(e); });
    },
  },
  mounted() {
    this.getPublicStartupBattles();
    setInterval(() => {
      this.getPublicStartupBattles();
    }, 300);
  },
};
</script>

<style>
</style>
