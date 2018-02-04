<template>
  <div>
    <app-nav></app-nav>
    <h3 class="text-center">Daily Startup Battles</h3>
    <button class="btn btn-info log" @click="updateBattles()">Update Battles</button>
    <hr/>
    <div class="col-sm-4" v-for="battle in publicBattles">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title"> {{ battle.name }} </h3>
        </div>
        <div class="panel-body">
          <p><span class="badge alert-info"> Sponsor: </span> {{ battle.sponsor }} </p>
          <p><span class="badge alert-danger"> SeedFund: </span><strong> ${{ battle.seedFund }} </strong></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import AppNav from './AppNav';
import { getPublicStartupBattles } from '../../utils/battles-api';

export default {
  name: 'publicBattles',
  components: {
    AppNav,
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
  },
};
</script>

<style scoped>
</style>
