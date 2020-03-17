***Major Objective***

    1. Building an API in the django rest_framework
    2. Binding that framework with the frontend(in this case VUE.JS)


***Lets Get Started***


>>>         FIRST STEP(getting started)

        1. Created a virtualenv with the name(Djvue)source Djvue/bin/activate.
        2. Created an project in the virtualenv (Djvue).
        3. Needed an app an api to be specific, so done, with the name(YourApi).
        4. Applied migartions, and Successfully launched the server.
        


>>>        SECOND STEP(creating models and handeling the routing)


        1. Adding the appname and (rest_framework) we created to the installed_apps list in the settings.py file(rooy directory.
        2. introduced the urls.py file
        3. Importing routers and working with them
        4. Cerated some tabels and migrated them
        5. Created a (serializers.py) file for serializing the models
        6. Serialized all the three models and added nessasory details
        7. We created the views for each, under classes and have the logic needed to manipulate the basic functionality of the app.
        8. Integrated Kite with vs code.
        9. Just informed django by writting the permissions description in the settings.py file, as usual.

>>>        Urls.py

        1. Firstly register all the viewsets.




>>>            ***Vue Part***


        1. Installed npm
        2. initiated an app using the (VUE CLI)
        3. installed the bootstrap-vue inside the frontend-app(djvuefront)(npm install bootstrap-vue)
        4. also for making HTTP requests to the backend we need (axios, a libirary for making connection)
        5. Add all the nessary imports needed,  and the requirments

              1.npm install vue bootstrap-vue bootstrap
                import Vue from 'vue'
                import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

                  2.   // Install BootstrapVue
                        Vue.use(BootstrapVue)
                        // Optionally install the BootstrapVue icon components plugin
                        Vue.use(IconsPlugin)

                       3.  import 'bootstrap/dist/css/bootstrap.css'
                           import 'bootstrap-vue/dist/bootstrap-vue.css'

        
>>>             Building components in vue


        1. Firstly Remove the pre-built component(The helloworld component)
        2. Also remove all the mentions of the component just removed (specifically from the home.vue file)
        3. Create a new vue component(ListVideos.vue)
        4. Now in the new component we can use the code structure from the home vue except for some changes
        5. 
