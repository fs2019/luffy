<template>
  <div class="home">
    <Header></Header>
    <Banner></Banner>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './common/Header'
import Banner from './common/Banner'
import Footer from './common/Footer'
export default {
  name: 'Home',
  data () {
    return {}
  },
  methods:{
  },
  components:{
    Header,
    Banner,
    Footer
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
