<template>
    <Navbar/>
    <h1 class="text-center text-5xl mt-2 font-bold">Bandeja de Solicitudes de Amistad</h1>
    <div class="bg-white max-w-[80vw] text-center rounded-md mx-auto p-3 mt-4 flex">
        <div class="w-1/2 ">
            <h2 class="text-xl font-bold ">Bandeja de solicitudes</h2>
            <div v-if="requests.length">
                <div v-for="(item, index) in requests" :key="index" class="">
                    <div :id="index" class="w-[80%] border-black rounded-2xl border mx-auto mt-5 justify-center bg-white p-2 flex space-x-2 items-center">
                        <img class="rounded-full w-[15%]" :src="item.send_by.get_avatar" alt="nadadad">
                        <div class="">
                            <h1 class="text-2xl font-bold">{{ item.send_by.first_name }}</h1>
                            <p>Te ha mandado una solicitud de amistad</p>
                            <div class="flex justify-between mt-3 text-white">
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
        </div>
        <div class="w-1/2">
            <h2 class="text-xl font-bold">Lista de Amigos</h2>
            <div v-if="friends.length">
                <div v-for="(friend, index) in friends" :key="index" class="">
                    
                    <div :id="index" class="w-[80%] border-black rounded-2xl border mx-auto mt-5 justify-center bg-white p-2 flex space-x-2 items-center">
                        <img class="rounded-full w-[15%]" :src="friend.get_avatar" alt="nadadad">
                        <div>
                            <h1 class="text-2xl font-bold">{{ friend.first_name }}</h1>
                            <div class="flex justify-between space-x-2 mt-3 text-white">
                                <button @click="privatesesion(friend.id)" class="bg-blue-500 hover:bg-blue-600 p-2 rounded-md">Conversar</button>
                                <router-link v-if="friend.role !== 'Professor'" :to="{name:'adduser',params:{id:friend.id}}" class="bg-yellow-500 hover:bg-yellow-600 p-2 rounded-md">Agregar a un Grupo</router-link>
                                <button @click="deletefriend(friend.id)" class="bg-red-500 hover:bg-red-600 p-2 rounded-md">Eliminar</button>
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
            <div v-else class="mt-4">
                <p class="text-center text-xl">Ud. no cuenta con algun amigo.</p>
                <p class="text-center">Intente mandando una solicitud!</p>
            </div>
        </div>

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
            requests:[],
            friends: [],
        }
    },
    mounted() {
        this.getRequests()    
        this.getFriends()
    },
    methods: {
        async privatesesion(id){
            await axios.post(`chat/private/${id}/`)
            .then(response => {
                this.$router.push({name: 'chat'}) 
                console.log(response.data);          
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getFriends(){
            await axios.get('user/friends/')
            .then(response => {
                this.friends = response.data
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
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
                if (option === 0){
                    this.getFriends()
                }
                value.setAttribute("hidden",true)
            })
            .catch(error => {
                console.log(error);
            })
        },
        async deletefriend(id){
            await axios.delete(`user/friends/delete/${id}/`)
            .then(response => {
                this.friends = this.friends.filter(user => user.id !== id)
            })
            .catch(error =>{
                console.log(error);
            })
        }
    },

}
</script>