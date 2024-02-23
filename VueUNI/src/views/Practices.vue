<template>
    <Navbar/>
    <NavCourse/>
    <div class="max-w-screen-2xl m-5 mx-20 flex items-center justify-between">
        <div>
            <h1 class="text-3xl font-sans font-bold">{{ course.code }} {{ course.name }}</h1>
            <p>Area de Practicas 🎓</p>
        </div>
        <div >
            <router-link :to="{name:'addMaterials',params:{id:$route.params.id}}" v-if="userStore.user.role === 'Professor'" class="rounded-xl p-2 bg-black hover:bg-slate-800 active:scale-90 transition duration-300 text-white font-normal">Añadir datos</router-link>
        </div>
    </div>  
    <div class="bg-white max-w-[85vw] p-6 rounded-md mx-auto space-y-6" >
        
        <div v-for="(item, index) in typesoftest" :key="index" class="mt-2">
            <h1 class="text-2xl font-sans font-bold">{{ item.text }}</h1>
            <div v-for="quiz in quizes.filter(object => object.typeoftest == item.text)" :key="quiz.id">
                <div v-if="quiz.state !== 'Not Available' || userStore.user.role ==='Professor'" class="w-full p-4 overflow-hidden shadow-md">
                    <div class="flex text-blue-600 items-center justify-between" >
                        <router-link :to="{name:'beforetest',params:{id:$route.params.id,pk:quiz.id}}" class="flex hover:underline items-center space-x-3">
                            <template v-if="item.color === 'blue'">
                                <div class="bg-blue-500 p-5 rounded-xl">
                                    <svg class="feather feather-file-minus text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" x2="15" y1="15" y2="15"/></svg>
                                </div>
                            </template>
                            <template v-else-if="item.color === 'green'">
                                <div class="bg-green-500 p-5 rounded-xl">
                                    <svg class="feather feather-file-minus text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" x2="15" y1="15" y2="15"/></svg>
                                </div>
                            </template>
                            <template v-else-if="item.color === 'yellow'">
                                <div class="bg-yellow-500 p-5 rounded-xl">
                                    <svg class="feather feather-file-minus text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" x2="15" y1="15" y2="15"/></svg>
                                </div>
                            </template>
                            <template v-else-if="item.color === 'orange'">
                                <div class="bg-orange-500 p-5 rounded-xl">
                                    <svg class="feather feather-file-minus text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" x2="15" y1="15" y2="15"/></svg>
                                </div>
                            </template>
                            <template v-else-if="item.color === 'red'">
                                <div class="bg-red-500 p-5 rounded-xl">
                                    <svg class="feather feather-file-minus text-white" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" x2="15" y1="15" y2="15"/></svg>
                                </div>
                            </template>
                            
                            <div>
                                <p>{{ quiz.title }}</p>
                                <p class="text-sm">Problemas: {{ quiz.problems }}</p>
                            </div>
                        </router-link>
                        <div class="flex items-center space-x-3" v-if="userStore.user.role === 'Professor'">
                            <router-link v-if="quiz.state === 'Not Available'" :to="{name:'problemsolutions',params:{id:$route.params.id,pk :quiz.id}}" class="rounded-xl p-1 bg-black hover:bg-slate-800 active:scale-90 transition duration-300 text-white font-normal">Crear Problemas</router-link>
                            <button v-else @click="destroyQuiz(quiz.id)" class="p-2 bg-red-600 text-white hover:bg-white border border-red-600 hover:text-red-600 duration-200">Eliminar</button>
                        </div>
                    </div>
                    
                </div>  
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
    name:'Practices',
    components:{
        Navbar,
        NavCourse,
    },
    data() {
        return {
            course:{},
            quizes: [],
            typesoftest: [{
                            text:'Quick (NON Q)',
                            color:'blue',   
                          },
                          {
                            text:'Practice (PC)',
                            color:'green',   
                          },
                          {
                            text:'Parcial (EP)',
                            color:'yellow',   
                          },
                          {
                            text:'Final (EF)',
                            color:'orange',   
                          },
                          {
                            text:'Sustitutorio (ES)',
                            color:'red',   
                          }]
        }
    },
    mounted() {
        this.getCourse()
        this.getQuizzes()
    },
    methods: {
        async destroyQuiz(id){
            await axios.delete(`quiz/delete/${id}/`)
            .then(response => {
                console.log(response.data.message);
                this.quizes = this.quizes.filter(object => object.id !== id)
            })
            .catch(error)
        },
        async getCourse(){
            await axios.get(`course/${this.$route.params.id}/`)
            .then(response => {
                this.course = response.data
                
            })
            .catch(error => {
                console.log(error); 
            })
        },
        async getQuizzes(){
            await axios.get(`quiz/quizzesfrom/${this.$route.params.id}/`)
            .then(response => {
                this.quizes=response.data;
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>