<template>

<div id="attn-graph"></div>
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
    draw(myData,tokens) {
      // set the dimensions and margins of the graph
      const margin = { top: 20, right: 20, bottom: 20, left: 20 },
        width = 600 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      const svg = d3
        .select("#attn-graph")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

      // Build X scales and axis:
      const axisContent = Array.from(new Array(12).keys())
      const x = d3.scaleBand().range([height, 0]).domain(axisContent).padding(0.05);

      svg
        .append("g")
        .style("font-size", 10)
        .attr("transform", `translate(0, ${height})`)
        .attr("class", "xAxis")
        .call(d3.axisBottom(x).tickSize(0))
        .selectAll(".tick")
        .data(axisContent)
        .select("text")
        .text(function (d, i) {
          return d;
        });

      // Build Y scales and axis:
      // const y = d3.scaleBand().range([height, 0]).domain(arry).padding(0.05);
      svg
        .append("g")
        .style("font-size", 10)
        .call(d3.axisLeft(x).tickSize(0))
        .selectAll(".tick")
        .data(axisContent)
        .select("text")
        .text(function (d, i) {
          return d;
        });
      d3.selectAll(".domain").remove();

      var valArr=[]

      myData.forEach(ele => {
        valArr.push(ele.val)
      });

      // Build color scale
      const myColor = d3
        .scaleSequential()
        .interpolator(d3.interpolateGnBu)
        .domain([0, d3.max(valArr)]);

      // console.log(myData)
      // console.log(Math.max.apply(Math, myData.map(function(o) {return o.val})))

      svg
        .selectAll()
        .data(myData)
        .join('rect')
        .attr("x", function (d) {
          return x(d.layer);
        })
        .attr("y", function (d) {
          return x(d.head);
        })
        .attr("rx", 4)
        .attr("ry", 4)
        .attr("width", x.bandwidth())
        .attr("height", x.bandwidth())
        .style("fill", function (d) {
          return myColor(d.val);
        })
        .style("stroke-width", 4)
        .style("stroke", "none")
        .style("opacity", 0.8);
    },
  },
  
  mounted() {
    const path = 'http://localhost:5000/attn-head';
      axios.get(path)
        .then((res) => {
          const impo_data = res.data.importance;
          const tokens =res.data.tokens
          this.draw(impo_data,tokens)
        }
        )
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
  },
};
</script>