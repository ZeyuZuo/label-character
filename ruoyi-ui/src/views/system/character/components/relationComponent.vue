<template>
  <div id="main" style="width: 100%; height: 100%;"></div>
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
    // 构建人物关系数据
    const nodes = [{
      name: this.person_info['姓名'],
      symbolSize: 80,
      itemStyle: { color: '#f6a956' }, // 设置本人节点颜色为红色
      node_type: 0
    }];
    const links = [];

    this.buildFamilyData(nodes, links);
    this.buildNetFriendData(nodes, links);
    this.buildFriendData(nodes, links);

    this.initChart(nodes, links);
  },
  methods: {
    buildFamilyData(nodes, links) {
      const data = JSON.parse(this.person_tag['家庭背景']);

      for (const id in data) {
        // console.log(id);
        // console.log(data[id]);
        const person = data[id];

        nodes.push({
          name: person['姓名'],
          itemStyle: { color: '#3ab7dd' },
          symbolSize: 50,
          info: person,
          node_type: 1
        });

        links.push({
          source: this.person_info['姓名'],
          target: person['姓名'],
          label: {
            show: true,
            formatter: person['关系']
          }
        });
      }
    },
    buildNetFriendData(nodes, links) {
      const data = JSON.parse(this.person_tag['网友关系']);

      for (const id in data) {
        // console.log(id);
        // console.log(data[id]);
        const person = data[id];

        nodes.push({
          name: person['真实姓名'],
          itemStyle: { color: '#3ab7dd' },
          symbolSize: 50,
          info: person,
          node_type: 2
        });

        links.push({
          source: this.person_info['姓名'],
          target: person['真实姓名'],
          label: {
            show: true,
            formatter: person['关系']
          }
        });
      }
    },
    buildFriendData(nodes, links) {
      const data = JSON.parse(this.person_tag['社会关系']);

      for (const id in data) {
        // console.log(id);
        // console.log(data[id]);
        const person = data[id];

        nodes.push({
          name: person['姓名'],
          itemStyle: { color: '#3ab7dd' }, // 设置其他人节点颜色为淡蓝色
          symbolSize: 50,
          info: person,
          node_type: 3
        });

        links.push({
          source: this.person_info['姓名'],
          target: person['姓名'],
          label: {
            show: true,
            formatter: person['关系']
          }
        });
      }
    },
    initChart(nodes, links) {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      option = {
        tooltip: {
          formatter: function (params) {
            if(params.dataType === 'node') {
              if (params.data.node_type === 1 || params.data.node_type === 3) {
                const info = params.data.info;
                return `
                            <strong>${info['姓名']}</strong><br>
                            关系: ${info['关系']}<br>
                            年龄: ${info['年龄']}<br>
                            工作单位: ${info['工作单位']}<br>
                            职务: ${info['职务']}<br>
                            人员互动: ${info['人员互动']}
                        `;
              } else if (params.data.node_type === 2) {
                const info = params.data.info;
                return `
                            <strong>${info['真实姓名']}</strong><br>
                            关系: ${info['关系']}<br>
                            网名: ${info['网名']}<br>
                            年龄: ${info['年龄']}<br>
                            平台: ${info['平台']}<br>
                            性别: ${info['性别']}<br>
                            互动: ${info['互动']}
                        `;
              }
            }
          }
        },
        series: [
          {
            type: 'graph',
            layout: 'force',
            data: nodes,
            links: links,
            roam: true,
            label: {
              show: true,
              position: 'inside',
              fontSize: 12,
              color: '#fff' // 设置标签颜色为白色，以便在深色节点上可见
            },
            force: {
              repulsion: 1000,
              edgeLength: 200 // 设置连接线长度
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
