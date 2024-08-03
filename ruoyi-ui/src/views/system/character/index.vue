<template>
  <div class="app-container">
    <el-form :model="queryPersonParams" ref="queryPersonParams" size="small" :inline="true" v-show="showSearch" label-width="68px">
      <el-form-item label="身份证号" prop="id_card">
        <el-input v-model="queryPersonParams.id_card" placeholder="请输入身份证号" clearable @keyup.enter.native="queryPerson"/>
      </el-form-item>
      <el-form-item label="姓名" prop="name">
        <el-input v-model="queryPersonParams.name" placeholder="请输入姓名" clearable @keyup.enter.native="queryPerson"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="queryPerson">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>

    <el-table v-if="refreshTable" v-loading="loading" :data="personList" row-key="id_card">
      <el-table-column label="姓名" align="left" prop="name" />
      <el-table-column label="身份证号" align="left" prop="id_card" />
      <el-table-column label="年龄" align="left" prop="age" />
      <el-table-column label="性别" align="left" prop="gender" />
      <el-table-column label="户籍所在地" align="left" prop="address" />

      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button size="mini" type="text" icon="el-icon-edit" @click="seeDetails(scope.row)">查看详情</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
import {listPerson} from "@/api/system/character";

export default {
  name: 'character',
  components: {},
  props: [],
  data() {
    return {
      showSearch: true,
      loading: true,
      refreshTable: true,
      personList: [],
      queryPersonParams: {
        id_card: '',
        name: ''
      }
    }
  },
  computed: {},
  watch: {},
  created() {
    this.queryPerson();
  },
  mounted() {},
  methods: {
    /* 搜索人的信息 */
    queryPerson() {
      this.loading = true;
      // alert('id_card:'+this.queryPersonParams.id_card)
      // alert('name:'+this.queryPersonParams.name)
      listPerson(this.queryPersonParams).then(response => {
        // console.log(response);
        // console.log(response.data);
        this.personList = response.data.data
        // console.log(this.personList)
        this.loading = false;
      })
    },
    // 重置并搜索
    resetQuery() {
      this.resetForm("queryPersonParams");
      this.queryPerson();
    },
    // 查看人物详情
    seeDetails: function(row) {
      // 跳转到详情页并带上id_card参数
      console.log(row.id_card);
      this.$router.push({
        path: '/character/peopleInfo',
        query: {
          id_card: row.id_card
        }
      });
    },
  }
}
</script>
