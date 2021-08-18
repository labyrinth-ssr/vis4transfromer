<template>
  <div id="attr-tree"></div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";
import {
  sankey as d3Sankey,
  sankeyLinkHorizontal as d3SsankeyLinkHorizontal,
  sankeyLeft as d3SankeyLeft
} from "d3-sankey"; 
import bus from './bus';


export default {
  name: "AttrTree",
  created(){
    bus.$on('dispatchsentencetoshow',val=>{
      this.tokens=val[0]
      var temp=[]
      val[0].forEach(function(token,index){
          temp.push({'node': `${index}`, 'name': token})
      })
      this.nodes=temp
          console.log(this.nodes)

      this.sentence_selected = val[1];
      console.log(this.sentence_selected)
      this.update();
    })
  },
  data() {
    return {
      data: [],
      sentence_selected:5, //初始时自动选择第一句
      tokens:[],
      nodes:[]
    };
  },
  methods: {
update(){
      
      console.log(this.sentence_selected)//清空SVG中的内容
      this.getAll();
    },


    draw(sankeydata,textData,nodesData) {//sankeydata:node,link
d3.select('#AttrTreeSvg').remove()
      d3.select('#AttrTreeSvg')
        .selectAll('*')
        .remove();
      var margin = { top: 60, right: 50, bottom: 50, left: 10 },
        width = 700 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
      const sankeyWidth=height,snakeyHeight=width;

      // format variables
      var formatNumber = d3.format(",.0f"), // zero decimal places
        format = function (d) {
          return formatNumber(d);
        },
        color = d3.scaleOrdinal(d3.schemePaired);
      
      const textData_index=Object.keys(textData)

        const x = d3.scaleBand().domain(textData_index).range([0,width]).padding(0);

      // append the svg object to the body of the page
      var svg = d3
        .select("#attr-tree")
        .append("svg")
        .attr('id','AttrTreeSvg')
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
      .text(function(d){
        return d;
      })

      // Set the sankey diagram properties
      var sankey = d3Sankey()
        .nodeWidth(36)
        .nodePadding(15)//最好换成一个函数
        .size([sankeyWidth,snakeyHeight])
        // .nodeAlign(d3[`sankey${align[0].toUpperCase()}${align.slice(1)}`])
        .nodeId(function id(d) {
          return d.node;
        })
        .nodeSort(function(a,b){
          return a.node-b.node
        })
        .nodeAlign(d3SankeyLeft)
        .nodes(nodesData)


      var graph = sankey(sankeydata);

      graph.nodes.forEach(node => {
          var newY=x(node.node)
          var yGAp=x.bandwidth()
          node.y0=newY
          node.y1=newY+yGAp
        });

        graph.links.forEach(link => {
          link.width=x.bandwidth()
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
        .attr('stroke','grey')
        .style('opacity',0.3)
        .style("stroke-width", function (d) {
          return d.width;
        })
        .on('mouseover',function(){
          d3.select(this).style('opacity',0.6)
        })
        .on('mouseleave',function(){
          d3.select(this).style('opacity',0.3)
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

      node.append('g')
      // .data(d3.select(this.parentNode).datum())
      .attr('class','textG')
      .attr('transform',function(d){
        return 'translate('+d.x0+','+d.y0+') rotate(45)'
      })

      

      // add the rectangles for the graph
      node
        .append("rect")
        .attr('class','nodeRect')
        .attr("x", function (d) {
          return d.x0;
        })
        .attr("y", function (d) {
          return d.y0;
        })
        .attr("height", function (d) {
          return Math.max(1,d.targetLinks.length)*x.bandwidth() ;
        })
        .attr("width", sankey.nodeWidth())
        .style("fill", function (d) {

          if((d.targetLinks.length+d.sourceLinks.length)=== 0){
            return 'none';
          }
          return (d.color = color(d.name.replace(/ .*/, "")));
        })
        .style("stroke",'none')
        .style("opacity",0.5)
        .append("title")
        .text(function (d) {
          return d.name + "\n" + format(d.value);
        });

d3.selectAll('.textG')
      .append('text')
      .attr('font-size',10)
      .text(function(d){
        return d.name
      })

        // d3.selectAll('.node')
        // .append('g')
        // .attr('transform','translate('+)
        // .append('rect')
        // .attr('width',50)
        // .attr('height',50)
        // .attr('fill','blue')
        // .append("text")
        // .attr('class','nodeText')
        // .attr('font-size',10)
        // .attr('text-anchor','end')
        // .text(function (d) {
        //   return d.name;
        // })

      // add in the title for the graph
      // node
      //   .append("text")
      //   .attr('class','nodeText')

      //   .attr("x", function (d) {
      //     return d.x0;
      //   })
      //   .attr("y", function (d) {
      //     return (d.y1 + d.y0) / 2;
      //   })
      //   // .attr("dy", "0.15em")
      //   .attr('font-size',10)

      //   .attr('text-anchor','end')
      //   // .attr('transform','rotate(45)')



      //   .text(function (d) {
      //     return d.name;
      //   })

      //   .filter(function (d) {
      //     return d.x0 < width / 2;
      //   })
      //   .attr("x", function (d) {
      //     return d.x1 + 6;
      //   })
      //   .attr("text-anchor", "start")


        // d3.selectAll('.node')
        //   .attr('transform',function(d){
            
        //     return 'translate('+d.x0
        //   })

      // });
    },
    getAll(){
      const path='http://127.0.0.1:5000/query_attr_tree/'+this.sentence_selected
      console.log(path)
      axios.get(path)
        .then((res) => {
          var nodeLinkData = res.data.node_link;
        var tokens=res.data.tokens
        if(this.tokens.length!=0){
            tokens=this.tokens
          }
        var nodesData=nodeLinkData.nodes
        if(this.nodes.length!=0){
          nodesData=this.nodes
        }
        this.draw(nodeLinkData,tokens,nodesData);
        }
        )
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  mounted() {
    this.getAll()
  },
};
</script>

