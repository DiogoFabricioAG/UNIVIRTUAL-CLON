<template>
    <div class="w-full mt-8 ">
        <div class="flex items-center justify-center">
            <img :src="user.get_avatar" class="rounded-full max-h-[25vh]" alt="face">
            <div class="mx-4">
                <h1 class="text-3xl font-bold">{{user.first_name}} {{ user.last_name }}</h1>
                <p>{{ user.role }}</p>
            </div>
            <div class="space-y-2">
                <router-link  :to="{name:'chat'}" class="flex border select-none p-1 items-center active:scale-90 rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-message-circle" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>Mensaje</router-link>
                <template  v-if="user.id">
                    <router-link :to="{name: 'profile',params:{id:user.id}}" class="flex border p-1 select-none items-center active:scale-90 rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-user" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>Perfil</router-link>
                </template>
                <template v-else>
                    <router-link :to="{name: 'profile',params:{id:userStore.user.id}}" class="flex border p-1 select-none items-center active:scale-90 rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-user" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>Perfil</router-link>
                </template>
            </div>
            <div class="space-y-2 mx-8">
                <template  v-if="user.id">
                    <router-link :to="{name: 'blog',params:{id:user.id}}"  class="flex border p-1 items-center active:scale-90 select-none rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-book-open" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>Blog Personal</router-link>
                </template>
                <template v-else>
                    <router-link :to="{name: 'profile',params:{id:userStore.user.id}}" class="flex border p-1 select-none items-center active:scale-90 rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-user-plus" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" x2="20" y1="8" y2="14"/><line x1="23" x2="17" y1="11" y2="11"/></svg>Solicitud de amistad</router-link>
                </template>
                <template  v-if="user.id">
                    <router-link :to="{name: 'friendship'}" class="flex border p-1 select-none items-center active:scale-90 rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-user-plus" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" x2="20" y1="8" y2="14"/><line x1="23" x2="17" y1="11" y2="11"/></svg>Solicitud de amistad</router-link>
                </template>
                <template v-else>
                    <router-link :to="{name: 'friendship'}" class="flex border p-1 select-none items-center active:scale-90 rounded-lg hover:translate-x-5 transition duration-300 border-black max-h-[7vh]"><svg class="feather feather-user-plus" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" x2="20" y1="8" y2="14"/><line x1="23" x2="17" y1="11" y2="11"/></svg>Solicitud de amistad</router-link>
                </template>
            </div>
           
        </div>
    </div>    
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
    props:{
        user:Object,
    }, 
    name: 'Banner',
    
} 

</script>
