<template >
    <div class="relative w-full h-[100vh] overflow-hidden ">
        <img class="w-full h-full top-0 select-none z-20 absolute" src="https://univirtual.uni.pe/pluginfile.php/1/theme_moove/loginbgimg/1704278506/Pabellon.jpg" alt="Pabellon">
        <form method="post" @submit.prevent="createUser" class="p-10 space-y-3 bg-white w-[50%] flex flex-col overflow-y-auto h-full left-1/4 mt-5 absolute z-50">
            <h1 class="text-2xl font-bold">Nueva cuenta</h1>
            <label for="nombre" class="text-sm">Nombres del Usuario</label>
            <input v-model="name" type="text" id="nombre" class="p-1 border rounded-lg border-black">
            <label for="apellido" class="text-sm">Apellidos del Usuario</label>
            <input v-model="lastname" type="text" id="apellido" class="p-1 border rounded-lg border-black">
            <label for="pais" class="text-sm">Pais</label>
            <input v-model="country" type="text" id="pais" class="p-1 border rounded-lg border-black">
            <label for="ciudad" class="text-sm">Ciudad</label>
            <input v-model="city" type="text" id="ciudad" class="p-1 border rounded-lg border-black">
            <label for="codigo" class="text-sm">Codigo de Autenticacion</label>
            <input v-model="authcode" type="text" id="codigo" class="p-1 border rounded-lg border-black">
            <label for="descripcion" class="text-sm">Descripcion del Usuario</label>
            <input v-model="description" type="text" id="codigo" class="p-1 border rounded-lg border-black">
            <label for="correo" class="text-sm">Correo Electronico del Usuario</label>
            <input v-model="email" type="email" id="correo" class="p-1 border rounded-lg border-black">
            <label for="rol" class="text-sm">Correo Electronico del Usuario</label>
            <select v-model="role" id="rol" class="p-1 border rounded-lg border-black">
                <option selected value="Student">Estudiante</option>
                <option value="Professor">Profesor</option>
            </select>
            <label for="contra" class="text-sm">Contraseña</label>
            <input v-model="password1" type="password" id="contra" class="p-1 border rounded-lg border-black">
            <label for="contra1" class="text-sm">Repetir Contraseña</label>
            <input v-model="password2" type="password" id="contra1" class="p-1 border rounded-lg border-black">
            <div class="bg-red-500 text-white p-2" v-for="(error, index) in errors" :key="index">
                <p>{{ error }}</p>
            </div>
            <button class="p-2 bg-blue-600 border border-blue-600 text-white hover:bg-white duration-200 hover:text-blue-600">Enviar</button>
            <router-link :to="{name:'login'}" class="p-2 bg-gray-600 text-center border border-gray-600 text-white hover:bg-white duration-200 hover:text-gray-600">Cancelar</router-link>
        </form>
    </div>
  

</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            name:'',
            lastname:'',
            country:'',
            city:'',
            authcode:'',
            description:'',
            email:'',
            role:'Student',
            password1:'',
            password2:'',
            errors: [],
        }
    }, 
    methods: {
        
        async createUser(){
            let form = {
                email: this.email, 
                authcode:   this.authcode,
                country:    this.country,
                city:       this.city,
                description: this.description,
                role:       this.role,
                last_name:  this.lastname,
                first_name: this.name,
                password1:  this.password1,
                password2:  this.password2,
            }
            await axios.post('user/signup/',form)
            .then(response => {
                this.errors = []
                if (response.data.error === ''){
                    this.$router.push({name:'login'})
                }
                else{
                    this.errors.push(response.data.error)
                }
            })
            .catch(error => {
                console.log(error);
            })
        },
    },
}
</script>
