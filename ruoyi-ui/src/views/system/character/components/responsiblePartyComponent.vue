<template>
  <div class="app-container">
    <div v-html="formattedResponsibleParty" class="text-center"></div>
  </div>
</template>

<script>
export default {
  name: 'ResponsiblePartyComponent',
  props: {
    data: {
      type: String,
      required: true
    }
  },
  computed: {
    formattedResponsibleParty() {
      try {
        const json = JSON.parse(this.data);
        return Object.keys(json).map(key => {
          return `<strong>${key}:</strong> ${json[key]}`;
        }).join('<br>');
      } catch (error) {
        console.error('Error parsing data:', error);
        return '';
      }
    }
  },
};
</script>

<style scoped lang="scss">

</style>
