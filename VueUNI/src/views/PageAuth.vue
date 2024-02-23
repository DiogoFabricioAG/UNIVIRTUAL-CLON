<template >
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <h1 class="text-2xl font-sans font-bold">¡Hola, {{ userStore.user.last_name }}! 👋</h1>
    </div>  
    <div class="bg-white max-w-[80vw] rounded-md mx-auto" >
        <template v-if="courses.length">
            <div class="flex w-full justify-between items-center">
                <h2 v-if="courses.length" class="text-2xl font-sans font-bold p-5">Mis cursos 📚</h2>
                <router-link :to="{name:'createcourse'}" v-if="userStore.user.role === 'Professor'" class="p-2 bg-green-500 mr-2 hover:bg-white border border-green-500 hover:text-green-500 duration-300 text-white">Crear Curso</router-link>
            </div>
            <div class="flex flex-wrap w-full">
                <router-link :to="{name : 'course',params:{id:course.id}}" class="mt-3 mx-auto relative z-5 active:scale-95 duration-300 transition-transform" v-for="course in courses" :key="course.id">
                <div v-if="userStore.user.role == 'Professor'">
                    <button class="absolute bg-black p-2 rounded-full right-5 active:scale-95 top-5 z-10" @click.prevent="$router.push({name:'setKey',params:{id:course.id}});"><svg class="feather feather-key text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/></svg></button>
                    <span v-if="course.active "><svg class="feather text-white bg-green-500 rounded-full p-1 fill-green-500 feather-power" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"/><line x1="12" x2="12" y1="2" y2="12"/></svg></span>
                    <span v-else><svg class="feather bg-red-500 rounded-full p-1 text-white fill-red-500 feather-power" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"/><line x1="12" x2="12" y1="2" y2="12"/></svg></span>
                </div>
                   <div class="max-w-[343px] min-h-[395px] p-4 overflow-hidden shadow-md">
                    <img class="min-h-[50%] " :src="course.get_image" :alt="course.name">
                    <div class="px-6 py-4">
                    <div class="text-sm mb-2">{{ course.code }} {{ course.name }}</div>
                    </div>
                    <div class="h-[30%] space-x-1" v-for="professor in course.professors">
                    <router-link :to="{name:'profile',params:{id:professor.id}}" class="flex">
                        <img :src="professor.get_avatar" height="40xp" width="40px" class="rounded-full  inline-block" alt="Name of teacher">
                        <div class="inline-block w-full">
                        <p class="inline-block px-3 py-1 text-[10.5px] hover:underline font-semibold ">{{ professor.first_name }} {{professor.last_name}}</p>
                        <p class=" bg-gray-200 rounded-full w-full text-[9px] px-3 py-1 font-semibold text-gray-700">Profesor</p>
                        </div>
                    </router-link>
                    </div>
                </div>
                </router-link>
            </div>
        </template>
        <template v-else>
            <div class="w-full space-y-4 text-center p-2">
                <h2 class="text-2xl font-bold">No se encuentra en ningun curso</h2>
                <div class="w-full p-2 space-x-4">
                    <router-link :to="{name:'createcourse'}" v-if="userStore.user.role === 'Professor'" class="p-2 bg-green-500 hover:bg-white border border-green-500 hover:text-green-500 duration-300 text-white">Crear Curso</router-link>
                    <router-link :to="{name:'colleges'}" class="p-2  mx-auto bg-gray-500 hover:text-gray-500 hover:bg-white duration-200 border border-gray-500 text-white ">Buscar Cursos</router-link>
                </div>
            </div>
        </template>
        
        
        
    </div>

</template>
<!--El nav colocarlo en el APP.vue pero con una validacion por autenticacion-->
<script>
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user'
import axios from 'axios'
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'PageAuth',
    components:{
        Navbar,
    },
    data() {
        return {
            courses: [],
        }
    },
    mounted() {
        this.getCourses()
    },
    methods: {
        
        async getCourses(){
            await axios.get(`course/users/${this.userStore.user.id}/in`) 
            .then(response =>{
                this.courses = response.data 
            })
            .catch(error => {
                console.log(error); 
            })
        },
    },
} 


</script>