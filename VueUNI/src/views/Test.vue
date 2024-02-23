<template>
<Navbar/>
<div class="bg-white max-w-[90vw] mt-5 space-y-10 p-2 rounded-md mx-auto" >
    <h2 class="text-2xl font-sans font-bold p-5">Practica Calificada 📄</h2>
    <button @click="Back" class="bg-slate-400 hover:bg-slate-500 duration-300 rounded-lg p-2 px-3 mx-5">Atras</button>
    
    <div v-if="!final">
        <div class="w-full  flex justify-end">
            <div class="p-1 border-t border-x border-black select-none">
                {{String(hour).padStart(2, '0') }}:{{ String(minutes).padStart(2, '0') }}:{{ String(seconds).padStart(2, '0') }}
            </div>
        </div>
        <div class="mb-3 flex space-x-4">
            <div class="border w-[15%] border-black p-1" >
                <p>Pregunta <strong>{{ pointer + 1 }}</strong></p>
                <p>Puntua como {{ problems[pointer].points }} pts</p>
                <p class="text-sm" v-if="answers[pointer]">Respuesta Guardada: {{ answers[pointer].split(' ')[0] }}</p>
            </div>
            <div class="bg-blue-200 w-[85%] border border-black space-y-3 p-1" >
                <h3>{{ problems[pointer].title }}</h3>
                <h4 class="">{{ problems[pointer].content }}</h4>
                <div class="space-y-1 p-1 justify-between content-between flex flex-col">
                    <label v-for="(solution, index) in solutions" :key="index">
                        <input v-model="answers[pointer]" type="radio" name="drone" :value="solution.content" />
                        <span>{{solution.content}}</span>
                    </label>
                    
                </div>
                <button @click="notselect" class="ml-0 text-blue-800" href="#">Quitar mi eleccion</button> 
            </div>
        </div>
        <div class="flex justify-between items-center">
            <button v-if="pointer !== 0" @click="getNewSolutions('atras')" class="bg-slate-300 hover:bg-slate-200 rounded-lg p-2 px-3 mx-5 mb-3">Retroceder</button>
            <button @click="getNewSolutions('adelante')" class="bg-slate-300 hover:bg-slate-200 rounded-lg p-2 px-3 mx-5 mb-3">Enviar</button>
        </div>
    </div>
    
    <div v-else>
        <div class="w-[80%] mx-auto text-center">
            <h2 class="text-2xl">Terminado la Practica <strong>{{  quiz.title }}</strong></h2>
            <div v-for="(item, index) in answers" :key="index">
                <div>
                    <p v-if="item">Respuesta para la pregunta {{ index+1 }}: {{ item }}</p>
                    <p v-else>No se ha dado una respuesta para la pregunta {{ index+1 }}</p>
                </div>
            
            </div>
            <div class="flex w-full m-5 space-x-2">
                <button @click="sendvalor" class="bg-green-600 p-2 w-[50%]  mx-auto text-white hover:bg-green-500">Enviar las Preguntas</button>
                <button @click="backtoquestions" class="bg-black text-white p-2 w-[50%]  mx-auto hover:bg-slate-900">Volver al las Preguntas</button>
            </div>
        </div>
    </div>
</div>

</template>
<script>
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios'

export default{
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    components:{
        Navbar
    },
    name:'Test',
    created() {
        this.getData()
        this.getQuiz()
    },
    data() {
        return {
            quiz: {},
            problems: [],
            solutions: [],
            answers:[],
            pointer: -1,
            final:false,
            pts:0,
            ids:[],
            hour:0,
            minutes:0, 
            seconds:0,
            myTimer:null,
        }
    },
    mounted() {
        this.myTimer = setInterval(() => {
            this.updatetimer()
            
        }, 1000);

        
    },
    methods: {
        Back(){
            clearInterval(this.myTimer);
            this.$router.push({name:'practices',params:{id:this.$route.params.id}})
        },
        updatetimer(){
            // 0 1 0
            if (this.seconds === 0){
                if (this.minutes === 0 && this.hour !== 0){
                    this.hour--
                    this.minutes=60
                }
                
                this.minutes--
                this.seconds = 60
            }
            this.seconds--
            if (this.seconds === 0 && this.hour === 0, this.minutes === -1 ){
                this.seconds=0
                this.minutes=0
                clearInterval(this.myTimer);
                this.sendvalor()
                this.$router.back()
                
            }
            
        },
        notselect(){
            this.answers[this.pointer] = ''
        },
        backtoquestions(){
            this.pointer = -1
            this.final = false
            this.getNewSolutions('adelante')
        },
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
        
        async getData(){
            this.pointer+=1
            if (this.pointer!==this.problems.length || this.problems.length===0){
                this.problems =  (await axios.get(`quiz/${this.$route.params.pk}/problems/`)).data.problems
                await axios.get(`quiz/problem/${this.problems[this.pointer].id}/`)
                .then(response => {
                    this.solutions = response.data
                })
                .catch(error => {
                    console.log(error)
                    console.log(this.problems[this.pointer].id);
                })
            }
            
            else {
               this.final = true
            }
        },
        async sendvalor(){
            await axios.post(`quiz/${this.$route.params.pk}/send/`,{
                answers:this.answers,
                ids:this.ids,
            })
            .then(response => {
                clearInterval(this.myTimer)
                this.$router.push({name:'practices',params:{id:this.$route.params.id}})
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getNewSolutions(where){
            try{
                this.ids[this.pointer] = this.solutions.find(object => object.content === this.answers[this.pointer]).id
            }
            catch{
                console.log("Pasamo");
            }
            
            
            if (where === 'adelante'){
                this.pointer+=1
                
            }
            else{
                this.pointer-=1
            }
            
            if (this.pointer!==this.problems.length || this.problems.length===0){
                await axios.get(`quiz/problem/${this.problems[this.pointer].id}/`)
                .then(response => {
                    this.solutions = response.data
                    console.log(this.solutions);
                })
                .catch(error => {
                    console.log(error)
                })
            }
            else {
               this.final = true
            }
        }
    },
}

</script>  