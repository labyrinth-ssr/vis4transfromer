<template>
  <div id="app">
    <a-row :gutter="[2, 2]">
      <a-col :span='12'>
        <ScrollingTable />
          <TokenTable />
      </a-col>
      <a-col :span='12'>
        <div id='attrTree_container'>
          <AttrTree></AttrTree>
        </div>
      </a-col>
    </a-row >
      <a-row :gutter="[2, 2]">
      <a-col :span='12'>
        <LayerSelected />
          <ScatterPlot />
      </a-col>
      <a-col :span='12'>
        <div id='att_container'>
          <AttnHead></AttnHead>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import ScatterPlot from "./components/ScatterPlot.vue";
import LayerSelected from "./components/LayerSelected.vue";
import ScrollingTable from "./components/ScrollingTable.vue";
import TokenTable from "./components/TokenTable.vue";
import AttnHead from "./components/headView.vue";
import AttrTree from './components/AttrTree.vue'

export default {
  name: "App",
  components: {
    ScrollingTable,
    ScatterPlot,
    LayerSelected,
    TokenTable,
    AttnHead,
    AttrTree
  },
};
</script>

<style>
#sentence {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
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
