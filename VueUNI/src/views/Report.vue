<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Mis Reportes Personales 💼</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" v-if="reports.length" >
        <h2 class="text-2xl font-sans font-bold">Lista de Informes</h2>
        <div class="w-[90%] my-3 mx-auto border border-black rounded-xl p-2" v-for="(report, index) in reports" :key="index">
            <div class="flex space-x-4 items-center">
                <img :src="report.created_by.get_avatar" class="h-11 w-11 rounded-full" alt="nada">
                <div>   
                    <h3 class="font-bold text-xl">
                        {{ report.title }}
                    </h3>
                    <p>{{ report.created_at_formatted }}</p>
                </div>
            </div>
            <div class="my-2 text-gray-500 text-sm">
                <p>Profesor: {{ report.created_by.name }}</p>
                <p>Curso: {{ report.reference_course.name }}</p>
            </div>
            <div class="my-2">
                <p>{{ report.content }}</p>
            </div>

        </div>
    </div>
    <div class="text-center p-1 bg-white w-[80%] mx-auto rounded-2xl" v-else>
        <h2 class="text-2xl font-bold">Uds no cuenta con ningun informe recibido.</h2>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import axios from 'axios';


export default {
    components:{
        Navbar,
    },
    data() {
        return {
            reports: []      
        }
    },
    mounted() {
        this.getReports()
    },
    methods: {
        async getReports(){
            await axios.get(`course/report/`)
            .then(response => {
                this.reports = response.data
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>
