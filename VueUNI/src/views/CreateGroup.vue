<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-5 mt-4" >
        <h2  class="text-2xl font-sans font-bold p-5">Crear un Grupo ⚔</h2>
        <form action="." @submit.prevent="createGroup" method="post" enctype="multipart/form-data" class="flex flex-col w-[50%] mt-3 mx-auto border p-2 rounded-md border-black">
            <label >Nombre del Grupo</label>
            <input v-model="title" class="border border-black p-2 rounded-md" placeholder="Coloque el nombre del Grupo" type="text">            
            <label>Imagen del Grupo</label>
            <label class="custom-file-upload border border-black p-3 mt-2">
                <span>Imagen del Grupo</span>
                <input class="border border-black p-1 rounded-md" ref="file" type="file">
            </label>
    
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
    name:'addMaterials',
    components:{
        Navbar,
    },
    data() {
        return {
            title:'',
        }
    },
    methods: {
        async createGroup(){
            let formdata = new FormData()
            formdata.append('title',this.title)
            formdata.append('file',this.$refs.file.files[0])
            await axios.post('chat/creategroups/',formdata)
            .then(response => {
                this.$router.back()
            })
            .catch(error =>{
                console.log(error);
            })

        }
    }
}

</script>