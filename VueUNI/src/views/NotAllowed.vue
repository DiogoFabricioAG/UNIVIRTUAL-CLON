<template>
    <Navbar/>
    <div class="bg-red-600 max-w-[80vw] text-white p-5 space-y-5 rounded-md mx-auto mt-5" >
        <h2 class="text-2xl font-sans font-bold ">No esta Permitido esta accion</h2>
        <div class="flex space-x-3 items-center">
            <p class="">La accion realizada no se encuentra disponible en su cuenta.</p>
            <router-link class="my-2 hover:underline " :to="{name:'pageauth'}">Volver a la Pagina principal</router-link>
        </div>
        
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
export default {
    name: 'ErrorsDetected',
    components:{
        Navbar,
    },
    
}


</script>