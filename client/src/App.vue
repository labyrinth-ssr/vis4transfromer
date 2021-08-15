<template>
  <div id="app">
    <a-row :gutter="[2, 2]">
      <a-col :span='12'>
        blankness
      </a-col>
      <a-col :span='12'>
        <div id='attrTree_container'>
          <AttrTree></AttrTree>
        </div>
      </a-col>
    </a-row >
      <a-row :gutter="[2, 2]">
      <!-- <a-col :span='12'>
        blankness
      </a-col> -->
      <!-- <a-col :span='6'>
        <div id='att_container'>
          <AttnMap></AttnMap>
        </div>
      </a-col> -->
      <a-col :span='24'>
        <div id='att_container'>
          <AttnHead></AttnHead>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import AttrTree from './components/AttrTree.vue'
import AttnHead from './components/headView.vue'
// import AttnMap from './components/new_attn_map.vue'

// import attrtree from './components/AttrTree.vue';

export default{
  name: 'App',
  components: {
    AttrTree,
    AttnHead,
    // AttnMap
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


</style>
