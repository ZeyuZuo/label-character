<template>
  <div class="app-container">
    <div>
      <el-row :gutter="15">
        <el-form ref="elForm" :model="formData" :rules="rules" size="medium" label-width="100px">
          <el-col :span="5">
            <div :style="{ fontSize: '20px', textAlign: 'center', lineHeight: '30px' }">姓名: {{person_name}}</div>
          </el-col>
          <el-col :span="9">
            <el-form-item label="选择内容" prop="tag_num">
              <el-cascader v-model="formData.tag_num" :options="tag_numOptions" :props="tag_numProps"
                           :style="{width: '100%'}" placeholder="请选择选择查看内容" clearable></el-cascader>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item size="small">
              <el-button type="primary" @click="submitForm">提交</el-button>
              <el-button @click="resetForm">重置</el-button>
            </el-form-item>
          </el-col>
        </el-form>
      </el-row>
    </div>
    <div class="chart-container">
      <component :is="currentComponent" v-bind="componentProps"></component>
    </div>
  </div>
</template>
<script>

import RelationComponent from "@/views/system/character/components/relationComponent.vue";
import DoubleTimeLineComponent from "@/views/system/character/components/doubleTimeLineComponent.vue";
import TimeLineComponent from "@/views/system/character/components/timeLineComponent.vue";
import PersonComponent from "@/views/system/character/components/personComponent.vue";
import {getPersonInfo, getPersonTag} from "@/api/system/character";

export default {
  components: {},
  props: [],
  data() {
    return {
      id_card: '',
      person_name: '',
      person_info: {},
      person_tag: {},
      currentComponent: [], // 当前组件
      componentProps: {}, // 传递给当前组件的属性
      formData: {
        tag_num: [],
      },
      rules: {
        tag_num: [{
          required: true,
          type: 'array',
          message: '请至少选择一个tag_num',
          trigger: 'change'
        }],
      },
      tag_numOptions: [{
        "label": "个人特征",
        "value": 1,
        "id": 100,
        "children": [{
          "label": "个人信息",
          "value": 5,
          "id": 104
        }, {
          "label": "教育工作经历",
          "value": 6,
          "id": 105
        }, {
          "label": "责任主体",
          "value": 7,
          "id": 106
        }]
      }, {
        "label": "行为特征",
        "value": 2,
        "id": 101,
        "children": [{
          "label": "前科记录,非法活动",
          "value": 8,
          "id": 109
        }, {
          "label": "活动区域,近期车辆使用",
          "value": 9,
          "id": 110
        }, {
          "label": "资金情况",
          "value": 10,
          "id": 111
        }, {
          "label": "网络痕迹记录,社交媒体痕迹",
          "value": 11,
          "id": 112
        }, {
          "label": "购物信息记录",
          "value": 12,
          "id": 113
        }, {
          "label": "通信数据记录",
          "value": 13,
          "id": 114
        }, {
          "label": "书籍阅读记录",
          "value": 14,
          "id": 115
        }, {
          "label": "医疗记录",
          "value": 15,
          "id": 116
        }]
      }, {
        "label": "人物关系",
        "value": 3,
        "id": 102,
      }, {
        "label": "推断特征",
        "value": 4,
        "id": 103
      }],
      tag_numProps: {
        "multiple": false
      },
    }
  },
  computed: {},
  watch: {},
  async created() {
    this.id_card = this.$route.query.id_card;
    this.person_name = this.$route.query.name;
    console.log(this.id_card);
    if (!this.id_card) {
      alert('请先选择一个人物');
      await this.$router.push({path: '/character/people'});
    } else {
      await this.fetchData();
    }
  },
  mounted() {},
  methods: {
    submitForm() {
      this.$refs['elForm'].validate(valid => {
        if (valid) {
          // console.log(this.formData.tag_num);
          if (this.formData.tag_num.includes(6)) { // 教育经历,工作经历
            console.log('教育经历,工作经历');
            this.currentComponent = DoubleTimeLineComponent;
            this.componentProps = {
              leftName: '教育经历',
              rightName: '工作经历',
              leftData: this.person_tag['教育经历'],
              rightData: this.person_tag['工作经历']
            };
          } else if (this.formData.tag_num.includes(8)) { // 前科记录,非法活动
            this.currentComponent = DoubleTimeLineComponent;
            this.componentProps = {
              leftName: '前科记录',
              rightName: '非法活动',
              leftData: this.person_tag['前科记录'],
              rightData: this.person_tag['非法活动']
            };
          } else if (this.formData.tag_num.includes(9)) { // '活动区域轨迹,近期车辆使用情况'
            this.currentComponent = DoubleTimeLineComponent;
            this.componentProps = {
              leftName: '活动区域轨迹',
              rightName: '近期车辆使用记录',
              leftData: this.person_tag['活动区域轨迹'],
              rightData: this.person_tag['近期车辆使用记录']
            };
          } else if (this.formData.tag_num.includes(10)) { // '异常资金交易记录,贷款记录'
            this.currentComponent = DoubleTimeLineComponent;
            this.componentProps = {
              leftName: '异常资金交易记录',
              rightName: '贷款记录',
              leftData: this.person_tag['异常资金交易记录'],
              rightData: this.person_tag['贷款记录']
            };
          } else if (this.formData.tag_num.includes(11)) { //'网络痕迹记录,社交媒体痕迹'
            this.currentComponent = DoubleTimeLineComponent;
            this.componentProps = {
              leftName: '网络痕迹记录',
              rightName: '社交媒体痕迹',
              leftData: this.person_tag['网络痕迹记录'],
              rightData: this.person_tag['社交媒体痕迹']
            };
          } else if (this.formData.tag_num.includes(3)) { // 人物关系
            this.currentComponent = RelationComponent;
            this.componentProps = {
              person_info: this.person_info,
              person_tag: this.person_tag,
            };
          } else if (this.formData.tag_num.includes(12)) {
            this.currentComponent = TimeLineComponent;
            this.componentProps = {
              data: this.person_tag['购物信息记录']
            }
          } else if (this.formData.tag_num.includes(13)) {
            this.currentComponent = TimeLineComponent;
            this.componentProps = {
              data: this.person_tag['通信数据记录']
            }
          } else if (this.formData.tag_num.includes(14)) {
            this.currentComponent = TimeLineComponent;
            this.componentProps = {
              data: this.person_tag['书籍阅读记录']
            }
          } else if (this.formData.tag_num.includes(15)) {
            this.currentComponent = TimeLineComponent;
            this.componentProps = {
              data: this.person_tag['医疗记录']
            }
          } else if (this.formData.tag_num.includes(5)) {
            this.currentComponent = PersonComponent;
            this.componentProps = {
              data: this.person_info
            }
          }
        }
      })
    },
    resetForm() {
      this.$refs['elForm'].resetFields()
    },
    async fetchData() {
      // 获取人物信息
      // 获取人物tag
      const personInfoPromise = getPersonInfo(this.id_card, 5).then(response => {
        this.person_info = response.data.data;
      });
      const personTagPromise = getPersonTag(this.id_card).then(response => {
        this.person_tag = response.data.data;
      });

      await Promise.all([personInfoPromise, personTagPromise]);
      // this.person_name = this.person_info['姓名'];
    }
  }
}

</script>
<style>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Ensure the container takes full viewport height */
}

.chart-container {
  flex: 1; /* Allow this div to take up remaining space */
}
</style>
