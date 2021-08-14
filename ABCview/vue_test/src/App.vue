<template>
  <div id="sentence">
    <ScrollingTable/>
    <TokenTable/>
    <LayerSelected/>             
    <ScatterPlot />
  </div>
</template>

<script>
import ScatterPlot from './components/ScatterPlot.vue'
import LayerSelected from './components/LayerSelected.vue'; 
import ScrollingTable from './components/ScrollingTable.vue';
import TokenTable from './components/TokenTable.vue'

export default {
  name: 'App',
  components: {
      ScrollingTable,ScatterPlot,LayerSelected,TokenTable
  }
}
</script>

<style>
#sentence {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.project-title {
  margin: 1rem 0 1rem 0;
}
</style>
