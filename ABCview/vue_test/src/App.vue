<template>
  <div id="app">
    <a-row id='row1' :gutter="[2, 2]">
      <a-col :span='12'>
        <div id='tableContainer' class="container"> 
        <ScrollingTable />
          <TokenTable />
        </div>
      </a-col>
      <a-col :span='12'>
        <div id='attrTree_container' class="container">
          <ThresholdSelected />
          <AttrTree></AttrTree>
        </div>
      </a-col>
    </a-row >
    <a-row id='row2' :gutter="[2, 2]">
      <a-col :span='12'>
        <div id='tsneContainer' class="container">
        <LayerSelected />
          <ScatterPlot />
        </div>
      </a-col>
      <a-col :span='12'>
        <div id='att_container' class="container">
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
import ThresholdSelected from './components/ThresholdSelected.vue'

export default {
  name: "App",
  components: {
    ScrollingTable,
    ScatterPlot,
    LayerSelected,
    TokenTable,
    AttnHead,
    AttrTree,
    ThresholdSelected
  },
};
</script>

<style>
html,body { height: 100%; padding: 0; margin: 0; }
#app {
        height: 100%;
        width: 100%;
        box-sizing: border-box;
        /* display: flex; */
        overflow: hidden;

}
.ant-row{
  box-sizing: border-box;
  height: 50%;
  width: 100%;
}
/* #row2{
  box-sizing: border-box;
  height: 40%;
  width: 100%;
} */
.ant-col{
  box-sizing: border-box;
  height: 100%;
}
.container{
  box-sizing: border-box;
  height: 100%;
  width: 100%;
  border: 1px solid darkred;
  overflow: auto;
}

/* #sentence {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.project-title {
  margin: 1rem 0 1rem 0;
} */
</style>
