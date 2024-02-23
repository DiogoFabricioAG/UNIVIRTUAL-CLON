<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Eventos para la fecha {{ $route.query.date }} 🤵</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-5" >
            <template v-if="events.length">
                <div class="justify-end w-full flex">
                    <router-link :to="{name:'createevent',query:{date:$route.query.date}}" class="bg-green-600  hover:bg-green-700 duration-200 rounded-2xl p-2 text-white border border-black">Crear un Evento</router-link>

                </div>

                <div v-for="(event, index) in events" :key="index" class="w-full border mt-3 flex flex-col   border-black p-2 rounded-lg">
                    <div class="flex justify-between items-center h-[30%]">
                        <div class="w-[90%] space-y-3">
                            <h2 class="text-2xl font-bold">{{ event.title }}</h2>
                            <p>{{ event.description }} </p>
                            <div class="flex space-x-3">
                                <router-link :to="{name:'editevent',params:{id:event.id}}" class="bg-gray-400 text-white rounded-xl p-2">Editar</router-link>
                                <button @click="deleteEvent(event.id)" class="bg-red-600 text-white rounded-xl p-2">Borrar</button>
                            </div>
                        </div>
                        <div class="w-[10%] ">
                            <p>{{ event.created_at }}</p> 
                        </div>
                        
                    </div>
                    
                </div>

            </template>
            <template v-else>
                <div class="w-full text-center justify-between p-2">
                    <p class="text-3xl font-bold mb-4">No hay eventos programados 🚫</p>
                    <router-link :to="{name:'createevent',query:{date:$route.query.date}}" class="bg-green-600 mt-4 hover:bg-green-700 duration-200 rounded-2xl p-2 text-white border border-black">Crear un Evento</router-link>
                </div>
            </template>
            
        </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import axios from 'axios'

export default {
    components:{
        Navbar
    },
    name:'Events Description',
    mounted() {
        this.getEvents()
    },
    data() {
        return {
            events: []
        }
    },
    methods: {
        async getEvents(){
            await axios.get(`calendar/get-events-date?date=${this.$route.query.date}`)
            .then(response => {
                this.events = response.data
            })
        },
        async deleteEvent(id){
            await axios.delete(`calendar/deleted-event/${id}/`)
            .then(response => {
                this.$router.back()
            })
            .catch(error => {
                console.log(error);
            })
        }
    },

}
</script>
