<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Mis Certificados 📝</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2 flex justify-between flex-wrap" v-if="resumes.length" >
        <div v-for="(resume, index) in resumes" :key="index" class="rounded-xl text-center border w-full md:w-[30%] mx-2 my-2 border-black">
            <img :src="resume.course.get_image" class="rounded-t-xl p-1" alt="nonImage">
            <div class="mt-2">
                <h2 class="font-bold text-xl">{{ resume.course.name }}</h2>
                <p>{{ resume.course.code }}</p>
            </div>
            <a :href="resume.get_certificate" target="_blank"  class="p-2 inline-block my-2 border duration-200 border-blue-700 rounded-lg hover:text-blue-700 text-sm hover:bg-white  bg-blue-700 focus:outline-none active:scale-95 text-white">Descargar Certificado</a>
        </div>

        
    </div>
    <div class="text-center p-1 bg-white w-[80%] mx-auto rounded-2xl" v-else>
        <h2 class="text-2xl font-bold ">Uds no cuenta con ningun curso concluido.</h2>
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
            resumes: []
        }
    },
    mounted() {
        this.getResumes()
    },

    methods: {
        async getResumes(){
            await axios.get('quiz/myresumes/')
            .then(response => {
                this.resumes = response.data
                this.resumes = this.resumes.filter(object => object.get_certificate !== null)
            })
            .catch(error => {
                alert('Algun error ha ocurrido')
            })
        }
    },
}
</script>
<style lang="">
    
</style>