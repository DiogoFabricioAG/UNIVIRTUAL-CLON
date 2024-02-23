<template>
    <Navbar/>
    <div class="bg-white max-w-[80vw] rounded-md mx-auto mt-10" >
        <h2  class="text-2xl font-sans font-bold p-5">Añadir un nuevo elemento 🎁 </h2>
        <form action="." @submit.prevent="submitForm" method="post" enctype="multipart/form-data" class="flex flex-col w-[50%] mt-3 mx-auto border p-2 rounded-md border-black">
            <label >Nombre del elemento</label>
            <input v-model="title" class="border border-black p-2 rounded-md" type="text">
            <label>Tipo del Material</label>
            <select v-model="materialtype" class="border rounded-sm border-black">
                <option value="PDF">PDF</option>
                <option value="News">News</option>
                <option value="Urls">Urls</option>
                <option value="Videos">Videos</option>
                <option value="Test">Test</option>
            </select>
            <label v-if="materialtype!=='Test' && materialtype!=='PDF'">Link del url</label>
            <input v-if="materialtype!=='Test' && materialtype!=='PDF'" v-model="link" class="border border-black p-1 rounded-md" type="text">
            <label v-if="materialtype!=='Test' && materialtype!=='Urls' && materialtype!=='Videos'" >Archivo</label>
            <input v-if="materialtype!=='Test' && materialtype!=='Urls' && materialtype!=='Videos'" id="file" class="border border-black p-1 rounded-md" ref="file" type="file">
            <label  v-if="materialtype!=='Test' && materialtype!=='Urls' && materialtype!=='Videos'" class="custom-file-upload border border-black p-3 mt-2">
                <span v-if="!image">Archivo</span>
                <span v-else>Archivos Cargados</span>
                <input class="border border-black p-1 rounded-md" @change="setimage" ref="file" type="file">
            </label>

            <label v-if="materialtype ==='Test'">Cantidad de Preguntas</label>
            <input v-model="problems" v-if="materialtype ==='Test'" class="border border-black p-1 rounded-md" type="number">
            <label v-if="materialtype ==='Test'">Cantidad de Soluciones</label>
            <input v-model="solutions" v-if="materialtype ==='Test'" class="border border-black p-1 rounded-md" type="number">
            <label v-if="materialtype ==='Test'">Tipo de Test</label>
            <select v-model="typeoftest" v-if="materialtype ==='Test'" class="border rounded-sm border-black">
                <option value="Quick (NON Q)">Quick (NON Q)</option>
                <option value="Practice (PC)">Practice (PC)</option>
                <option value="Parcial (EP)">Parcial (EP)</option>
                <option value="Final (EF)">Final (EF)</option>
                <option value="Sustitutorio (ES)">Sustitutorio (ES)</option>
            </select>
            <label  v-if="materialtype ==='Test'">Cantidad de Tiempo (Horas)</label>
            <input v-model="time" v-if="materialtype ==='Test'" step=0.01 class="border border-black p-1 rounded-md" type="number">
            <label  v-if="materialtype ==='Test'">Cantidad de Intentos</label>
            <input v-model="attempts" v-if="materialtype ==='Test'" class="border border-black p-1 rounded-md" type="number">
            
            <div class="flex mx-auto mt-2 space-x-1 ">
                <label>Cerrar al crear</label>
                <input v-model="close" type="checkbox">
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
    name:'addMaterials',
    components:{
        Navbar,
    },
    data() {
        return {
            title:'',
            materialtype:'',
            link:'',
            close:false,
            solutions:0,
            problems:0,
            image: false ,   
            time:0,
            attempts:0,
            typeoftest:'Quick (NON Q)'
        }
    },
    created() { 
        this.verify() //Lo colocamos en Created para que verifique antes esto quela carga del template
    },
    methods: {
        setimage(){
            this.image = true
        },
        verify(){
            if (this.userStore.user.role === 'Student'){
                this.$router.push({name:'notAllowed'}) // Modificar los lados no autenticados
            }
        },
        async submitForm(){
            let form = new FormData()
            if (this.materialtype!=='Test'){
                
                form.append('file',this.$refs.file.files[0])
                form.append('name',this.title)
                form.append('link',this.link)
                form.append('materialtype',this.materialtype)
                
                await axios.post(`course/${this.$route.params.id}/create_material/`,form,{
                    headers: {
                        "Content-Type":"multipart/form-data",
                    }
                }).then(response => {
                    console.log(response.data);
                    if (this.close){
                        this.$router.push({name:'course',params:{id:this.$route.params.id}})
                    }
                    else{
                        this.title = ''
                        this.materialtype = ''
                        this.link = ''
                        this.close = false
                        let file = document.getElementById('file')
                        file.value = null
                    }
                })
                .catch(error => {
                    console.log(error);
                })

            
            }
            else{
                form.append('problems',this.problems)
                form.append('typeoftest',this.typeoftest)
                form.append('time',this.time*3600)
                form.append('title',this.title)
                form.append('solutions',this.solutions)
                form.append('attempts',this.attempts)
                await axios.post(`quiz/createfor/${this.$route.params.id}/`,form,{
                    headers: {
                        "Content-Type":"multipart/form-data",
                    }
                }).then(response => {
                    console.log(response.data);
                    if (this.close){
                        this.$router.back()
                    }
                    else{
                        this.title = ''
                        this.materialtype = ''
                        this.link = ''
                        this.problems = 0
                        this.typeof = 'Quick (NON Q)'
                        this.time=0
                        this.close = false
                        let file = document.getElementById('file')
                        file.value = null
                    } 
                })
                .catch(error => {
                    console.log(error);
                })
            }
    },
    }
}

</script>