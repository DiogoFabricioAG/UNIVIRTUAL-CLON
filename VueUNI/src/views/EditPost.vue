<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto mt-10" >
        <h2  class="text-2xl font-sans font-bold p-5">Editar el Post 🧩 </h2>
        <form action="." @submit.prevent="submitForm" method="post" enctype="multipart/form-data" class="flex flex-col w-[50%] mt-3 mx-auto border p-2 rounded-md border-black">
            <label >Asunto</label>
            <input v-model="subject" class="border border-black p-2 rounded-md" type="text">
            <label >Cuerpo</label>
            <textarea v-model="body" class="border border-black rounded-md p-2" cols="30" rows="10"></textarea>
            <label>Tipo del Material</label>
            <select v-model="type" class="border rounded-sm border-black">
                <option value="Imagen">Imagen</option>
                <option value="Documento">Documento</option>
                <option selected value="None">None</option>
            </select>
            <label >Subir el Archivo</label> 
            <label class="custom-file-upload border border-black p-3">
                <span v-if="!file">Archivo</span>
                <span v-else>Archivos Cargados</span>
                <input class="border border-black p-1 rounded-md" @change="setimage" ref="file" type="file">
            </label>
            <div class="flex mx-auto mt-2 space-x-1 ">
                <label>Visible para todos los usuarios</label>
                <input v-model="visible" type="checkbox">
            </div>
            <button class="p-2 mt-2 hover:bg-white hover:text-black border border-black transition duration-300  bg-black text-white">Crear</button>
            <button @click="$router.back()" class="p-2 mt-2 hover:bg-white hover:text-gray-500 border border-gray-500 transition duration-300  bg-gray-500 text-white">Cancelar</button>
            <div class="mt-2">
                <div class="bg-red-500 text-center text-white p-1" v-for="(error, index) in errors" :key="index">
                    <p>{{ error }}</p>
                </div>
            </div>
            
            <div class="mt-2">
                <div class="bg-blue-400 text-center text-white p-1" v-for="(message, index) in messages" :key="index">
                    <p>{{ message }}</p>
                </div>
            </div>
            
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
    name:'editPost',
    components:{
        Navbar,
    },
    data() {
        return {
            subject:'',
            body:'',
            type:'',
            file: false, 
            messages:[],
            visible:false,
            errors: []
        }
    },
    mounted() {
        this.getPost()
    },
    created() { 
        this.verify() 
    },
    methods: {
        setimage(){
            this.image = true
        },
        verify(){
            if (this.userStore.user.id !== this.$route.params.id){
                this.$router.push({name:'notAllowed'}) // Modificar los lados no autenticados
            }
        },
        async getPost(){
            await axios.get(`blog/post/${this.$route.params.pk}/`)
            .then(response =>{
                this.subject = response.data.subject
                this.body = response.data.body
                if (response.data.get_image){
                    this.type = 'Imagen'
                }
                else if (response.data.get_file){
                    this.type = 'Documento'
                }
                else{
                    this.type = 'None'
                }
                console.log(response.data);
                this.visible = response.data.visible
            })
        }, 
        async submitForm(){
            let form = new FormData()
            form.append('subject',this.subject)
            form.append('body',this.body)
            form.append('type',this.type)
            form.append('archivo',this.$refs.file.files[0])
            form.append('visible',this.visible)
            axios.post(`blog/post/${this.$route.params.pk}/edit/`,form,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            }).then(response => {
                this.$router.back()
            })
            .catch(error => {
                console.log(error);

                this.errors.push('Error en la edicion del Post')
                if (!this.file){
                    this.errors.push('No se coloco nada en los archivos')
                    this.messages.push('Si no quiere editar el archivo, cambie el Tipo de material a None')
                }
            })
        }
    },

}

</script>