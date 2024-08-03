<template>
  <div id="main" style="width: 600px; height: 400px;"></div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
  name: 'RelationshipGraph',
  props: {
    person_info: {
      type: Object,
      required: true
    },
    person_tag: {
      type: Object,
      required: true
    }
  },
  mounted() {
    const data = JSON.parse(this.person_tag['家庭背景']);
    console.log(data);
    console.log(this.person_info['姓名']);

    // 构建人物关系数据
    const nodes = [{ name: this.person_info['姓名'], symbolSize: 50 }];
    const links = [];

    for (const id in data) {
      console.log(id);
      console.log(data[id]);
      const person = data[id];
      nodes.push({ name: person['姓名'], symbolSize: 50 });
      links.push({ source: this.person_info['姓名'], target: person['姓名'] });
    }

    this.initChart(nodes, links);
  },
  methods: {
    initChart(nodes, links) {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      option = {
        title: {
          text: '人物关系图'
        },
        tooltip: {},
        series: [
          {
            type: 'graph',
            layout: 'force',
            data: nodes,
            links: links,
            roam: true,
            label: {
              show: true,
              position: 'right'
            },
            force: {
              repulsion: 1000
            }
          }
        ]
      };

      option && myChart.setOption(option);
    }
  }
};
</script>

<style>
#main {
  width: 100%;
  height: 100%;
}
</style>
