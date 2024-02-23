<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto mt-10 p-2" >
        <h2  class="text-2xl font-sans font-bold p-5">Añadir/Editar preguntas de {{ quiz.title }} 🧪</h2>
        <div v-if="index === quiz.problems + 1">
            <p class="text-lg">Todas las preguntas fueron enviadas correctamente</p>
            <p class="text-base">Si se quieren editar presione el boton editar de la <button class="text-blue-700 hover:underline" @click="backto">pagina anterior</button> </p>
        </div>
        <div v-else v class="border border-black rounded-lg m-2 w-[75%] mx-auto" :id="index">
            <form method="post" action="." @submit.prevent class="w-[75%] mx-auto p-2 space-y-3 text-black flex flex-col" >
                <h1 class="font-bold">Pregunta {{ index }}º</h1>
                <label>Titulo</label>
                <input type="text" v-model="title" class="border border-black p-1" placeholder="Titulo de la Pregunta">
                <label>Contenido</label>
                <textarea type="text" v-model="content" class="border border-black p-1" placeholder="Contenido de la pregunta"></textarea>
                <label>Valor de la Pregunta</label>
                <input type="number" v-model="points" class="border border-black p-1" placeholder="Peso de la Pregunta">
            </form>
            <hr>
            <div v-for="index in quiz.solutions" :key="index"> 
                <form action="." @submit.prevent method="post" class="space-x-2 flex w-[75%] space-y-2 m-3 mx-auto items-center">
                    <label>Respuesta {{ index }}º:</label>
                    <textarea class="border border-black p-1 w-full" v-model="textcontent[index-1]"></textarea>
                    <input type="checkbox" v-model="problems[index-1]" name="solution">
                </form>
            </div>
            <div class="w-full text-center">
                <button @click="sendInfo(index)" class="p-2 w-full rounded-b-lg bg-black text-white hover:bg-neutral-900">Enviar Pregunta</button>
                
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import axios from 'axios'
export default{
    name:'CreateProblems',
    components:{
        Navbar,
    },
    data() {
        return {
            quiz:{},
            title: '',
            content : '',
            index: 1,
            points: 0,
            problems:[],
            textcontent: [],
        }
    },
    mounted() {
        this.getQuiz()
    },
    methods: {
        async getQuiz(){
            await axios.get(`quiz/${this.$route.params.pk}/`)
            .then(response =>{
                this.quiz = response.data
            }) 
            .catch(error =>{
                console.log(error);
            })
        },
        async sendInfo(id){
            for (let i = 0; i < this.problems.length; i++) {
                if (this.problems[i] === undefined) {
                    this.problems[i] = false;
                } 
            }
            await axios.post(`quiz/${this.$route.params.pk}/create_problem/`,{
                title:this.title,
                content:this.content,
                points:this.points, 
                solutionscontext:this.textcontent,
                corrections:this.problems,
            })
            .then(response => {
                this.title = ''
                this.content = ''
                this.points = 0
                this.index++
                this.textcontent = []
                this.problems = []
            })
            .catch(error => {
                console.log(error)
            })
        },
        async backto(){
            await axios.patch(`quiz/${this.$route.params.pk}/available/`)
            .then(response => {
                this.$router.back() 
            })
            .catch(error => console.log(error))
        }
    },
}

</script>
