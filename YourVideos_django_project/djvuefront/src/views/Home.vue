<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <ListVideos msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'   #New Removed the component
import ListVideos from '@/components/ListVideos.vue'   

export default {
  name: 'Home',
  components: {
    ListVideos
  }
}
</script>
