<template>
    <Navbar/>
    <NavCourse/>
    <div class="max-w-screen-2xl m-5 mx-20 flex items-center justify-between">
        <div>
            <h1 class="text-3xl font-sans font-bold">{{ course.code }} {{ course.name }}</h1>
            <p>Supervisor: {{ admin.name }}</p>
        </div>
        <div v-if="userStore.user.role === 'Professor'"  >
            <router-link v-if="course.active" :to="{name:'addMaterials',params:{id:$route.params.id}}" class="p-3 bg-black hover:text-black border-black border hover:bg-white active:scale-90 transition duration-300 text-white font-normal">Añadir datos</router-link>
            <button v-else @click="setAvailable" class="p-2 bg-green-500 border border-green-500 text-white hover:bg-white hover:text-green-500 duration-300 ">Aperturar Curso</button>
        </div>

    </div>  
    <div class="bg-white max-w-[85vw] p-6 rounded-md mx-auto space-y-6" >
        <h1 class="text-2xl font-sans font-bold">General</h1>
        <template v-if="!forumexist && userStore.user.role === 'Professor'"> 
            <div class="w-full p-4 overflow-hidden shadow-md">
                <button @click="createForum" class="flex text-blue-600 hover:underline items-center space-x-3">
                    <div class="bg-orange-600 p-5 rounded-xl">
                        <svg class="feather feather-message-square text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    </div>
                    <p>Crear el Foro</p>
                </button>
            </div>
        </template>
        <template v-else-if="forumexist"> 
            <div class="w-full p-4 overflow-hidden shadow-md">
                <router-link :to="{name:'forum',params:{id:forum.id}}" class="flex text-blue-600 hover:underline items-center space-x-3">
                    <div class="bg-orange-600 p-5 rounded-xl">
                        <svg class="feather feather-message-square text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    </div>
                    <p>Ingresar al Foro</p>
                </router-link>
            </div>
        </template>
        
        <h1 class="text-2xl font-sans font-bold">Material del Curso</h1>
        <div v-for="(material, index) in materials" :key="index">
            <div class="w-full p-4 overflow-hidden shadow-md" v-if="material.is_visible == true || userStore.user.role == 'Professor'">
                <template v-if="material.materialtype === 'PDF'">
                    <div class="flex text-blue-600 items-center justify-between" >
                        <a :href="material.get_file" class="flex hover:underline items-center space-x-3">
                            <div class="bg-blue-500 p-5 rounded-xl">
                                <svg class="feather feather-file-minus text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" x2="15" y1="15" y2="15"/></svg>
                            </div>
                            <p>{{ material.name }}</p>
                        </a>
                        <div class="flex items-center space-x-3" v-if="userStore.user.role == 'Professor'">
                            <template v-if="material.is_visible">
                                <button @click="changevisible(material.id)"><svg class="feather feather-eye text-black" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></button>
                            </template>
                            <template v-else>
                                <button @click="changevisible(material.id)"><svg class="feather feather-eye-off text-black" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" x2="23" y1="1" y2="23"/></svg></button>
                            </template>
                            <router-link :to="{name:'editMaterials',params:{id:$route.params.id,pk :material.id}}" v-if="userStore.user.role === 'Professor'" class="rounded-xl p-1 bg-black hover:bg-slate-800 active:scale-90 transition duration-300 text-white font-normal">Editar</router-link>
                        </div>
                    </div>
                </template>
                <template v-else>
                    <div  class="flex text-blue-600 items-center justify-between">
                        <a :href="material.link" class="flex hover:underline items-center space-x-3">
                            <template v-if="material.materialtype === 'Videos'">
                                <div class="bg-purple-700 p-5 rounded-xl">
                                    <svg class="feather feather-monitor text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><rect height="14" rx="2" ry="2" width="20" x="2" y="3"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg>
                                </div>
                                <iframe width="420" height="315" frameborder="0"
                                    :src="material.get_link_embed">
                                </iframe>
                            </template>
                            <template v-else-if="material.materialtype === 'Urls'">
                                <div class="bg-green-600 p-5 rounded-xl">
                                    <svg class="feather feather-globe text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10"/><line x1="2" x2="22" y1="12" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                                </div>
                            </template>
                            <template v-else-if="material.materialtype === 'News'">
                                <div class="bg-orange-600 p-5 rounded-xl">
                                    <svg class="feather feather-message-square text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                                </div>
                            </template>
                            <p>{{ material.name }}</p>
                        </a>
                        <div class="flex items-center space-x-3" v-if="userStore.user.role == 'Professor'">
                            <template v-if="material.is_visible">
                                <button @click="changevisible(material.id)"><svg class="feather feather-eye text-black" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg></button>
                            </template>
                            <template v-else>
                                <button @click="changevisible(material.id)"><svg class="feather feather-eye-off text-black" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" x2="23" y1="1" y2="23"/></svg></button>
                            </template>
                            
                            <router-link :to="{name:'editMaterials',params:{id:$route.params.id,pk :material.id}}"  v-if="userStore.user.role === 'Professor'" class="rounded-xl p-1 bg-black hover:bg-slate-800 active:scale-90 transition duration-300 text-white font-normal">Editar</router-link>
                        </div>
                        
                    </div>
                </template>
                
            </div>
        </div>
        

        
        
    </div>
</template>
<script>
import NavCourse from '@/components/NavCourse.vue';
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user';

import axios from 'axios'
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'Notification',
    components:{
        Navbar,
        NavCourse,
    },
    data() {
        return {
            course:{},
            admin:{},
            materials:[],
            forumexist : false,
            forum: {
            }
        }
    },

    created(){
        this.imin()
    },
    mounted() {
        
        this.getCourse()
        this.getMaterials()
        this.forumExist()
        this.getForum()
    },
    methods: {
        async imin(){
            await axios.get(`course/${this.$route.params.id}/verifyuser/`)
            .then(response =>{
                if (!response.data.state){
                    this.$router.push({name:'enrollCourse',params:{id:this.$route.params.id}})
                }
            })
        },
        async createForum(){
            await axios.post(`chat/forum/${this.$route.params.id}/create/`)
            .then(response => {
                this.$router.go()
            })
        },
        async getForum(){
            await axios.get(`chat/forum/${this.$route.params.id}/`)
            .then(response => {
                console.log(response.data);
                this.forum = response.data[0]
            })
            .catch(error => {
                console.log(error);
            })
        },
        async forumExist(){
            await axios.get(`course/forumexist/${this.$route.params.id}/`)
            .then(response => {
                if (response.data.status){
                    this.forumexist = true
                }
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getCourse(){
            await axios.get(`course/${this.$route.params.id}/`)
            .then(response => {
                this.course = response.data
                this.admin = this.course.admin
            })
            .catch(error => {
                console.log(error); 
            })
        },
        async getMaterials(){
            axios.get(`course/${this.$route.params.id}/materials/`)
            .then(response =>{
                this.materials = response.data
                
            })
            .catch(error => {
                console.log(error);
            })
        },
        async setAvailable(){
            await axios.post(`course/setavailable/${this.$route.params.id}/`)
            .then(response => {
                console.log(response.data);
                this.$router.push({name:'pageauth'})
            })
            .catch(error => {
                console.log(error);
            })
        },
        async changevisible(pk){

            await axios.post(`course/material/${pk}/visibility/`)
            .then(response => { 
                console.log(response.data);
            })
            .catch(error => [
                console.log(error)
            ])

            this.getMaterials()
        }
    },
}


</script>