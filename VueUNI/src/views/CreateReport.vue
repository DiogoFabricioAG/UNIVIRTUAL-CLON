<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-5 mt-4" >
        <h2  class="text-2xl font-sans font-bold p-5">Crear un Grupo ⚔</h2>
        <form action="." @submit.prevent="createReport" method="post" enctype="multipart/form-data" class="flex flex-col w-[50%] mt-3 mx-auto border p-2 rounded-md border-black">
            <label >Titulo del Reporte</label>
            <input v-model="title" class="border border-black p-2 rounded-md" placeholder="Coloque el titulo del Reporte" type="text">            
            <label >Contenido del Reporte</label>
            <textarea v-model="content" cols="30" rows="10"  class="border border-black p-2 rounded-md resize-none" placeholder="Coloque el contenido del Reporte"></textarea>
        
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
            content: '',
        }
    },
    methods: {
        async createReport(){
            await axios.post(`course/report/create/${this.$route.params.pk}/course/${this.$route.params.id}/`,{
                title : this.title,
                content: this.content,
            })
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