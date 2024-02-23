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
            <input id="file" class="border border-black p-1 rounded-md" ref="file" type="file">
            <div class="flex mx-auto mt-2 space-x-1 ">
                <label>Visible para todos los usuarios</label>
                <input v-model="visible" type="checkbox">
            </div>
            
            <button class="p-2 mt-2 hover:bg-slate-700 transition duration-300 active:shadow-lg active:bg-slate-500 bg-black text-white">Crear</button>
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
            type:'None',
            visible:false,
        }
    },
    mounted() {
        this.getPost()
    },
    created() { 
        this.verify() //Lo colocamos en Created para que verifique antes esto quela carga del template
    },
    methods: {
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
                this.visible = response.data.visible
                console.log('asdbasdjjasdbj');
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
            })
        }
    },

}

</script>