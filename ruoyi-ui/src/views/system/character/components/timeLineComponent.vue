<template>
  <div class="container">
    <div class="timeline-container">
<!--      <div class="vertical-line"></div>-->
      <div v-for="(record, index) in buildHtml" :key="index" class="timeline-item">
        <div v-html="record.details"></div>
      </div>
      <!--    <div v-show=isVisible class="divider"></div>-->
    </div>
    <div v-show=isVisible class="guess">
      <div v-html="guessContent"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TimeLineComponent',
  props: {
    data: {
      type: String,
      required: true
    },
    guess: {
      type: String,
      required: false
    },
    guessData: {
      type: String,
      required: false
    }
  },
  computed: {
    buildHtml() {
      if(this.guess) {
        this.isVisible = true;
        this.guessContent = this.formattedGuessData();
      } else {
        this.isVisible = false;
      }
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
    formattedGuessData() {
      try {
        return `<strong>${this.guess}:</strong><br><p>${this.guessData}</p>`
      } catch (error) {
        console.error('Error parsing guessData:', error);
        return '';
      }
    }
  },
  data() {
    return {
      guessContent: '',
      isVisible: false
    };
  }
}
</script>

<style>
.timeline-item {
  position: relative;
  width: 60%;
  padding: 10px;
  box-sizing: border-box;
  text-align: left;
  left: 0;
  margin-bottom: 20px; /* Add some space between items */
}

.container {
  display: flex;
}

.timeline-container {
  position: relative; /* Make this container the reference point for absolute positioning */
  padding: 0 0 60px 0;
  width: 40%;
  margin: auto;
  height: 100%;
  overflow-y: auto;
  max-height: 100vh;
}

.guess {
  width: 20%;
  padding: 20px;
  overflow: auto;
}

</style>
