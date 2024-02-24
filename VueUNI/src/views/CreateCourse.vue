<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20 flex items-center justify-between">
        <div>
            <h1 class="text-3xl font-sans font-bold">{{ code }} {{ name }}</h1>
        </div>
    </div>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto" >
        <h2 class="text-2xl font-sans font-bold p-5">Creacion del Curso: </h2>
        <div class="flex">
            <div class="mt-3 mx-1 w-[30%]">
                <div class="max-w-[343px] min-h-[395px] p-4 overflow-hidden shadow-md">
                    <img v-if="imagePreview" :src="imagePreview" class="min-h-[50%]" alt="Aqui ira tu imagen">
                    <div class="px-6 py-4">
                        <div class="text-sm mb-2">{{ code }} {{ name }}</div>
                    </div>
                    
                    <router-link :to="{name:'profile',params:{id:userStore.user.id}}" class="flex">
                        <img :src="user.get_avatar" class="rounded-full max-w-[20%] inline-block" alt="Name of teacher">
                        
                        <div class="inline-block w-full">
                            <p class="inline-blockpx-3 hover:underline py-1 text-[10.5px]  font-semibold ">{{ userStore.user.first_name }} {{userStore.user.last_name}}</p>
                            <p class=" bg-gray-200 rounded-full w-full text-[9px] px-3 py-1 font-semibold text-gray-700">Profesor</p>
                        </div>
                    </router-link>
                </div>
            </div>
            <div class="mt-3 mx-1 w-[50%]">
                    <form  action="." method="post" class="w-full left m-2 space-y-2" @submit.prevent="submitForm">
                        <div class="space-y-2 flex flex-col ">
                            <label>Nombre del Curso:</label>
                            <input v-model="name" type="text" class="rounded-md w-[100%] border p-1 border-black" >
                            <label>Carrera:</label>
                            <select v-model="career" class="rounded-md w-[100%] border p-1 border-black">
                                <option v-for="(career, index) in careers" :key="index" :value="career.name">{{ career.name }}</option>
                            </select>
                            <div class="flex items-center space-x-2">
                                <label>Codigo:</label>
                                <input v-model="code" type="text" placeholder="ABC12U" class="rounded-md w-[100%] border p-1 border-black" > 
                                <label>Seccion:</label>
                                <input v-model="section" type="text" placeholder="U" class="rounded-md w-[100%] border p-1 border-black" > 
                            </div>
                            <label class="custom-file-upload border space-x-4 border-black p-3 mt-2">
                                <span>Imagen del curso</span>
                                <span v-if="imagePreview">Archivo Cargado</span>
                                <input class="border border-black p-1 rounded-md" ref="file" @change="previewImage" type="file">
                            </label>

                           
                        </div>
                        <button class="w-1/2 p-2 active:scale-90  hover:bg-slate-800 duration-200 text-white bg-black">Crear Curso</button>
                    </form>

            </div>
        </div>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user';

import axios from 'axios'
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'Notification',
    components:{
        Navbar,
    },
    data() {
        return {
            name: '',
            code: '',
            section:'',
            career:'Ingeniería de Sistemas',
            user:{},
            imagePreview: null,
            careers: [],
        }
    },
    mounted() {
        this.getUser()
        this.getCareer()
    },
    methods: {
        async getCareer(){
            await axios.get('colleges/allcareers/')
            .then(response => {
                this.careers = response.data
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getUser(){
            await axios.get(`user/${this.userStore.user.id}/`)
            .then(response => {
                this.user = response.data 
            })
            .catch(error => {
                console.log(error);
            })
        },
        previewImage(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = () => {
                    this.imagePreview = reader.result;
                };
                reader.readAsDataURL(file);
            }
        },
        async submitForm(){
            let formdata = new FormData()
            formdata.append('name',this.name)
            formdata.append('code',this.code)
            formdata.append('seccion',this.section)
            formdata.append('career',this.career)
            formdata.append('image',this.$refs.file.files[0])
            await axios.post('course/create/',formdata,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            })
            .then(response => {
                console.log(response.data);
                this.$router.push({name:'pageauth'})
            })
            .catch(error => {
                console.log(error);
            })
        },    
    },
}


</script>