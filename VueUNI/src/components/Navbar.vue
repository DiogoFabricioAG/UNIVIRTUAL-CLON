<template>
    <nav class="border-gray-200 dark:bg-white shadow-lg text-sm fixed h-[10vh] top-0 left-0 w-full z-50">
        <div class="max-w-screen-2xl flex justify-between flex-wrap items-center mx-auto p-2 ">
            <div class="flex space-x-1 md:space-x-3 items-center text-[10px]" >
                <router-link :to="{name:'pageauth'}" class="flex items-center space-x-3 rtl:space-x-reverse no-underline">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Uni-logo_transparente_granate.png/611px-Uni-logo_transparente_granate.png" class="md:h-12 h-8 mx-3"/>
                    <p class="font-bold text-black md:text-sm">Pagina principal</p>
                </router-link>
                <router-link :to="{name: 'calendar'}" class="no-underline">
                    <p class="text-black md:text-sm">Area Personal</p>
                </router-link>
                <router-link :to="{name:'colleges'}" class="no-underline">
                    <p class="text-black md:text-sm">Mis Cursos</p>
                </router-link>
                
            </div>
            
            <div class="md:w-auto flex md:space-x-3 flex-row" id="navbar-solid-bg">
                <router-link :to="{name: 'notification'}"><svg class="feather md:h-[24px] h-[16px] feather-bell" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></router-link>
                <router-link :to="{name: 'chat'}"><svg class="feather md:h-[24px] h-[16px] feather-message-circle" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg></router-link>
                <router-link :to="{name: 'profile',params:{id:userStore.user.id}}"><svg class="feather md:h-[24px] h-[16px] feather-user" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></router-link>
                <button @click="logout"><svg class="feather md:h-[24px] h-[16px] feather-log-out" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg></button>
            </div>
        </div>
    </nav>
    <div class="w-full h-[10vh]" ></div> <!--Ayudenme-->
</template>
<script>
import { useUserStore } from '@/stores/user';

export default { 
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    methods: {
        logout(){
            this.userStore.removeToken()
            this.$router.push({name:'login'})
        } 
    },
}
</script>
