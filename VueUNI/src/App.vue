<template>
  <RouterView />
  
</template>
<style>
body{
  margin: 0;
  background-color: rgb(242, 243, 247);
}
</style>
<script>
import { useUserStore } from './stores/user'
import axios from 'axios'
import { onMounted } from 'vue'
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore
        }
    },
    
    name:'App',
    beforeCreate() {
        this.userStore.initStore()
        const token = this.userStore.user.access
        if (token){
            axios.defaults.headers.common['Authorization']  = 'Bearer ' + token;   
        } else{
            axios.defaults.headers.common['Authorization'] = ''
        }

    },
}
</script>