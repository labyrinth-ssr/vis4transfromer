<template>
<!-- // 说明：const：text message,margin，svg大小
// getmessage 方法未分离，耦合在mounted中
// 数据从flask来，整个方法用d3画在svg上，模板里面只有一个div 
建议：与map图共用svg和数据，属于一个组件

-->

<div id="my_dataviz"></div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";
// import visData from '../../../data/attn_head.json'

export default {
  name: "attn_graph",
  data() {
    return {
      data: []
    };
  },
  methods: {
    // getMessage() {
    //   const path = 'http://localhost:5000/data';
    //   axios.get(path)
    //     .then((res) => {
    //       this.data = res.data.data;
    //       console.log(this.data)
    //     })
    //     .catch((error) => {
    //       // eslint-disable-next-line
    //       console.error(error);
    //     });
    // },
    draw(myData) {
      // set the dimensions and margins of the graph
      const margin = { top: 80, right: 25, bottom: 30, left: 40 },
        width = 450 - margin.left - margin.right,
        height = 450 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      const svg = d3
        .select("#my_dataviz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

      //static data
      const xText = [
        "[CLS]",
        "I",
        "have",
        "tried",
        "my",
        "best",
        "[SEP]",
        "Sadly",
        ",",
        "I",
        "still",
        "lose",
        "[SEP]",
      ];
      const yText = [
        "[CLS]",
        "I",
        "have",
        "tried",
        "my",
        "best",
        "[SEP]",
        "Sadly",
        ",",
        "I",
        "still",
        "lose",
        "[SEP]",
      ];
      var arrx = [];
      for (var i = 0; i < xText.length; i++) {
        arrx.push(i);
      }
      var arry = [];
      for (var i = 0; i < xText.length; i++) {
        arry.push(i);
      }

      // Build X scales and axis:
      const x = d3.scaleBand().range([height, 0]).domain(arrx).padding(0.05);

      svg
        .append("g")
        .style("font-size", 10)
        .attr("transform", `translate(0, ${height})`)
        .attr("class", "xAxis")
        .call(d3.axisBottom(x).tickSize(0))
        .selectAll(".tick")
        .data(xText.reverse())
        .select("text")
        .text(function (d, i) {
          return d;
        });

      // Build Y scales and axis:
      const y = d3.scaleBand().range([height, 0]).domain(arry).padding(0.05);
      svg
        .append("g")
        .style("font-size", 10)
        .call(d3.axisLeft(y).tickSize(0))
        .selectAll(".tick")
        .data(yText)
        .select("text")
        .text(function (d, i) {
          return d;
        });
      d3.selectAll(".domain").remove();

      // Build color scale
      const myColor = d3
        .scaleSequential()
        .interpolator(d3.interpolateInferno)
        .domain([0, 1]);

      svg
        .selectAll()
        .data(myData)
        .join('rect')
        .attr("x", function (d) {
          return x(+d['source']);
        })
        .attr("y", function (d) {
          return y(+d['target']);
        })
        .attr("rx", 4)
        .attr("ry", 4)
        .attr("width", x.bandwidth())
        .attr("height", y.bandwidth())
        .style("fill", function (d) {
          return myColor(+ d['value']);
        })
        .style("stroke-width", 4)
        .style("stroke", "none")
        .style("opacity", 0.8);
    },
  },
  
  mounted() {
    const path = 'http://localhost:5000/data';
      axios.get(path)
        .then((res) => {
          const newData = res.data.data;
          this.draw(newData)
        }
        )
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
  },
};
</script>