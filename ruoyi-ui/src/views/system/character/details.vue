<template>
  <div class="app-container">
    <h1>人物详情</h1>
    <h2>{{id_card}}</h2>
  </div>
</template>

<script>
export default {
  name: 'CharacterDetails',
    data() {
    return {
      id_card: '',
      personDetails: {}
    }
  },
  created() {
    this.id_card = this.$route.query.id_card;
    console.log(this.id_card);
    // 根据id_card查询详细信息
    // this.fetchDetails();
  },
  methods: {
    // fetchDetails() {
    //   getPersonDetails(this.id_card).then(response => {
    //     this.personDetails = response.data;
    //   });
    // }
  }
}
</script>


<style scoped lang="scss">

</style>
