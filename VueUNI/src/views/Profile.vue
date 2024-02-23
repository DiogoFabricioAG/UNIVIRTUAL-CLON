<template>
    <Navbar/>
    <div class="bg-white max-w-[84vw] mt-10 flex flex-col md:flex-row rounded-md mx-auto" >
        <div class="md:w-1/3 w-full">
            <div class="m-5 items-center text-center flex flex-col border-2 p-3 space-y-4 border-gray-50 shadow-md">
                <img :src="user.get_avatar" class="rounded-full select-none max-w-[30vh]" alt="face">
                <h1 class="font-bold text-2xl">{{ user.first_name }} {{ user.last_name }}</h1>
                <router-link :to="{name:'profileedit',params:{id:$route.params.id}}" class="bg-blue-700 flex justify-center transition duration-150 hover:bg-blue-900 text-white rounded-md w-full mt-3 p-1"><p><svg class="feather feather-edit" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg></p>Editar Perfil</router-link>
                <div class="text-base font-semibold w-full text-left">
                    <h3>Informacion Personal</h3>
                    <p class="font-light text-sm">{{ user.description }}</p>
                </div>
                <div class="text-base font-semibold w-full text-left">
                    <h3>Direccion de correo:</h3>
                    <a :href="user.email" class="text-blue-700 text-sm hover:underline" >{{user.email}}</a>
                </div>
                <div class="text-base font-semibold w-full text-left">
                    <h3>Pais: </h3>
                    <p class="text-sm font-normal">{{ user.country }}</p>
                </div> 
                <div class="text-base font-semibold w-full text-left">
                    <h3>Ciudad</h3>
                    <p class="text-sm font-normal">{{ user.city }}</p>
                </div>

            </div>
            
           
        </div>
        <div class="md:w-1/3 w-full">
            
            <div class="m-5 items-center text-center flex flex-col border-2 p-3 space-y-4 border-gray-50 shadow-md" v-if="courses.length">
                
                <div class="text-base font-semibold w-full text-left space-y-2">
                    <p class="font-light text-lg">Detalles del curso</p>
                    <p class="font-bold text-sm">Perfiles de curso</p>
                    <div class="mt-2">
                        <div class="mt-1" v-for="course in courses">
                            <router-link :to="{name:'course',params:{id:course.id}}" class="text-blue-700 font-normal text-md hover:underline"> {{ course.name }}</router-link>
                        </div>
                        
                    </div>
                    
                    
                </div>
                
            </div>
            <div class="m-5 items-center text-center flex flex-col border-2 p-3 space-y-4 border-gray-50 shadow-md">
                <div class="text-base font-semibold w-full text-left space-y-2">
                    <p class="font-light text-lg">Miscelanea</p>
                    <div><router-link :to="{name:'blog',params:{id:$route.params.id}}" class="text-blue-700 text-sm hover:underline" >Entradas del blog</router-link></div>
                    <div><router-link :to="{name:'forums'}" class="text-blue-700 text-sm hover:underline" >Foros de discusión</router-link></div>
                    
                
                </div>
            </div>
            <div class="m-5 items-center text-center flex flex-col border-2 p-3 space-y-4 border-gray-50 shadow-md" v-if="userStore.user.id == user.id">

                <div class="text-base font-semibold w-full text-left space-y-2">
                    <p class="font-light text-lg">Informes</p>
                    
                    
                    <div><router-link :to="{name:'certificate'}" href="#" class="text-blue-700 text-sm hover:underline" >Mis certificados</router-link></div>
                    <div><router-link :to="{name:'report'}" href="#" class="text-blue-700 text-sm hover:underline" >Informes Personales</router-link></div>
                    <div><router-link :to="{name:'resumes'}" class="text-blue-700 text-sm hover:underline" >Resumen de Calificaciones</router-link></div>
                    
                </div>
            </div>
        </div>
        <div class="md:w-1/3 w-full">
            <div class="m-5 items-center text-center flex flex-col border-2 p-3 space-y-4 border-gray-50 shadow-md">
                <div class="text-base font-semibold w-full text-left space-y-2">
                    <p class="font-light text-lg">Actividad de accesos</p>
                    <p class="font-bold text-sm">Primer acceso al sitio</p>
                    <p class="text-sm font-normal">{{ user.date_joined_formatted }}</p>
                    <p class="font-bold text-sm">Último acceso al sitio</p>
                    <p class="text-sm font-normal">{{ user.last_login_formatted }}</p>
                </div>
            </div>
            <div class="m-5 items-center text-center flex flex-col border-2 p-3 space-y-4 border-gray-50 shadow-md">
                <div class="text-base font-semibold w-full text-left space-y-2">
                    <p class="font-light text-lg">App para dispositivos móviles</p>
                    <p class="font-bold text-sm">Código QR para el acceso desde la app</p>
                    <p class="text-sm font-normal">Escanee el código QR con su app y accederá automáticamente. El código QR expirará en 10 minutos.</p>
                    <button @click="generateQR" class="bg-blue-700 flex font-normal text-sm justify-center transition duration-150 hover:bg-blue-900 text-white rounded-md mt-3 p-2">Ver Codigo QR</button>
                    <img v-if="qr_code!== ''" :src="qr_code" alt="asdasdasd">
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
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'Profile',
    data() {
        return {     
            user: {},        
            courses: [],
            qr_code:'',
        }
    },
    components:{
        Navbar,
    },
    mounted() {
        this.getUser()
        this.getCourses()
    },
    watch: {
        "$route.params.id": { // <-- here 
        handler () {
            this.getUser();
            this.getCourses();
        },
            immediate: true, // will call handler on component mount / create as well, so no need to call fn on mounted again
            deep:true,
        }
    },
    methods: {
        async getUser(){
            await axios.get(`user/${this.$route.params.id}/`)
            .then(response => {
                this.user = response.data 
            })
            .catch(error => {
                console.log(error);
            })
        },

        async getCourses(){ 
            await axios.get(`course/users/${this.$route.params.id}/in`) 
            .then(response =>{
                this.courses = response.data

            }) 
            .catch(error => {
                console.log(error); 
            })
        },
        async generateQR(){
            await axios.post(`user/generate-qr/${this.$route.params.id}/`,{
                url: this.$route
            })
            .then(response => {
                this.qr_code = response.data.url_image
            })
            .catch(error => {
                console.log(error);
            })
        },
    },

}
</script>