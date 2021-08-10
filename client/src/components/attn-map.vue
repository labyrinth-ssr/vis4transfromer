<template>
  <div id="attn-map"></div>
</template>

<script>
import * as d3 from "d3";
// import axios from "axios";
import visData from "../../../data/layerHead1.csv";

export default {
  name: "attn_map",
  data() {
    return {
      data: [],
    };
  },
  methods: {

    draw() {
      // set the dimensions and margins of the graph
      const margin = { top: 80, right: 25, bottom: 30, left: 40 },
        width = 450 - margin.left - margin.right,
        height = 450 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      const svg = d3
        .select("#attn-map")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

      const left_text = [
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
      const right_text = [
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
      const leftTextEntry = left_text.entries();
      const rightTextEntry = right_text.entries();
      d3.csv(visData).then((data) => {
        renderDetail(data);
      });

      const config = {};
      const color = "steelblue";
      const background_color = "pink";
      const DETAIL_ATTENTION_WIDTH = 140;
      const DETAIL_BOX_WIDTH = 80;
      const DETAIL_BOX_HEIGHT = 18;
      const DETAIL_PADDING = 0;
      const TEXT_SIZE = 13;
      config.leftText = left_text;
      config.rightText = right_text;
      config.svg = svg;

      function renderDetail(att) {
        const x = 50,
          y = 50;
        var posLeftText = x;
        var posAttention = posLeftText + DETAIL_BOX_WIDTH;
        var posRightText = posAttention + DETAIL_ATTENTION_WIDTH;

        // renderDetailFrame(x,y);
        renderDetailText(
          leftTextEntry,
          "leftText",
          posLeftText,
          y + DETAIL_PADDING
        );
        renderDetailAttn(posAttention, y + DETAIL_PADDING, att);
        renderDetailText(
          rightTextEntry,
          "rightText",
          posRightText,
          y + DETAIL_PADDING
        );
      }

      function renderDetailText(text, id, x, y) {
        var tokenContainer = config.svg
          .append("svg:g")
          .classed("detail", true)
          .selectAll("g")
          .data(text)
          .enter()
          .append("g");

        tokenContainer
          .append("rect")
          .classed("highlight", true)
          .style("opacity", 0.0)
          .attr("height", DETAIL_BOX_HEIGHT)
          .attr("width", DETAIL_BOX_WIDTH)
          .attr("x", x)
          .attr("y", function (d, i) {
            console.log(i);
            return y + i * DETAIL_BOX_HEIGHT;
          });

        var textContainer = tokenContainer
          .append("text")
          .classed("token", true)
          .text(function (d) {
            return d[1];
          })
          .attr("font-size", TEXT_SIZE + "px")
          .style("cursor", "default")
          .style("-webkit-user-select", "none")
          .attr("fill", color)
          .attr("x", x)
          .attr("y", function (d, i) {
            return i * DETAIL_BOX_HEIGHT + y;
          })
          .attr("height", DETAIL_BOX_HEIGHT)
          .attr("width", DETAIL_BOX_WIDTH)
          .attr("dy", TEXT_SIZE);

        if (id == "leftText") {
          textContainer
            .style("text-anchor", "end")
            .attr("dx", DETAIL_BOX_WIDTH - 2);
          tokenContainer.on("mouseover", function (d, data) {
            console.log(data);
            highlightSelection(data[0]);
          });
          tokenContainer.on("mouseleave", function () {
            unhighlightSelection();
          });
        }
      }

      function renderDetailAttn(x, y, att) {
        var attnContainer = config.svg
          .append("g")
          .classed("detail", true)
          .attr("pointer-events", "none");
        attnContainer
          .selectAll("g")
          .data(att)
          .enter()
          .append("g") // Add group for each source token
          .attr("id", function (d, i) {
            return `g${i}`;
          })
          .classed("attn-line-group", true) //13*13(source-target)
          .attr("source-index", function (d, i) {
            // Save index of source token
            return i;
          })
          .selectAll("line")
          .data(function (d) {
            // Loop over all target tokens
            var arr = Object.values(d).map(Number);
            return arr;
          })
          .enter()
          .append("line")
          .attr("x1", x)
          .attr("y1", function (d) {
            var sourceIndex = +this.parentNode.getAttribute("source-index");
            return y + (sourceIndex + 0.5) * DETAIL_BOX_HEIGHT;
          })
          .attr("x2", x + DETAIL_ATTENTION_WIDTH)
          .attr("y2", function (d, targetIndex) {
            return y + (targetIndex + 0.5) * DETAIL_BOX_HEIGHT;
          })
          .attr("stroke-width", 2.2)
          .attr("stroke", color)
          .attr("stroke-opacity", function (d) {
            return d;
          });
      }

      function highlightSelection(index) {
        config.svg
          .selectAll(".highlight")
          .attr("fill", background_color)
          .style("opacity", function (d, i) {
            return i == index ? 1.0 : 0.0;
          });
        config.svg
          .selectAll(".attn-line-group")
          .style("opacity", function (d, i) {
            return i == index ? 1.0 : 0.0;
          });
      }

      function unhighlightSelection() {
        config.svg
          .select("#leftText")
          .selectAll(".highlight")
          .style("opacity", 0.0);
        config.svg.selectAll(".attn-line-group").style("opacity", 1);
      }
    },
  },
  mounted() {
    this.draw()
  },
};
</script>