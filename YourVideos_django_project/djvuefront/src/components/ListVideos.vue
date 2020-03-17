<template>
  <div class="">
      <div class="row">
          <div class="col-md-12 text-center">
              <h3>Say Yes to Your Imagination</h3>
          <button v-on:click="getVideos">Get the Videos</button>

          </div>

      </div>

  </div>
</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'   #New Removed the component

import axios from 'axios'


export default {
  name: 'Home',
  components: {
    
  },

  // New
  data(){
return{
  videos : [], 
}

  },
  methods:{   
    getVideos(){
      axios.get('http://127.0.0.1:8000/api/videos/')
      // .then(res=>(this.videos=res.data))
      .then(res=>console.log(res.data))
      .catch(err=>console.log(err));
      console.log(this.videos)

    }
  }
}
</script>
