<template>

  <div class="home">
    
    <ListVideos msg="Welcome to Your Vue.js App"/>
    <!-- <Detailview msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'   #New Removed the component
import ListVideos from '@/components/ListVideos.vue'   
import DetailView from '@/components/Detailview.vue'   

export default {
  name: 'Home',
  components: {
    ListVideos,
    DetailView
  }
}
</script>
