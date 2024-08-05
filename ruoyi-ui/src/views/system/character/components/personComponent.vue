<template>
  <div class="app-container">
    <div class="card">
      <div class="card-title">个人信息</div>
      <div class="card-content">
        <div class="top-section">
          <div class="info">
            <div v-for="(value, key) in personalInfoTop" :key="key" class="info-item">
              <strong>{{ key }}:</strong> {{ value }}
            </div>
          </div>
          <div class="avatar">
            <img src="/assets/image.png" alt="头像" />
          </div>
        </div>
        <hr />
        <div class="bottom-section">
          <div v-for="(value, key) in personalInfoBottom" :key="key" class="info-item">
            <strong>{{ key }}:</strong> {{ value }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PersonComponent",
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      personalInfoTop: {
        "身份证号码": "123456789012345678",
        "姓名": "张三",
        "曾用名": "张三三",
        "绰号": "三哥",
        "联系电话": "13800000000",
        "性别": "男",
        "年龄": 30,
        "身高": 175,
        "体重": 70,
      },
      personalInfoBottom: {
        "血型": "O",
        "民族": "汉族",
        "重点人员类型": "无",
        "教育程度": "本科",
        "职业": "软件工程师",
        "工作单位": "某科技公司",
        "出生地": "北京市",
        "户籍所在地": "北京市海淀区",
        "常住地": "北京市朝阳区",
        "家庭人口": 3,
        "思想倾向": "中立",
        "兴趣爱好": "读书, 旅游, 运动",
        "政治面貌": "群众",
        "宗教信仰": "无",
        "祖籍": "山东省",
        "特殊经历": "曾在某公司担任项目经理",
        "特殊外表与标记": "左手有胎记",
        "犯罪技能": "无",
        "婚姻状况": "未婚"
      }
    };
  },
  mounted() {
    console.log("Personal Info:", this.data);
  }
};
</script>

<style>

.card {
  left: 50%;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 90%; /* Increase width to 90% */
  max-width: 1000px; /* Increase max-width */
  padding: 20px;
  max-height: 90vh; /* Set a maximum height */
  overflow-y: auto; /* Allow vertical scrolling */
  margin: 0 auto; /* Center the card horizontally */
}

.card-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
}

.card-content {
  display: flex;
  flex-direction: column;
}

.top-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 5px;
}

.info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.info-item {
  margin-bottom: 10px;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

hr {
  border: none;
  border-top: 1px solid #ddd;
  margin: 20px 0;
}

.bottom-section {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.info-item {
  width: 30%; /* Adjust width to 30% */
  margin-bottom: 10px;
}
</style>
