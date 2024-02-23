<template >
    <Navbar/>
    <NavCourse/>
    <div class="max-w-screen-2xl m-5 mx-20 flex items-center justify-between">
        <div>
            <h1 class="text-3xl font-sans font-bold">{{ course.code }} {{ course.name }}</h1>
            <p>Supervisor: {{ admin.name }}</p>
        </div>
    </div>
    <div class="bg-white max-w-[90vw] rounded-md mx-auto" >
        <div class="p-2 w-full flex items-center justify-between" > 
            <router-link :to="{name: 'profile',params:{id:userStore.user.id}}" class="flex items-center space-x-5 hover:underline text-blue-700 font-bold text-2xl">
                <img :src="user.get_avatar" alt="face" class="h-24 w-24 rounded-2xl">
            <p>{{ user.first_name }} {{ user.last_name }}</p>
            </router-link>
            <button v-if="userStore.user.role === 'Professor'" @click="finishCourse" class="p-2 bg-black rounded-lg hover:bg-slate-800 duration-200 text-white">Finalizar el Curso</button>
        </div>
        <div>
            <div class="overflow-x-auto m-4 p-5">
                <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
                    <thead class="ltr:text-left rtl:text-right">
                    <tr>
                        <th class="whitespace-nowrap px-4 text-left py-2 font-medium text-gray-900">Ítem de calificación</th>
                        <th class="whitespace-nowrap px-4 text-left py-2 font-medium text-gray-900">Tipo de Practica</th>
                        <th class="whitespace-nowrap px-4 text-left py-2 font-medium text-gray-900">Rango</th>
                        <th class="whitespace-nowrap px-4 text-left py-2 font-medium text-gray-900">Calificación</th>

                    </tr>
                    </thead>

                    <tbody class="divide-y divide-gray-200">
                    <tr class="odd:bg-gray-50" v-for="(solution, index) in solutions" :key="index">
                        <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{ solution.quiz.title }}</td>
                        <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ solution.quiz.typeoftest }}</td>
                        <td class="whitespace-nowrap px-4 py-2 text-gray-700">0-{{ solution.quiz.total_points }}</td>
                        <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ solution.qualification }}</td>
                    </tr>
                    </tbody>
                </table>
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
    components:{
        Navbar,
        NavCourse,
    },
    data() {
        return {
            user:{},
            course:{},
            admin:{}, 
            solutions: []
        }
    },
    mounted() {
        this.getUser()
        this.getCourse()
        this.getQuizesTries()
    },
    methods: {
        async getUser(){
            await axios.get(`user/${this.userStore.user.id}/`)
            .then(response => {
                this.user = response.data
            })
            .catch(error => { 
                console.log(error);
            })
        },
        async finishCourse(){
            await axios.post(`quiz/finish/${this.$route.params.id}/`)
            .then(response => {
                this.$router.push({name:'pageauth'})
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
        async getQuizesTries(){
            await axios.get(`quiz/myquizes/${this.$route.params.id}/`)
            .then(response => {
                this.solutions = response.data
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>
