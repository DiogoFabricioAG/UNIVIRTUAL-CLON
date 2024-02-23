<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-5 mt-4" >
        <h2  class="text-2xl font-sans font-bold p-5">Crear un Evento ⏱</h2>
        <form action="." @submit.prevent="createEvent" method="post" enctype="multipart/form-data" class="flex flex-col w-[50%] mt-3 mx-auto border p-2 rounded-md border-black">
            <label >Titulo del Evento</label>
            <input v-model="title" class="border border-black p-2 rounded-md" placeholder="Coloque el nombre del Grupo" type="text">            
            <label >Descripcion del Evento</label>
            <input v-model="description" class="border border-black p-2 rounded-md" placeholder="Coloque el nombre del Grupo" type="text">            
            <label>Fecha del Evento</label>
            <input v-model="date_event" type="date" class="border border-black p-2 rounded-md">
            <button class="p-2 mt-2 hover:bg-slate-950 transition duration-300 active:shadow-lg  bg-black text-white">Crear</button>
        </form>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import axios from 'axios'

import { useUserStore } from '@/stores/user';

export default{
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name:'addEvent',
    components:{
        Navbar,
    },
    data() {
        return {
            title:'',
            description: '',
            date_event:this.$route.query.date
        }
    },
    methods: {
        async createEvent(){
            await axios.post('calendar/create-event/',{
                title: this.title,
                description: this.description,
                date_event: this.date_event,
            })
            .then(response => {
                this.$router.back()
            })
            .catch(error =>{
                console.log(error);
            })

        }
    }
}

</script>