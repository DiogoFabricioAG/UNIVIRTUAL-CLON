<template>
    <Navbar/>
    <NavCourse/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">{{ course.code }} {{ course.name }}</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" >
        <div class="flex w-full justify-between">
            <h2 class="text-2xl font-sans font-bold p-2">Lista de Participantes 🙋‍♂️🙋‍♀️</h2>
            <button v-if="userStore.user.role === 'Professor'" @click="sendCode" class="px-2 bg-green-400 text-white rounded-md hover:bg-green-300">Enviar Codigo</button>
        </div>
        
        <div class="relative overflow-auto shadow-md sm:rounded-lg m-3">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 ">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 ">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            Nombre Completo
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Rol en el Curso
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Acciones
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="odd:bg-white  even:bg-gray-100 border-b" v-for="(user, index) in users" :key="index">
                        <th scope="row" class="px-6 py-4" >
                            <div class="flex items-center space-x-2">
                                <img class="max-w-12 rounded-full" :src="user.get_avatar" :alt="user.name">
                                <router-link :to="{name:'profile', params:{id:user.id}}" class="font-medium text-blue-600  hover:underline">{{ user.first_name }} {{ user.last_name }}</router-link>
                            </div>
                        </th>
                        <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                            {{user.role}}
                        </td>
                        <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                            <div class="flex space-x-2">
                                <button @click="sendrequest(user.id)" class="rounded-full bg-green-500 hover:bg-green-600 text-white p-2"><svg class="feather feather-plus" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><line x1="12" x2="12" y1="5" y2="19"/><line x1="5" x2="19" y1="12" y2="12"/></svg></button>
                                <router-link v-if="userStore.user.role !== 'Professor' && user.role !==  'Professor' && userStore.user.id !== user.id" :to="{name:'adduser',params:{id:user.id}}" class="rounded-full bg-yellow-500 hover:bg-yellow-600 text-white p-2"><svg class="feather feather-users" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></router-link>
                                <button @click="privatesesion(user.id)" class="rounded-full bg-blue-500 hover:bg-blue-600 text-white p-2"><svg class="feather feather-send" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><line x1="22" x2="11" y1="2" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg></button>
                                <router-link :to="{name:'createreport',params:{id:$route.params.id,pk:user.id}}" v-if="userStore.user.role === 'Professor' && user.role === 'Student'" class="rounded-full bg-red-500 hover:bg-red-600 text-white p-2"><svg class="feather feather-clipboard" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect height="4" rx="1" ry="1" width="8" x="8" y="2"/></svg></router-link>
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
    name: 'TablePerson',
    components:{
        Navbar,
        NavCourse,
    },
    data() {
        return {
            users:[],
            course: {},
        }
    },
    mounted() {
        this.getCourse()
        this.getParticipants()
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
        async sendrequest(id){
            await axios.post(`user/sendrequest/`,{
                id:id,
            })
            .then(response => {
                console.log(response.data);
            })
            .catch(error =>{
                console.log(error);
            })
        },
        async getCourse(){
            await axios.get(`course/${this.$route.params.id}/`)
            .then(response => {
                this.course = response.data
                this.admin = this.course.admin
                
            })
            .catch(error => {
                console.log(error); 
            })
        },
        async getParticipants(){
            await axios.get(`course/${this.$route.params.id}/users/`)
            .then(response => {
                this.users = response.data                 
            })  
            .catch(error => { 
                console.log(error); 
            })
        },
        async sendCode(){
            await axios.post(`course/${this.$route.params.id}/sendcode/`)
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
    },
}
</script>