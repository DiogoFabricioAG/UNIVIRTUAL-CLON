<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Calificaciones Generales 📝</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2 flex flex-wrap justify-between"  >


            <div v-if="resumes.length" class="overflow-x-auto w-full">
                <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
                    <thead class="text-left">
                    <tr>
                        <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Curso</th>
                        <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Calificacion</th>
                        <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Aprobado</th>
                        <th class="px-4 py-2"></th>
                    </tr>
                    </thead>

                    <tbody class="divide-y divide-gray-200">
                        <tr v-for="(resume, index) in resumes" :key="index" >
                            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{ resume.course.name }}</td>
                            <td class="whitespace-nowrap px-4 py-2 text-gray-700">{{ resume.grade_prom }}</td>
                            <td class="whitespace-nowrap px-4 py-2 text-gray-700">
                                <p v-if="resume.passed">✅</p>
                                <p v-else>❌</p>
                            </td>
                            <td class="whitespace-nowrap px-4 py-2">
                            <router-link  v-if="!resume.get_certificate"
                                :to="{name:'course',params:{id:resume.course.id}}"
                                class="inline-block rounded bg-indigo-600 px-4 py-2 text-xs font-medium text-white hover:bg-indigo-700"
                            >
                                Ver Curso
                            </router-link>
                            </td>
                        </tr>

                    
                    </tbody>
                </table>
            </div>
            <div class="text-center p-1 bg-white w-[80%] mx-auto rounded-2xl" v-else>
                <h2 class="text-2xl font-bold ">Uds no cuenta con ningun curso concluido</h2>
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
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>
<style lang="">
    
</style>