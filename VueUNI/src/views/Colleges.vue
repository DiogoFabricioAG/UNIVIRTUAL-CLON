<template>
    <NavbarVue/>
    <div class="bg-white mt-5 max-w-[80vw] rounded-md mx-auto" >
        <h2 class="text-2xl font-sans font-bold p-5">Facultades 🏫</h2>
        <div class="flex flex-wrap w-full">
            <router-link  class="mt-3 mx-auto relative z-5 active:scale-95 duration-300 transition-transform" v-for="college in colleges" :key="college.id" :to="{name : 'college',params:{id:college.id}}">
            <div class="w-[350px]  p-4 overflow-hidden shadow-md">
                <img class="min-h-[50%] " :src="college.get_image" :alt="college.name">
                <div class="px-6 py-4">
                    <div class="text-lg font-bold mb-2">{{ college.short_name }}</div>
                    <p>{{ college.name }}</p>
        
                </div>
                
            </div>
            </router-link>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import NavbarVue from '@/components/Navbar.vue';

export default{

    name:'Colleges',
    components:{
        NavbarVue,
    },
    data() {
        return {
            colleges:[]      
        }
    },
    mounted(){
        this.getColleges()
    },
    methods: {
        async getColleges(){
            await axios.get('colleges/all/')
            .then(response =>{
                this.colleges = response.data
            })
            .catch(error => {
                console.log(error);
            })
        }
    },

}

</script>