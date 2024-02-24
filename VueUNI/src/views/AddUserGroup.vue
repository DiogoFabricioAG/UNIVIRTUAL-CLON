<template>
    <Navbar/>
    <div class="max-w-screen-2xl mt-5 mx-20">
        <div>
            <h1 class="text-3xl mb-4 font-sans font-bold">Mis Grupos 🎯</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" >
        <h2 class="text-2xl font-sans font-bold p-2">Lista de Grupos 🔦</h2>
        <div class="relative overflow-auto shadow-md sm:rounded-lg m-3">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 ">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 ">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            Nombre Completo
                        </th>
                        <th scope="col" class="px-6 py-3">
                            # Participantes
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Opciones
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="odd:bg-white  even:bg-gray-100 border-b" v-for="(group, index) in groups" :key="groups">
                        <th scope="row" class="px-6 py-4" >
                            <div class="flex items-center space-x-2">
                                <img class="max-w-12 rounded-full" :src="group.get_image" :alt="group.name">
                                <p class="font-medium text-black">{{ group.name }}</p>
                            </div>
                        </th>
                        <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                            {{group.count_users}}
                        </td>
                        <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                            <div class="flex space-x-2">
                                <button @click="addUser(group.id)" class="w-full text-white bg-green-500 p-2 rounded-2xl hover:bg-green-600">Agregar</button>  
                            </div> 
                            
                        </td>
                    </tr>
                    
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import NavCourse from '@/components/NavCourse.vue'
import Navbar from '@/components/Navbar.vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'UserAdd',
    components:{
        Navbar,
        NavCourse,
    },
    data() {
        return {
            user:{},
            groups:[],
        }
    },
    mounted() {
        this.getUser()
        this.getGroups()
    },
    methods: {
        async privatesesion(id){
            await axios.post(`chat/private/${id}/`)
            .then(response => {
                this.$router.push({name: 'chat'})           
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getGroups(){
            this.groups = (await axios.get('chat/myadmingroups/')).data
        },
        async getUser(){
            await axios.get(`user/${this.$route.params.id}/`)
            .then(response => {
                this.user = response.data 
            })
            .catch(error => {
                console.log(error);
            })
        },
        async addUser(id){
            await axios.post(`chat/group/${id}/add/${this.$route.params.id}/`)
            .then(response => {
                this.$router.push({name:'chat'})
            })
            .catch(error =>{
                console.log(error);
            })
        }

    },
}
</script>