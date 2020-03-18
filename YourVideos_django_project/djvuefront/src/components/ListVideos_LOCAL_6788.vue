<template>
  <div class="container" style="width: 500px">
    <div class="row">
      <div class="col-md-12" style="display: flex;">
        <img
          src="https://images.unsplash.com/photo-1453591954336-1b50a3f6c27f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
          alt="image"
          style="height: 100px; width: 100px;"
        />
        <h3>
         Mara pass
          <span
            style="display: block; font-size: 1.5rem;"
          >Watch full video to contact naveed!</span>
        </h3>
        <button v-on:click="getVideos">Get the Videos</button>
      </div>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'   #New Removed the component
import axios from "axios";

export default {
  name: "Home",
  components: {},

  // New

  data() {
    return {
      videos: []
    };
  },

  methods: {
    getVideos() {
      axios
        .get("http://127.0.0.1:8000/api/videos/")
        .then(res => (this.videos = res.data))
        .catch(err => console.log(err));
      console.log(this.videos);
    }
  }
};
</script>
