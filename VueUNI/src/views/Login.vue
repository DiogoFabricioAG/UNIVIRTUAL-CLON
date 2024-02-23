<template>
    <div class="w-screen h-screen overflow-hidden flex relative">
        <img class="w-[100vw] h-[100%]" src="https://univirtual.uni.pe/pluginfile.php/1/theme_moove/loginbgimg/1704278506/Pabellon.jpg" alt="Pabellon">
        <div class="rounded-md justify-center items-center text-center flex flex-col md:flex-row  absolute left-1/4 w-1/2 h-1/2 top-1/4 bg-white">
            <div class="md:w-1/2 w-full border-r items-center flex flex-col border-gray-300">
                <img src="https://univirtual.uni.pe/pluginfile.php/1/theme_moove/logo/1704278506/logo_uni_2016.png" class="h-1/6" alt="lgoito">
                <form action="." @submit.prevent.="submitForm" class="flex flex-col w-full h-1/2 space-y-2">
                    <input type="text" class="rounded-lg text-sm p-1.5 border border-gray-400 mx-auto  w-[80%]" v-model="form.authcode" placeholder="Escribir su codigo UNI" >
                    <input type="password" class="rounded-lg text-sm p-1.5 mx-auto border border-gray-400 w-[80%]" v-model="form.password" placeholder="Escribir su contraseña">
                    <button type="submit" class="mx-auto w-[80%] p-1 px-2 border border-black text-black transition-colors duration-300 rounded-lg  hover:bg-gray-400">Acceder</button>
                    <p class="text-xs">¿No tienes cuenta? Crea una! <router-link :to="{name:'signup'}" class="text-xs no-underline hover:underline  text-blue-600">Click aqui</router-link></p> <!--Si se me da la gana hago una opcion de crear cuenta-->
                
                </form>
            </div>
            <div class="md:w-1/2 w-full">
                <img class="h-1/2 w-1/2 mx-auto border border-black" src="https://gestion.pe/resizer/NyDQqsomtC5A1hM4rmTnD8lwehE=/1200x1200/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/DL7ZRZB7LVHDFGWMTS74BY3X4Y.png" alt="entrada">
            </div>
        </div>

    </div>
</template>
  
<style scoped>

</style>
<script>
import axios from 'axios';
import { useUserStore } from '@/stores/user'
export default{
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
            
        }
    },
    data() {
        return {
            form: {
                authcode:'',
                password: '',
            },
            errors: []
            
        }
    },
    methods: {
        async submitForm(){
            this.errors=[]
            if (this.form.authcode === ''){
                this.errors.push('Your authcode is missing')
            }

            if (this.form.password === ''){
                this.errors.push('The password is missing')
            }
            if (!this.errors.length){
                await axios.post('/user/login/',this.form)
                .then(response => {

                    this.userStore.setToken(response.data)
                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access                    
                }).catch(error => {
                    console.log('error ',error);
                    this.errors.push('The email or the password are incorrect. Or the account is not activated')
                })
            }
            if (!this.errors.length){
                await axios.get('/user/me/')
                .then(response => {
                    this.userStore.setUserInfo(response.data)
                    this.$router.push({name: 'pageauth'})
                    
                }).catch(error => {
                    console.log('error ',error);
                })
            }
        },
        
        

    },
}

</script>
