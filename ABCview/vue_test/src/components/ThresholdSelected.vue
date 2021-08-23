<template>
  <div id="threshold-selected">
    <a-slider :marks='marks' :max=0.5 :min=0.1 :step=0.1 :default-value="0.4" 
      @afterChange="onAfterChange" 
              />
  </div>
</template>

<script>
import bus from './bus'

export default {
  name: 'ThresholdSelected',
  methods: {
     onAfterChange(value) {
       console.log('after change')
      this.threshold = value;
      bus.$emit("dispatchthreshold",this.threshold);
    },
    
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
#threshold-selected{
  height: 5%;
}
</style>