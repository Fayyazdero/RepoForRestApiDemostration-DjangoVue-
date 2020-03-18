<template>

  <div class="">
        <div class="row">
          <div class="col-md-12 text-center">
              <h3>The Limit is your Imagination!</h3>
              <br>
               <b-button  v-on:click="getVideos">Get All the Videos</b-button>

              </div>

        </div>
 
      <div class="row">
    

           <div class="col-md-6 text-center">
               <p v-bind:key="item.id" v-for="item in videos">
            <br>
            Video Title: {{item.title}}
            <br>
            Rating: {{item.average_ratings}}
            <br>
            Comments: {{item.comments_list[0]}}
            <br/>
            <button class="btn-sm btn-primary" v-on:click="Detailview(item)">View Details</button>

          </p>
         
           </div>

          <div class="col-md-6 text-center">
            <Detailview/>
       </div>
            </div>

      </div>


     
</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'   #New Removed the component

import axios from 'axios';
import Detailview from './Detailview'


export default {
  name: 'Home',
  components: {
    Detailview
  },

  // New
  data(){
return{
  videos : [], 
  Detailview : Object,
  
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
    Detailideo(item){
      this.detailview = item;
      console.log(this.detailview)

  },

  created(){
    this.getVideos()
    this.Detailview()
  }
}
</script>