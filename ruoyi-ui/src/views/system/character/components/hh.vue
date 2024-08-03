<template>
  <div class="timeline-container">
    <div v-for="(record, index) in buildHtml" :key="index" class="timeline-item" :class="{'left': isLeft(index), 'right': !isLeft(index)}">
      <div v-html="record.details"></div>
    </div>
    <div class="vertical-line"></div>
  </div>
</template>

<script>
export default {
  name: 'TimeLineComponent',
  props: {
    data: {
      type: String,
      required: true
    }
  },
  computed: {
    buildHtml() {
      try {
        const data = JSON.parse(this.data);
        const sortedKeys = Object.keys(data).sort((a, b) => a - b);
        return sortedKeys.map(key => {
          const item = data[key];
          return {
            details: Object.keys(item).map(k => `<strong>${k}:</strong> ${item[k]}`).join('<br>')
          };
        });
      } catch (error) {
        console.error('Error parsing data:', error);
        return [];
      }
    }
  },
  methods: {
    isLeft(index) {
      return index % 2 === 0;
    }
  }
}
</script>

<style scoped>
.timeline-container {
  position: relative;
  padding: 20px 0;
  width: 80%;
  margin: auto;
  height: 90%;
}

.vertical-line {
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 4px;
  background-color: #2196F3;
}

.timeline-item {
  position: relative;
  width: 45%;
  padding: 10px;
  box-sizing: border-box;
}

.timeline-item.left {
  right: 0;
  text-align: right;
}

.timeline-item.right {
  left: 55%;
  text-align: left;
}

.timeline-item .content {
  background-color: #f9f9f9;
  padding: 15px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.timeline-item.left .content {
  margin-right: 20px;
}

.timeline-item.right .content {
  margin-left: 20px;
}
</style>
