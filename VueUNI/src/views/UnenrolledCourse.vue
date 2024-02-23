<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20 flex items-center justify-between">
        <div>
            <h1 class="text-3xl font-sans font-bold">{{ course.code }} {{ course.name }}</h1>
        </div>
    </div>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto" >
        <h2 class="text-2xl font-sans font-bold p-5">Opciones de Matriculacion 🔑</h2>
        <div class="flex">
            <div class="mt-3 mx-1 w-[30%]">
                <div class="max-w-[343px] min-h-[395px] p-4 overflow-hidden shadow-md">
                    <img class="min-h-[50%]" :src="course.get_image" :alt="course.name">
                    <div class="px-6 py-4">
                        <div class="text-sm mb-2">{{ course.code }} {{ course.name }}</div>
                    </div>
                    <div class="h-[30%] space-x-1" v-for="professor in course.professors">
                        <router-link :to="{name:'profile',params:{id:professor.id}}" class="flex">
                            <img :src="professor.get_avatar" class="rounded-full max-w-[20%] inline-block" alt="Name of teacher">
                            <div class="inline-block w-full">
                                <p class="inline-blockpx-3 hover:underline py-1 text-[10.5px]  font-semibold ">{{ professor.first_name }} {{professor.last_name}}</p>
                                <p class=" bg-gray-200 rounded-full w-full text-[9px] px-3 py-1 font-semibold text-gray-700">Profesor</p>
                            </div>
                        </router-link>
                        
                    </div>
                </div>
            </div>
            <div class="mt-3 mx-1 w-[50%]">
                <template v-if="course.active">
                    <form  action="." method="post" class="w-full left m-2 text-right space-y-6" @submit.prevent="submitForm">
                        <div class="flex space-x-2 items-center">
                            <label>Codigo de Inscripcion:</label>
                            <input v-model="code" type="password" class="rounded-md w-[100%] border p-1 border-black" >
                            
                        </div>
                        <button class="w-1/2 p-2 active:scale-90 hover:bg-slate-800 duration-200 text-white bg-black">Inscribirse</button>
                    </form>
                    <button @click="addSolicitor" class="p-2 mx-2 hover:bg-gray-400 duration-200 bg-gray-500 text-white w-full">Solicitar Codigo</button>
                </template>
                <template v-else >
                    <div class="space-y-3 mx-5">
                        <h3>El curso actualmente se encuentra desactivado</h3>
                        <button @click="sendSolicitude" v-if="userStore.user.role === 'Student'" class="p-2 bg-green-500 border border-green-500 text-white hover:bg-white hover:text-green-500 duration-300 ">Solicitar Apertura</button>
                    </div>
                </template>
                
            </div>
        </div>
    </div>
</template>
<script>
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
    },
    data() {
        return {
            code: '',
            course:{},
        }
    },
    mounted() {
        this.getCourse()

    },
    methods: {
        async getCourse(){
            axios.get(`course/${this.$route.params.id}/`)
            .then(response => {
                this.course = response.data
                this.admin = this.course.admin
                
            })
            .catch(error => {
                console.log(error); 
            })
        },
        async submitForm(){
            let form = new FormData()
            form.append('validation',this.code)
            axios.post(`course/${this.$route.params.id}/validate-code/`,form,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            })
            .then(response =>{
                if (response.data.message === 'Enrollment was successful'){
                    this.$router.push({name:'course',params:{id:this.$route.params.id}})
                }
                else{
                    window.alert(response.data.message)
                }
            })
            .catch(error => {
                console.log(error);
            })
        },
        async sendSolicitude(){
            await axios.post(`course/opencourse/${this.$route.params.id}/`)
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
        async addSolicitor(){
            await axios.post(`course/${this.$route.params.id}/addsolicitor/`)
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
        
        
        
    },
}


</script>