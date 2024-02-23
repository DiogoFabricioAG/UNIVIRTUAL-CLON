<template >
    
    <div class="relative w-full h-[100vh] overflow-hidden ">
        <img class="w-full h-full top-0 select-none z-20 absolute" src="https://univirtual.uni.pe/pluginfile.php/1/theme_moove/loginbgimg/1704278506/Pabellon.jpg" alt="Pabellon">
        
        <form method="post" @submit.prevent="changePassword" class="p-10 space-y-3 bg-white md:w-[50%] w-[75%] flex flex-col overflow-y-auto h-auto left-[12.5%]  md:left-1/4 mt-5 absolute z-50">
            
            
            <h1 class="text-2xl  font-bold">Cambio de Contraseña</h1>
            

            <label for="contra" class="text-sm">Contraseña</label>
            <input v-model="old_password" type="password" id="contra" class="p-1 border rounded-lg border-black">
            <label for="contra1" class="text-sm">Nueva Contraseña</label>
            <input v-model="new_password1" type="password" id="contra1" class="p-1 border rounded-lg border-black">
            <label for="contra2" class="text-sm">Repetir Contraseña</label>
            <input v-model="new_password2" type="password" id="contra2" class="p-1 border rounded-lg border-black">
            <div class="bg-red-500 text-white p-2" v-for="(error, index) in errors" :key="index">
                <p>{{ error }}</p>
            </div>
            <button class="p-2 bg-blue-600 border border-blue-600 text-white hover:bg-white duration-200 hover:text-blue-600">Enviar</button>
            <router-link :to="{name:'profile',params:{id:userStore.user.id}}" class="p-2 bg-gray-600 text-center border border-gray-600 text-white hover:bg-white duration-200 hover:text-gray-600">Cancelar</router-link>
        </form>
    </div>
</template>
<script>
import { useUserStore } from '@/stores/user'
import axios from 'axios'

export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    data() {
        return {
            old_password: '',
            new_password2: '',
            new_password1: '',
            errors: [],
        }
    },
    methods: {
        async changePassword(){
            let formData = new FormData()
            formData.append('old_password',this.old_password)
            formData.append('new_password2',this.new_password2)
            formData.append('new_password1',this.new_password1)
            await axios.post('user/editpassword/',formData,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            })
            .then(response => {
                console.log(response.data);
                this.errors= []
                if (response.data.error === '')
                    this.$router.push({name:'profile',params:{id:this.userStore.user.id}})
                else{
                    this.errors.push(response.data.error)
                }
            })
            .catch(error => {
                console.log(error);
            })
        }
    },
}
</script>
