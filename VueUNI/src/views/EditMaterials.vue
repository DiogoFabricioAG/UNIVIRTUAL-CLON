<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto mt-10" >
        <h2  class="text-2xl font-sans font-bold p-5">Editar {{ material.name }} 🛠</h2>
        <div class="w-[50%] mt-3 mx-auto border p-2 rounded-md border-black">
            <form action="." @submit.prevent="submitForm" method="post" enctype="multipart/form-data" class="flex flex-col">
                <label >Nombre del elemento</label>
                <input v-model="material.name" class="border border-black p-2 rounded-md" type="text">
                <label>Tipo del Material</label>
                <select v-model="material.materialtype" class="border rounded-sm border-black">
                    <option value="PDF">PDF</option>
                    <option value="News">News</option>
                    <option value="Urls">Urls</option>
                    <option value="Videos">Videos</option>
                    <option value="Test">Test</option>
                </select>
                <label v-if="material.materialtype!=='Test' && material.materialtype!=='PDF'">Link del url</label>
                <input v-if="material.materialtype!=='Test' && material.materialtype!=='PDF'" v-model="material.link" class="border border-black p-1 rounded-md" type="text">
                <label v-if="material.materialtype!=='Test' && material.materialtype!=='Urls' && material.materialtype!=='Videos'" class="custom-file-upload border border-black p-3 mt-2 mx-auto  w-[90%]">
                    <span class="">Archivo</span>
                    <input v-if="material.materialtype!=='Test' && material.materialtype!=='Urls' && material.materialtype!=='Videos'" class="border border-black p-1 rounded-md" ref="file" type="file">
                </label>
                
                <button class="p-2 mt-2 hover:bg-slate-700 transition duration-300 active:shadow-lg active:bg-slate-500 bg-black text-white">Editar</button>
            </form>
            <button @click="deletematerial" class="p-2 mt-2 w-full hover:bg-red-700 transition duration-300 active:shadow-lg active:bg-red-900 bg-red-600 text-white">Borrar</button>
        </div>
        
        
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import { useUserStore } from '@/stores/user';

import axios from 'axios'
export default{
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name:'editMaterials',
    components:{
        Navbar,
    },
    data() {
        return {
            material: {},
        }
    },
    mounted() {
        this.verify()
        this.getMaterial()
    },
    methods: {
        verify(){
            if (this.userStore.user.role === 'Student'){
                this.$router.push({name:'notAllowed'}) // Modificar los lados no autenticados
            }
        },
        async getMaterial(){
            axios.get(`course/material/${this.$route.params.pk}/`)
            .then(response => {
                this.material = response.data
            })
            .catch(error => {
                console.log(error);
            })
        },
        async submitForm(){
            let format = new FormData()
            format.append('file',this.$refs.file.files[0])
            format.append('name',this.material.name)
            format.append('link',this.material.link)
            format.append('materialtype',this.material.materialtype)
            axios.post(`course/material/${this.$route.params.pk}/edit/`,format,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            }).then(response => {
                this.$router.push({name:'course',params:{id:this.$route.params.id}})
            })
            .catch(error => {
                console.log(error);
            })
        },
        async deletematerial(){
            axios.delete(`course/material/${this.$route.params.pk}/delete/`)
            .then(response =>{
                console.log(response.data); 
                this.$router.push({name:'course',params:{id:this.$route.params.id}})
            })
            .catch(error => {
                console.log(error);
            })
        }
    },

}

</script>