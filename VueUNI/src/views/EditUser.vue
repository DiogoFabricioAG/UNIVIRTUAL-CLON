<template>
    <Navbar/>
    <Banner v-bind:user="user"/>
    <div class="bg-white max-w-[80vw] mt-5 rounded-md mx-auto" >
        <div class="flex w-full items-center justify-between">
            <h2 class="text-2xl font-sans font-bold p-5">Editar al Usuario {{ user.first_name }} 🧰</h2>
            <router-link :to="{name:'password'}" class=" bg-black p-2 mr-3 text-white">Editar la Contraseña</router-link>
        </div>
        <div class="w-full  mx-auto flex ">
            <div class="w-1/2 border-r border-gray-400">
                <h2 class="text-2xl font-sans font-bold p-5">General</h2>
                <form action="." @submit.prevent="submitForm"  method="post" class="w-[90%] p-5  space-y-5" enctype="multipart/form-data">
                    <div class="flex w-full justify-between items-center">
                        <label>Nombre</label>
                        <input v-model="user.first_name" class="border border-black p-1 target:border-gray-700 rounded-md" type="text">
                    </div>
                    <div class="flex w-full justify-between">
                        <label>Apellido(s)</label>
                        <input v-model="user.last_name" class="border border-black p-1 target:border-gray-700 rounded-md" type="text">
                    </div>
                    <div class="flex w-full justify-between">
                        <label>Direccion de Correo</label>
                        <input v-model="user.email" class="border border-black p-1 target:border-gray-700 rounded-md" type="email">
                    </div>
                    <div class="flex w-full justify-between">
                        <label>Ciudad</label>
                        <input v-model="user.country" class="border border-black p-1 target:border-gray-700 rounded-md" type="text">
                    </div>
                    <div class="flex w-full justify-between">
                        <label>Pais</label>
                        <input v-model="user.city" class="border border-black p-1 selection:border-gray-700 target:border-gray-700 rounded-md" type="text">
                    </div>
                    <div class="flex w-full justify-between">
                        <label>Imagen de Perfil</label>
                        <label class="custom-file-upload border border-black p-3 mt-2">
                            <span>Imagen de Perfil</span>
                            <input class="border border-black p-1 rounded-md" ref="file" type="file">
                        </label>
                        
                    </div>
                    <button class="p-3 bg-black rounded-lg w-full text-white">Editar</button>
                </form>
            </div>
            <div class="w-1/2 border-l border-gray-400 flex items-center justify-center space-x-10">
                <h2 class="text-2xl font-sans font-bold p-5">Foto Perfil</h2>
                <img class="rounded-full w-[40%] border-2 border-black" :src="user.get_avatar" :alt="user.name">   
            </div>
        </div>
    </div>
    
</template>

<script>
import Banner from '@/components/Banner.vue';
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user';

import axios from 'axios'
export default{
    name:'editMaterials',
    components:{
        Navbar,
        Banner,
    },
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    created() {
        this.verify()
    },
    data() {
        return {
            material: {},
            user: {}
        }
    },
    mounted() {
        
        this.getUser()
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
        verify(){
            if (this.$route.params.id !== this.userStore.user.id){
                this.$router.push({name:'notAllowed'}) // Modificar los lados no autenticados
            }
        },
        async submitForm(){ 
            let format = new FormData()
            format.append('avatar',this.$refs.file.files[0])
            format.append('first_name',this.user.first_name)
            format.append('last_name',this.user.last_name)
            format.append('email',this.user.email)
            format.append('country',this.user.country)
            format.append('city',this.user.city)
            axios.post(`user/edit/${this.$route.params.id}/`,format,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            }).then(response => {
                console.log(response.data);
                this.$router.back()
            })
            .catch(error => {
                console.log(error);
            })
        },
    },

}

</script>