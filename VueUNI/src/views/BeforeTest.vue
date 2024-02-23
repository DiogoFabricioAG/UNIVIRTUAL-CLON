<template >
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Examen {{ quiz.typeoftest }}: {{ quiz.title }} 📌</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" >
        <div class="flex flex-col w-full">
            <h2 class="text-2xl font-sans font-bold">Datos de la prueba 📅</h2>
            <div class="mt-8 text-sm space-y-3">
                <p>Intentos Permitidos : {{ quiz.attempts }}</p>
                <p>Limite de tiempo : {{ time_in_minutes }} minutos </p>
            </div>
            <template v-if="attempts.length">
                <h2 class="text-xl mt-4 font-sans font-bold">Resumen de Intentos</h2>
                <div class="w-full mx-auto p-2 bg-gray-100">
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y-2 divide-gray-200 bg-gray-100 text-sm">
                            <thead class="text-left">
                            <tr>
                                <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Fecha del Examen</th>
                                <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Calificacion</th>
                            </tr>
                            </thead>

                            <tbody class="divide-y divide-gray-200">

                            <tr v-for="(attempt, index) in attempts" :key="index">
                                <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{ attempt.created_at_formatted }}</td>
                                <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ attempt.qualification }}/{{ quiz.total_points }}</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </template>
            <template v-else>
                <h2 class="text-lg font-bold font-sans text-center mb-3">Uds. puede rendir el examen con normalidad</h2>
            </template>
            <p v-if="attempts.length >= quiz.attempts" class="text-center text-lg mb-3 font-bold">Uds. No cuenta con mas Intentos</p>
            <div class="w-full flex justify-center space-x-2">
                <router-link :to="{name:'test',params:{id:$route.params.id,pk:quiz.id}}" v-if="attempts.length < quiz.attempts" class="p-2 bg-blue-600 text-white hover:bg-white border border-blue-600 hover:text-blue-600">Rendir Examen</router-link>
                <router-link :to="{name:'practices',params:{id:$route.params.id}}" class="p-2 bg-gray-600 text-white hover:bg-white border border-gray-600 hover:text-gray-600">Volver a Practicas</router-link>
            </div>
        </div>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import axios from 'axios'

export default {
    components:{
        Navbar,
    },
    data() {
        return {
            quiz:{},
            attempts:[],
            hour   : 0,
            minutes: 0,
            seconds: 0,
        }
    },  
    computed:{
        time_in_minutes: function(){
            return this.hour*60 + this.minutes + this.seconds/60
        },
    },
    mounted() {
        this.getQuiz()
        this.getAttempts()
    },
    methods: {
        async getQuiz(){
            await axios.get(`quiz/${this.$route.params.pk}/`)
            .then(response =>{
                this.quiz = response.data
                this.hour = Number(this.quiz.time.split(':')[0])
                this.minutes = Number(this.quiz.time.split(':')[1])
                this.seconds = Number(this.quiz.time.split(':')[2])
            }) 
            .catch(error =>{
                console.log(error);
            })
        },
        async getAttempts(){
            await axios.get(`quiz/myquizes/attempts/${this.$route.params.pk}/`)
            .then(response => {
                console.log(response.data);
                this.attempts = response.data
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>
