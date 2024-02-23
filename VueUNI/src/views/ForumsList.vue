<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Foros en Activo 📌</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" >
        <h1 class="text-2xl font-sans font-bold">Lista de Foros 📅</h1>
        <div class="flex flex-col justify-between mt-4 items-center w-full">
            
            <div v-for="(forum, index) in forums" :key="index" class="w-[80%] rounded-lg flex m-5 space-x-3 mx-auto p-5 border border-black">

                <img :src="forum.get_image" class="w-[30%]">
                <div class="w-[70%] flex flex-col justify-between text-right">
                    <h3 class="font-bold text-xl">{{ forum.name }}</h3>
                    <p>Participantes: {{ forum.count_users }}</p>
                    <p>Mensajes totales: {{forum.count_messages}}</p>
                    <p>Rol dentro del Foro: {{ userStore.user.role }}</p>
                    <router-link :to="{name:'forum',params:{id:forum.id}}" class="p-1 text-center duration-100 bg-blue-600 text-white hover:bg-white hover:text-blue-600 border border-blue-600">Entrar</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios';


export default {
    components:{
        Navbar,
    },
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    data() {
        return {
            forums: [],
        }
    },
    mounted() {
        this.getForum()
    },
    methods: {
        async getForum(){
            await axios.get(`chat/myforums/`)
            .then(response => { 
                console.log(response.data)
                this.forums = response.data
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>
