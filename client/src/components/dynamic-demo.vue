<template>
    <div id="dynamic-component-demo" class="demo">
  <button
     v-for="tab in tabs"
     v-bind:key="tab"
     v-bind:class="['tab-button', { active: currentTab === tab }]"
     v-on:click="currentTab = tab"
   >
    {{ tab }}
  </button>

  <component v-bind:is="currentTabComponent" class="tab"></component>
</template>

<script>
import AttnHead from './headView.vue'
import AttnMap from './new_attn_map.vue'

const app = Vue.createApp({
  data() {
    return {
      currentTab: 'Home',
      tabs: ['Home', 'Posts', 'Archive']
    }
  },
  computed: {
    currentTabComponent() {
      return 'tab-' + this.currentTab.toLowerCase()
    }
  }
})

app.component('tab-home', {
  template: `<AttnMap></AttnMap>`
})
app.component('tab-posts', {
  template: `<AttnHead></AttnHead>`
})

app.mount('#attn_container')
</script>
