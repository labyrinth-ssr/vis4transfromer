<template>
  <div id="layer-selected">
    <a-slider :marks='marks' :max=0.5 :min=0.1 :step=0.1 :default-value="0.4" 
              @afterChange = "afterChange"
              />
  </div>
</template>

<script>
import bus from './bus'

export default {
  name: 'ThresholdSelected',
  methods: {
     afterChange(value) {
      this.threshold = value;
      bus.$emit("dispatchthreshold",this.threshold);
    }
  },
  data(){
    return {
      marks: {
        0.1: '0.1',
        0.2: '0.2',
        0.3: '0.3',
        0.4: '0.4',
        0.5: '0.5',
        },
      threshold:0.4
    }
  }
}
</script>

<style>
</style>