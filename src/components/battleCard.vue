<template>
  <div class="col-sm-4">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title" v-on:click="shoutOut"> {{ battle.name }} </h3>
      </div>
      <div class="panel-body" v-on:click="shoutOut">
        <p><span class="badge alert-info"> Sponsor: </span> {{ battle.sponsor }} </p>
        <p><span class="badge alert-danger"> SeedFund: </span><strong> ${{ battle.seedFund }} </strong></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'battle-card',
  props: ['battle'],
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
