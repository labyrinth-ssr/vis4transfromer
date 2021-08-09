<template>
  <div id="my_dataviz"></div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";
import {
  sankey as d3Sankey,
  sankeyLinkHorizontal as d3SsankeyLinkHorizontal,
  sankeyLeft as d3SankeyLeft
} from "d3-sankey";
// import * as sankey from 'd3-sankey'
// import sankeydata

export default {
  name: "attr-tree",
  data() {
    return {
      data: [],
    };
  },
  methods: {
    draw(sankeydata,textData) {
      var margin = { top: 60, right: 10, bottom: 50, left: 50 },
        width = 1000 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;
      const sankeyWidth=height,snakeyHeight=width;

      // format variables
      var formatNumber = d3.format(",.0f"), // zero decimal places
        format = function (d) {
          return formatNumber(d);
        },
        color = d3.scaleOrdinal(d3.schemePastel1);
      
      const textData_index=Object.keys(textData)

        const x = d3.scaleBand().domain(textData_index).range([0,width]).padding(0);

      // append the svg object to the body of the page
      var svg = d3
        .select("#my_dataviz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr('id','g-sankey-scale')
        .attr("transform", " translate(" + (margin.left) + "," +( margin.top +height)+ ") rotate(-90)")

      d3.select("svg")
      .append('g')
        .attr("transform", " translate(" + (margin.left) + "," +( margin.top +height)+ ')')
      .style('font-size',7)
      .call(d3.axisBottom(x).tickPadding(0))
      .selectAll('.tick')
      .data(textData)
      .select('text')
      .text(function(d,i){
        return d;
      })

      // Set the sankey diagram properties
      var sankey = d3Sankey()
        .nodeWidth(36)
        .nodePadding(15)//最好换成一个函数
        .size([sankeyWidth,snakeyHeight])
        // .nodeAlign(d3[`sankey${align[0].toUpperCase()}${align.slice(1)}`])
        .nodeId(function id(d) {
          // console.log(d.node, d.name);
          return d.node;
        })
        .nodeSort(function(a,b){
          return a.node-b.node
        })
        .nodeAlign(d3SankeyLeft)

      var path = sankey.links();

      var graph = sankey(sankeydata);

      graph.nodes.forEach(node => {
          var newY=x(node.node)
          var yGAp=node.y1-node.y0
          node.y0=newY-yGAp/2
          node.y1=newY+yGAp/2
          console.log(this)
        });
        sankey.update(graph)

      // add in the links
      var link = svg
        .append("g")
        .selectAll(".link")
        .data(graph.links)
        .enter()
        .append("path")
        .attr("class", "link")
        .attr("d", d3SsankeyLinkHorizontal())
        .attr('fill','none')
        .attr('stroke','#E6E6FA')
        .style("stroke-width", function (d) {
          console.log(d.width)
          return d.width;
        })

      // add the link titles
      link.append("title").text(function (d) {
        return d.source.name + " → " + d.target.name + "\n" + format(d.value);
      });

      // add in the graph
      var node = svg
        .append("g")
        .selectAll(".node")
        .data(graph.nodes)
        .enter()
        .append("g")
        .attr("class", "node");

      // add the rectangles for the graph
      node
        .append("rect")
        .attr("x", function (d) {
          return d.x0;
        })
        .attr("y", function (d) {
          return d.y0;
        })
        .attr("height", function (d) {
          
          return d.y1-d.y0;
        })
        .attr("width", sankey.nodeWidth())
        .style("fill", function (d) {
          return (d.color = color(d.name.replace(/ .*/, "")));
        })
        .style("stroke",'none')
        .append("title")
        .text(function (d) {
          return d.name + "\n" + format(d.value);
        });

      // add in the title for the graph
      node
        .append("text")
        .attr("x", function (d) {
          return d.x0 - 6;
        })
        .attr("y", function (d) {
          return (d.y1 + d.y0) / 2;
        })
        .attr("dy", "0.15em")
        .attr("text-anchor", "end")
        .text(function (d) {
          return d.name;
        })
        .filter(function (d) {
          return d.x0 < width / 2;
        })
        .attr("x", function (d) {
          return d.x1 + 6;
        })
        .attr("text-anchor", "start")


        // d3.selectAll('.node')
        //   .attr('transform',function(d){
            
        //     return 'translate('+d.x0
        //   })

      // });
    },
  },

  mounted() {
    const path = "http://localhost:5000/attr-tree";
    axios
      .get(path)
      .then((res) => {
        var nodeLinkData = res.data.node_link;
        var textData=res.data.tokens
        // console.log(nodeLinkData);
        this.draw(nodeLinkData,textData);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
};
</script>

