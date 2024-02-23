<template>
    <Navbar/>
    <Banner v-bind:user="user"/>
    <div class="bg-white max-w-[80vw]  min-h-[60vh] mt-4 rounded-2xl mx-auto p-4" >
        <h2 class="text-2xl font-sans font-bold p-5">Notificaciones 🔔</h2>
        <div class="mx-6 max-w-[80vw] min-h-[50vh] flex my">
            <div class="w-[30%] border max-h-[50vh] border-black overflow-auto">
                <button v-for="(item, index) in notifications" :key="index" @click="getNotification(item.id)" :id="item.id" class="p-1 text-left text-xs border-y  transition duration-150 border-black text-white font-normal" 
                :class="[item.read_it ? 'bg-slate-600 hover:bg-slate-800' : 'bg-blue-600 hover:bg-blue-700', '']">
                    <h1 v-if="item.send_by">{{ item.send_by.name }} realizo este tipo de notificacion: {{ item.typenotification }}</h1>
                    <h1 v-else>Ha recibido este tipo de notificacion: {{ item.typenotification }}</h1>
                    <p>{{item.created_at_formatted}}</p>
                </button>
                
            </div>
            
            <div class="w-[70%] border flex flex-col border-black">
                <div class="h-[20%] text-sm border-b space-y-1 p-2 border-black" v-if="notification.typenotification !== 'Received a Message' && notification.send_to.name !== ''">
                    <h1 class="font-bold text-xl">{{ notification.typenotification }}</h1>
                    <p>{{ notification.created_at_formatted }}</p>
                </div>
                <div class="h-[20%] text-sm border-b space-y-1 p-2 border-black" v-else-if="notification.send_by.name !== ''">
                    <h1 class="font-bold text-xl">{{ notification.typenotification }}</h1>
                    <p>{{ notification.created_at_formatted }}</p>
                </div>
                <div class="h-[20%] text-sm border-b space-y-2 p-2 border-black"  v-else>
                    <p>Titulo de la Notification</p>
                </div>
                <div class="h-[80%] p-2 " v-if="notification.typenotification !== 'Received a Message' && notification.send_to.name !== ''">
                    <p>
                        Ha recibido este tipo de notification: {{ notification.typenotification }}
                    </p>
                </div>
                <div class="h-[80%] p-2 " v-else-if="notification.send_by.name !== ''">
                    <p>
                        {{ notification.send_by.name}} realizo este tipo de notificacion: {{ notification.typenotification }}
                    </p>
                </div>
                <div class="h-[80%] p-2 " v-else>
                    <p>
                        Aqui ira la descripcion de tu notificacion
                    </p>
                </div>
                <button @click="deleteNotification()" v-if="notification.send_to.name !== ''" class="bg-red-600 text-white  border border-black p-2">Borrar Notificacion</button>
            </div>
        </div>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import Banner from '@/components/Banner.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'Notification',
    components:{
        Navbar,
        Banner,
    },
    data() {
        return {
            user: {},
            notifications : [],
            notification: {
                send_by: {
                    name:''
                },
                send_to:{
                    name:''
                }
            },
        }
    },
    mounted() {
        this.getNotifications()
        this.getUser()
    },

    methods: {
        async getUser(){
            await axios.get(`user/${this.userStore.user.id}/`)
            .then(response => {
                this.user = response.data 
            })
            .catch(error => { 
                console.log(error);
            })
        },
        async getNotifications(){
            await axios.get(`notification/mynotifications/`)
            .then(response => {
                this.notifications = response.data
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getNotification(id){
            await axios.post(`notification/mynotifications/${id}/`)
            .then(response => {
                this.notification = response.data 
                console.log(this.notification);
            })
            .catch(error => {
                console.log(error);
            })
        },
        async deleteNotification(){
            await axios.delete(`notification/mynotifications/${this.notification.id}/destroy/`)
            .then(response => {
                console.log(response.data);
                console.log(this.notifications);
                let value = document.getElementById(this.notification.id)
                value.setAttribute('hidden',true)
                this.notification = {}
            })
            .catch(error => {
                console.log(error);
            })
            
        }
    },
}


</script>