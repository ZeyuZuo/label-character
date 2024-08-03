<template>
  <div class="container">
    <div class="left">
      <h2>{{ this.leftName }}</h2>
      <ul class="timeline">
        <li v-for="(item, index) in formattedLeftData" :key="index" class="timeline-item">
          <div class="timeline-content">
<!--            <p><strong>时间:</strong> {{ item.time }}</p>-->
            <p v-html="item.details"></p>
          </div>
        </li>
      </ul>
    </div>
    <div class="divider"></div>
    <div class="right">
      <h2>{{ this.rightName }}</h2>
      <ul class="timeline">
        <li v-for="(item, index) in formattedRightData" :key="index" class="timeline-item">
          <div class="timeline-content">
<!--            <p><strong>时间:</strong> {{ item.time }}</p>-->
            <p v-html="item.details"></p>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DoubleTimeLineComponent',
  props: {
    leftName: {
      type: String,
      required: true
    },
    rightName: {
      type: String,
      required: true
    },
    leftData: {
      type: String,
      required: true
    },
    rightData: {
      type: String,
      required: true
    }
  },
  mounted() {
    console.log('Left:', this.leftName);
    console.log('Right:', this.rightName);
    console.log('Left Data:', this.leftData);
    console.log('Right Data:', this.rightData);
  },
  computed: {
    formattedLeftData() {
      try {
        const left = JSON.parse(this.leftData);
        const sortedKeys = Object.keys(left).sort((a, b) => a - b);
        return sortedKeys.map(key => {
          const item = left[key];
          return {
            details: Object.keys(item).map(k => `<strong>${k}:</strong> ${item[k]}`).join('<br>')
          };
        });
      } catch (error) {
        console.error('Error parsing leftData:', error);
        return [];
      }
    },
    formattedRightData() {
      try {
        const right = JSON.parse(this.rightData);
        const sortedKeys = Object.keys(right).sort((a, b) => a - b);
        return sortedKeys.map(key => {
          const item = right[key];
          return {
            details: Object.keys(item).map(k => `<strong>${k}:</strong> ${item[k]}`).join('<br>')
          };
        });
      } catch (error) {
        console.error('Error parsing rightData:', error);
        return [];
      }
    }
  },
  data() {
    return {};
  }
};
</script>

<style>
.container {
  display: flex;
  height: 100vh;
}

.left, .right {
  width: 50%;
  padding: 20px;
  overflow-y: auto;
}

.divider {
  width: 2px;
  background-color: #000;
}

.timeline {
  list-style-type: none;
  padding: 0;
}

.timeline-item {
  margin: 20px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  background-color: #f9f9f9;
}

.timeline-content {
  display: flex;
  flex-direction: column;
}

.timeline-content h3 {
  margin: 0 0 10px;
}
</style>
