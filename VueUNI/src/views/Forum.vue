<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Foro del Curso 📮</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" >
        <h2 class="text-2xl font-sans font-bold">{{ forum.name }} ✉</h2>
        <form method="post" @submit.prevent="createMessage" class="h-[30%] w-full p-2 my-3">
            <div class="flex justify-center">
                <input v-model="title" type="text" class="my-2 p-2 rounded-lg w-1/2 border border-black" placeholder="Coloque el titulo para el Foro">
            </div>

            <textarea v-model="content" class="border p-1 w-full resize-none border-black" placeholder="Coloque su mensaje para el Foro" cols="30" rows="5"></textarea>
            <div class="flex justify-end">
                <button class="bg-green-600 p-2 hover:bg-green-800 active:scale-90 transition duration-300 text-white rounded-2xl">Enviar</button>
            </div>
        </form>
        <hr>
        <div class="w-[90%] my-3 mx-auto border border-black rounded-xl p-2" v-for="(message, index) in messages" :key="index">
            <div class="flex justify-between items-center">
                <div class="flex space-x-4 items-center">
                    <img :src="message.send_by.get_avatar" class="h-11 w-11 rounded-full" alt="nada">
                    <div>   
                        <h3 class="font-bold text-xl">
                            {{ message.title }}
                        </h3>
                        <p>{{ message.created_at_formatted }}</p>
                    </div>
                </div>
                <p >{{ index + 1}}</p>
            </div>
            
            <div class="my-2 text-gray-500 text-sm">
                <p>{{ message.send_by.role }}: {{ message.send_by.name }}</p>
            </div>
            <div class="my-2">
                <p>{{ message.content }}</p>
            </div>

        </div>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import axios from 'axios';


export default {
    components:{
        Navbar,
    },
    data() {
        return {
            title: '',
            content:'',   
            messages: [],
            forum: {}
        }
    },
    mounted() {
        this.getForum()
        this.getMessages()
    },
    methods: {
        async getForum(){
            await axios.get(`chat/room/${this.$route.params.id}/`)
            .then(response => {
                console.log(response.data);
                this.forum = response.data
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getMessages(){
            await axios.get(`chat/forum/${this.$route.params.id}/messages/`)
            .then(response => {
                this.messages =response.data
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
        async createMessage(){
            await axios.post(`chat/forum/${this.$route.params.id}/createmessages/`,{
                title: this.title,
                content: this.content
            })
            .then(response => {
                console.log(response.data.message);
                this.messages.push(response.data.obj)
                this.title = ''
                this.content =''
            })
            .catch(error => {
                console.log(error);
            })
        },
    },
}
</script>
