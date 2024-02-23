<template>
    <NavbarVue/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <h1 class="text-2xl font-sans font-bold">{{ college.name }} ⭐</h1>
    </div>  
    <div class="bg-white max-w-[80vw] rounded-md mx-auto" >
        <div >
            <div class="flex justify-between items-center w-full p-3" v-if="courses.length">
                <h2 class="text-2xl font-sans font-bold p-5">Cursos Disponibles 📚</h2>
                
                <form class="flex space-x-2 w-[50%]" action="." method="post" @submit.prevent>
                    <input v-model="query" type="text" class="border w-[100%] p-1 border-black" placeholder="Nombre del Curso">
                    <button @click="getCourses" class="bg-black text-white p-2 rounded-lg active:scale-90 transition duration-200 flex space-x-2">
                        <p>Search</p>
                        <svg class="feather feather-search" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/></svg>
                    </button>
                </form>
                
            </div> 
            <h2 v-else-if="query === ''" class="text-2xl font-sans font-bold p-5">{{college.short_name}} no cuenta con Cursos disponibles en este momento</h2>
            <div v-else class="p-3">
                <h2 class="text-2xl font-sans font-bold p-5">{{college.short_name}} no cuenta con Cursos con la busqueda realizada.</h2>
                <h3>Intentar Nuevamente</h3>
                <form class="flex space-x-2 w-[50%]" action="." method="post" @submit.prevent>
                    <input v-model="query" type="text" class="border w-[100%] p-1 border-black" placeholder="Nombre o Codigo del Curso">
                    <button @click="getCourses" class="bg-black text-white p-2 rounded-lg active:scale-90 transition duration-200 flex space-x-2">
                        <p>Search</p>
                        <svg class="feather feather-search" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><circle cx="11" cy="11" r="8"/><line x1="21" x2="16.65" y1="21" y2="16.65"/></svg>
                    </button>
                </form>
            </div>
        </div>
        
        <div class="flex flex-wrap w-full">
            <router-link :to="{name : 'course',params:{id:course.id}}" class="mt-3 mx-auto relative z-5 active:scale-95 duration-300 transition-transform" v-for="course in courses" :key="course.id">
                <span v-if="course.validation !== ''" class="absolute bg-black p-2 rounded-full right-5 active:scale-95 top-5 z-10"><svg class="feather feather-key text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/></svg></span>
                <span v-else class="absolute bg-black p-2 rounded-full right-5 active:scale-95 top-5 z-10"><svg class="feather text-white feather-unlock" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><rect height="11" rx="2" ry="2" width="18" x="3" y="11"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg></span>

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
    </div>
</template>
<script>
import axios from 'axios'
import NavbarVue from '@/components/Navbar.vue';

export default{

    name:'CoursesfromColleges',
    components:{
        NavbarVue,
    },
    data() {
        return {
            college:{},
            courses: [],
            query:'',
        }
    },
    mounted(){
        this.getCollege()
        this.getCourses()
    },
    methods: {
        async getCollege(){
            await axios.get(`colleges/${this.$route.params.id}/`)
            .then(response =>{
                this.college = response.data
            })
            .catch(error => {
                console.log(error);
            })
        }, 
        async getCourses(){
            await axios.post(`course/college/${this.$route.params.id}/`,{
                query:this.query,
            })
            .then(response =>{
                this.courses = response.data
            }) 
            .catch(error => {
                console.log(error);
            })
        }
    },

}

</script>