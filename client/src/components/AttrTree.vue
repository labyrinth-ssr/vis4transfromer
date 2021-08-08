<template>
  <div id="my_dataviz"></div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";
import {
  sankey as d3Sankey,
  sankeyLinkHorizontal as d3SsankeyLinkHorizontal,
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
    draw(sankeydata) {
      var margin = { top: 10, right: 10, bottom: 10, left: 10 },
        width = 900 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

      // format variables
      var formatNumber = d3.format(",.0f"), // zero decimal places
        format = function (d) {
          return formatNumber(d);
        },
        color = d3.scaleOrdinal(d3.schemeCategory10);

      // append the svg object to the body of the page
      var svg = d3
        .select("body")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // Set the sankey diagram properties
      var sankey = d3Sankey()
        .nodeWidth(36)
        .nodePadding(0)
        .size([width, height])
        // .nodeAlign(d3[`sankey${align[0].toUpperCase()}${align.slice(1)}`])
        .nodeId(function id(d) {
          // console.log(d.node, d.name);
          return d.node;
        });

      var path = sankey.links();

      const{nodes,links} = sankey({
    nodes: sankeydata.nodes.map(d => Object.assign({}, d)),
    links: sankeydata.links.map(d => Object.assign({}, d))
  });

  console.log(links)
  console.log(nodes)

      // add in the links
      var link = svg
        .append("g")
        .selectAll(".link")
        .data(links)
        .enter()
        .append("path")
        .attr("class", "link")
        .attr("d", d3SsankeyLinkHorizontal())
        .attr("stroke-width", function (d) {
          console.log(d.width)
          return d.width;
        })

      // add the link titles
      link.append("title").text(function (d) {
        return d.source.name + " → " + d.target.name + "\n" + format(d.value);
      });

      // add in the nodes
      var node = svg
        .append("g")
        .selectAll(".node")
        .data(nodes)
        .enter()
        .append("g")
        .attr("class", "node");

      // add the rectangles for the nodes
      node
        .append("rect")
        .attr("x", function (d) {
          return d.x0;
        })
        .attr("y", function (d) {
          return d.y0;
        })
        .attr("height", function (d) {
          return d.y1 - d.y0;
        })
        .attr("width", sankey.nodeWidth())
        .style("fill", function (d) {
          return (d.color = color(d.name.replace(/ .*/, "")));
        })
        .style("stroke", function (d) {
          return d3.rgb(d.color).darker(2);
        })
        .append("title")
        .text(function (d) {
          return d.name + "\n" + format(d.value);
        });

      // add in the title for the nodes
      node
        .append("text")
        .attr("x", function (d) {
          return d.x0 - 6;
        })
        .attr("y", function (d) {
          return (d.y1 + d.y0) / 2;
        })
        .attr("dy", "0.35em")
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
        .attr("text-anchor", "start");

      // });
    },
  },

  mounted() {
    const path = "http://localhost:5000/attr-tree";
    axios
      .get(path)
      .then((res) => {
        var newData = res.data.node_link;
        // console.log(newData);

        this.draw(newData);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
};
</script>

