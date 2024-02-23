<template>
    <Navbar/>
    <Banner v-bind:user="user"/>
    <div class="bg-white max-w-[80vw] space-y-4 rounded-md p-3 mx-auto mt-4" >
        <div class="flex justify-between w-full items-center">
            <div class="p-5">
                <h2 class="text-2xl font-sans font-bold">Blog de {{ user.first_name }} 📱</h2>
                <h3 v-if="blog.my_followers">{{ blog.my_followers }} Seguidores ⚰</h3>
            </div>
            
            <div class="space-x-3 flex items-center">
                <label v-if="$route.params.id == userStore.user.id && message == 'no'" class="relative inline-flex items-center cursor-pointer">
                    <input type="checkbox" v-model="public" class="sr-only peer">
                    <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
                    <span class="ms-1 text-sm font-medium text-black select-none">Publico</span>
                </label>
                <button v-if="$route.params.id != userStore.user.id && !follow" @click="follower"  class=" m-1 active:scale-90 transition duration-200 p-2 rounded-md text-white hover:bg-blue-500 bg-blue-600 ">Suscribirse</button>
                <button v-if="$route.params.id != userStore.user.id && follow" @click="unfollow" class=" m-1 p-2 active:scale-90 transition duration-200 rounded-md text-white hover:bg-zinc-900 bg-zinc-950 ">Desuscribirse</button>
                <button v-if="$route.params.id == userStore.user.id && message == 'no'" @click="createBlog" class=" m-1 text-white p-2 active:scale-90  transition duration-200 rounded-md hover:bg-green-400 bg-green-500 ">Crear Blog</button>
                <router-link v-if="$route.params.id == userStore.user.id && message != 'no'"  :to="{name:'blogpost',params:{id:user.id}}" class=" m-1 active:scale-90  transition duration-200 text-white p-2 rounded-md hover:bg-slate-400 bg-slate-500 ">Crear Post</router-link>
                <button v-if="$route.params.id == userStore.user.id && message != 'no' " @click="deleteBlog" class=" m-1 p-2 rounded-md text-white active:scale-90  transition duration-200 hover:bg-red-500 bg-red-600 ">Eliminar Blog</button>                
            </div>
        </div>
        
        
        <div  v-for="post in posts" :key="post.id" :id="post.id" >
            <div class="w-[75vw] mx-auto bg-gray-300 m-3 rounded-2xl p-3" v-if="$route.params.id === userStore.user.id || post.visible === true || itisfollow===true">
                <div class="flex space-x-3">
                    <img :src="user.get_avatar" class="rounded-full w-[5%]" alt="myface">
                    <div>
                        <h1 class="font-bold">{{ post.subject }}</h1>
                        <p>de {{ user.first_name }} {{ user.last_name }} - {{ post.created_at_formatted }}</p>
                    </div>
                </div>
                <div class="my-2 p-2">
                    {{ post.body }}

                    <img v-if="post.get_image" class="m-4 p-2 mx-auto" :src="post.get_image" :alt="post.subject">
                    <template v-if="post.get_file" >
                        <a :href="post.get_file" class="hover:underline text-blue-600 ">Descarga el archivo aqui</a>
                    </template> 

                    
                </div>
                <div class="flex space-x-2">
                    <div class="flex space-x-2" v-if="$route.params.id == userStore.user.id">
                        <router-link :to="{ name:'editPost', params:{id:$route.params.id,pk:post.id} }"><svg class="feather feather-edit-2" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg></router-link>
                        <button @click="deletePost(post.id)" ><svg class="feather feather-trash-2" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/><line x1="14" x2="14" y1="11" y2="17"/></svg></button>       
                    </div>
                    <div class="flex items-center space-x-2">
                        <svg @click="like(post.id)" :id="'like-'+post.id" class="feather cursor-pointer  text-black feather-thumbs-up" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"/></svg>
                        <p>{{ post.count_of_likes }} like</p>
                    </div>
                    <template v-if="post.visible">
                        <button v-if="$route.params.id == userStore.user.id" @click="changevisible(post.id)"><svg class="feather feather-eye text-black" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></button>
                    </template>
                    <template v-else>
                        <button v-if="$route.params.id == userStore.user.id" @click="changevisible(post.id)"><svg class="feather feather-eye-off text-black" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" x2="23" y1="1" y2="23"/></svg></button>
                    </template>
                    
                </div>
            </div>
            
        </div>
        
        
    </div>
</template>
<script>
//fill-black
import Navbar from '@/components/Navbar.vue';
import Banner from '@/components/Banner.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios'
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'Chat',
    components:{
        Navbar,
        Banner,
    },
    data() {
        return {
            user: {},
            blog : {},
            posts: [],
            message: '',
            public: false,
            follow: false,
            itisfollow: false
        }
    },
    created() {

        this.existBlog()
    },
    mounted() {
        
        
        
        this.getUser()
        if (this.userStore.user.id !== this.$route.params.id){

            this.isfollowing()
            this.issuscriber()
        }
        if (this.message !='no' ){
            this.getPosts()
        }
        
    },

    methods: {
        async issuscriber(){
            await axios.get(`blog/${this.$route.params.id}/isfollowing/`)
            .then(response =>{
                if (response.data.is_following ) { 
                    this.itisfollow = true
                }
                else {
                    this.itisfollow = false
                }
            }) 
            .catch(error => { 
                console.log(error);
            })
        },
        async changevisible(id){
            await axios.post(`blog/post/${id}/change/`)
            let post = this.posts.find(object => object.id === id)
            post.visible = !post.visible
        },
        async unfollow(){
            await axios.delete(`blog/${this.$route.params.id}/unfollow/`)
            .then(response => {
                console.log("You're leave this blog");
                this.blog.my_followers-=1
                this.follow = false
            })
            .catch(error =>{
                console.log(error);
            })
        },
        async follower(){
            await axios.post(`blog/${this.$route.params.id}/follow/`)
            .then(response => {
                console.log("Now you're following this blog");
                this.blog.my_followers+=1
                this.follow = true
            })
            .catch(error =>{
                console.log(error);
            })
        },
        async isfollowing(){
            await axios.get(`blog/${this.$route.params.id}/isfollowing/`)
            .then(response => {
                this.follow = response.data.is_following

                console.log(response.data.is_following);
            })
            .catch(error =>{
                console.log(error); 
            })
        },
        async deleteBlog(){
            await axios.delete(`blog/${this.$route.params.id}/destroy/`)
            .then(response => {
                this.$router.push({name:'profile',params:{id:this.$route.params.id}})
            })
            .catch(error => {
                console.log(error);  
            })
        },
        async createBlog(){
            await axios.post(`blog/${this.$route.params.id}/create/`,{
                public: this.public
            })
            .then(response => {
                this.$router.go()
            })
            .catch(error =>{
                console.log(error);
            })
        },
        async getUser(){
            await axios.get(`user/${this.$route.params.id}/`)
            .then(response => {
                this.user = response.data 
            })
            .catch(error => { 
                console.log(error);
            })
        },
        async existBlog() {
            try {
                const response = await axios.get(`blog/${this.$route.params.id}/exist/`);  // Echar un ojo
                if (response.data.state === 'yes') {
                    const response1 = await axios.get(`blog/${this.$route.params.id}/`);
                    this.blog = response1.data;
                    if (!this.blog.public && this.userStore.user.id !== this.$route.params.id) {
                        console.log(this.blog.public);
                        console.log(this.userStore.user.id);
                        console.log(this.$route.params.id);
                        this.$router.push({ name: 'notAllowed' });
                    }
                } else {
                    this.blog.public = false;
                    this.message = 'no';
                    if (!this.blog.public && this.userStore.user.id !== this.$route.params.id) {
                        this.$router.push({ name: 'notAllowed' });
                    }
                }
            } catch (error) {
                console.error(error);
            }
        },
        async getPosts(){
            await axios.get(`blog/${this.$route.params.id}/posts/`)
            .then(response =>{
                this.posts = response.data
            }) 
            .catch(error => {
                console.log(error);
            })
        }, 
        async deletePost(id){
            await axios.delete(`blog/posts/delete/${id}/`)
            .then(response => {
                console.log(response.data);
                let value = document.getElementById(`${id}`)
                value.setAttribute("hidden", true);
            })
            .catch(error => {
                console.log(error);
            })
        },
        
        async like(id){
            let given = false
            await axios.get(`blog/like/${id}/was-given/`)
            .then(response => {
                if (response.data.message === 'True'){
                    given = true
                }
            })
            .catch(error =>{
                console.log(error);
            })
            if (given){
                await axios.delete(`blog/like/${id}/delete/`)
                .then(response => {
                    
                    let value = this.posts.find(object => object.id === id)
                    value.count_of_likes-=1
                })
                .catch(error => {
                    console.log(error);
                })
            }
            else{
                await axios.post(`blog/like/${id}/create/`)
                .then(response => {
                    let value = this.posts.find(object => object.id === id)
                    value.count_of_likes+=1
                })
                .catch(error => {
                    console.log(error);
                })
            }

        }
    },
    
}

</script>