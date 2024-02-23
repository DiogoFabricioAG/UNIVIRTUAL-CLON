<template>
    <Navbar/>
    <h1 class="text-center text-5xl mt-2 font-bold">Bandeja de Solicitudes de Amistad</h1>
    <div v-if="requests.length">
        <div v-for="(item, index) in requests" :key="index" class="">
            <div :id="index" class="w-[75%] border-black rounded-2xl border mx-auto mt-5 justify-center bg-white p-2 flex space-x-2 items-center">
                <img class="rounded-full w-[15%]" :src="item.send_by.get_avatar" alt="nadadad">
                <div class="">
                    <h1 class="text-2xl font-bold">{{ item.send_by.first_name }}</h1>
                    <p>Te ha mandado una solicitud de amistad</p>
                    <div class="flex space-x-5 mt-3 text-white">
                        <button @click="options(0,item.send_by.id,index)" class="bg-green-500 hover:bg-green-600 p-2 rounded-md">Aceptar</button>
                        <button @click="options(1,item.send_by.id,index)" class="bg-red-500 hover:bg-red-600 p-2 rounded-md">Denegar</button>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
    <div v-else class="mt-4">
        <p class="text-center text-xl">Ud. no cuenta con alguna solicitud.</p>
        <p class="text-center">Intente mandando una!</p>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import axios from 'axios'

export default{
    name:'Notification',
    components:{
        Navbar,
    },
    data() {
        return {
            requests:[]
        }
    },
    mounted() {
        this.getRequests()    
    },
    methods: {
        async getRequests(){
            await axios.get(`user/myrequests/`)
            .then(response =>{
                this.requests = response.data
            })
            .catch(error =>{
                console.log(error);
            })
        },
        async options(option,id,index){
            await axios.post(`user/friendship-request-options/${option}/`,{
                id:id
            })
            .then(response => {
                console.log(response.data);
                let value = document.getElementById(index)
                value.setAttribute("hidden",true)
            })
            .catch(error => {
                console.log(error);
            })
        }
    },

}
</script>