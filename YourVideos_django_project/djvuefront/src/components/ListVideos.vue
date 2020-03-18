<template>
  <div class="">
      <div class="row">
          <div class="col-md-12 text-center">
              <h3>Say Yes to Your Imagination</h3>
          <button v-on:click="getVideos">Get the Videos</button>

           <div class="col-md-12 text-center">
               <p v-bind:key="item.id" v-for="item in videos">
            <br>
            Video Title: {{item.title}}
            <br>
            Rating: {{item.average_ratings}}
            <br>
            Comments: {{item.comments_list[0]}}
          </p>

           </div>
            <button class="btn-sm btn-primary">View Full Details</button>

         
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
      .then(res=>(this.videos=res.data))
      // .then(res=>console.log(res.data))
      .catch(err=>console.log(err));
      console.log(this.videos)

    }
  },
  created(){
    this.getVideos()
  }
}
</script>
