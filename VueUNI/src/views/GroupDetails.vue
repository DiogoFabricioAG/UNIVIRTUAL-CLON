<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto mt-10" >
        <h2  class="text-2xl font-sans font-bold p-5">Detalles del grupo: {{ group.name }} 🥂 </h2>
        <div class="w-[50%] mt-3 mx-auto border p-2 space-y-2 rounded-md border-black">
            <form action="." @submit.prevent="editedGroup" method="post" enctype="multipart/form-data" class="flex flex-col">
                <label >Nombre del Grupo</label>
                <input v-model="group.name" class="border border-black p-2 rounded-md" type="text">
                <label>Ascender a Admin</label>
                <select v-model="admin"  class="border rounded-sm p-1 border-black">
                    <option value="None">None</option>
                    <option v-for="(participant, index) in group.participants" :key="index" :value="participant.authcode">{{ participant.name }}</option>

                </select>
                <label class="custom-file-upload border border-black p-3 mt-2">
                    <span>Imagen del Grupo</span>
                    <input class="border border-black p-1 rounded-md" ref="file" type="file">
                </label>
                
                <button class="p-2 mt-2 hover:bg-slate-700 transition duration-300 active:shadow-lg active:bg-slate-500 bg-black text-white">Editar</button>
            </form>
            <button @click="leftGroup" class="p-2 mt-2 w-full hover:bg-red-700 transition duration-300 active:shadow-lg active:bg-red-900 bg-red-600 text-white">Salir del Grupo</button>
        </div>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';

import axios from 'axios'
export default {
    components:{
        Navbar,
    },
    data() {
        return {
            name:'',
            admin: '',
            group: {},
        }
    },
    mounted() {
        this.getGroup()
    },
    methods: {
        async getGroup(){
            await axios.get(`chat/room/${this.$route.params.id}/`)
            .then(response => {
                this.group = response.data
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
        async editedGroup(){
            let form = new FormData()
            form.append("name",this.group.name)
            form.append("admin",this.admin)
            form.append('image',this.$refs.file.files[0])
            await axios.post(`chat/room/${this.$route.params.id}/edited/`,form,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            })
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error);
            })
        },
        async leftGroup(){
            await axios.delete(`chat/room/${this.$route.params.id}/left/`)
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
