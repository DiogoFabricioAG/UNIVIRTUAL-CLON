<template>
    <Navbar/>
    <Banner v-bind:user="user"/>
    <div class="bg-white max-w-[80vw] p-2  min-h-[100vh] m-4 rounded-2xl mx-auto" >
        <div class="w-[95%] flex justify-between mx-auto items-center">
            <h2 class="text-2xl font-sans font-bold p-5">Chat 🗣</h2>
            <router-link :to="{name:'groups'}" class="rounded-xl h-[10%] text-white p-2 hover:bg-blue-800 bg-blue-700">Create Group</router-link>
        </div>

        <div class="mx-6 max-w-full min-h-[8vh] h-auto  max-h-[40vh] flex ">
            <div class="w-[30%] border border-black max-h-[40vh] overflow-y-auto" >
                <div class="" v-for="(group, index) in groups" :key="index">
                    <button @click="getMessages(group.id)" class="bg-slate-400 w-full flex items-centers h-[10vh] space-x-2 p-1 text-left text-xs border-y hover:bg-blue-700 transition duration-150 border-black text-white font-normal">
                        <template v-if="group.typeof === 'Private'">
                            <template v-for="(user, index) in group.participants" :key="index">
                                <div>
                                    <img :src="user.get_avatar" class="rounded-full h-8 w-8" alt="My" v-if="user.id !== userStore.user.id">
                                    <p v-if="user.id !== userStore.user.id && friends.filter(object => object.id === user.id).length === 1">Amigos</p>
                                </div>
                                
                            </template>
                        </template>
                        <template v-else>
                            <img :src="group.get_image" class="rounded-full w-8 h-8" alt="My">
                        </template>
                        
                        <div>
                            <h1>{{ group.name }}</h1>
                        </div>
                        
                    </button>
                </div>
                
            </div>
            <div class="border w-[70%] flex flex-col h-[80vh] justify-between  border-black">
                <div class="text-sm flex justify-between h-[25%]: border-b items-center bg-slate-100 border-black"> 
                    <div class="flex items-center  space-y-2 space-x-3 p-2">
                        <button class="active:scale-90 transition duration-300"><svg id="Layer_1" style="enable-background:new 0 0 512 512;" version="1.1" viewBox="0 0 512 512" width="16px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M437.5,386.6L306.9,256l130.6-130.6c14.1-14.1,14.1-36.8,0-50.9c-14.1-14.1-36.8-14.1-50.9,0L256,205.1L125.4,74.5  c-14.1-14.1-36.8-14.1-50.9,0c-14.1,14.1-14.1,36.8,0,50.9L205.1,256L74.5,386.6c-14.1,14.1-14.1,36.8,0,50.9  c14.1,14.1,36.8,14.1,50.9,0L256,306.9l130.6,130.6c14.1,14.1,36.8,14.1,50.9,0C451.5,423.4,451.5,400.6,437.5,386.6z"/></svg></button>
                        <template v-if="group.typeof === 'Private'">
                            <template v-for="(user, index) in group.participants" :key="index">
                                <img :src="user.get_avatar" class="rounded-full mb-7  w-11 h-11" alt="My" v-if="user.id !== userStore.user.id">
                                <div>
                                    <h1 class="font-bold" v-if="user.id !== userStore.user.id">{{ user.first_name }} {{ user.last_name }}</h1>
                                </div>
                                
                            </template>
                        </template>
                        <template v-else-if="group.typeof==='Group'">
                            <img :src="group.get_image" class="rounded-full mb-7 w-11 h-11" alt="My">
                            <div>
                                <h1 class="font-bold">{{ group.name }}</h1>
                            </div>
                        </template>
                    </div>
                    <template v-if="imadmin && group.typeof === 'Group'">
                        <router-link v-if="group.exist" :to="{name: 'groupdetails',params:{id:group.id}}" class="bg-black hover:bg-slate-800 duration-300 text-white text-sm mx-2 rounded-xl p-1"> Detalles</router-link>
                    </template>
                    <template v-else-if="!imadmin && group.typeof === 'Group'">
                        <button @click="leftGroup(group.id)" class="p-2  hover:bg-red-700 rounded-xl mx-4 transition duration-300 active:shadow-lg active:bg-red-900 bg-red-600 text-white">Salir del Grupo</button>
                    </template>
                    
                    
                    
                </div> 
                <div class="flex flex-col overflow-auto h-[50%] "> 
                    <div class="p-2" v-for="(message, index) in messages" :key="index">
                        <div class="w-full" :class="[message.send_by.id === userStore.user.id ? 'flex justify-end' : '', '']" >
                            <div class="flex p-2 text-black max-w-[60%] items-center space-x-2 min-h-[3rem] text-sm rounded-md" :class="[message.send_by.id === userStore.user.id ? 'bg-blue-500' : 'bg-slate-200', '']">
                                <template v-if="message.get_image">
                                    <div :class="[message.send_by.id === userStore.user.id ? 'items-end' : 'items-start', 'flex flex-col']" >
                                        <img :src="message.send_by.get_avatar" alt="Dunno" class="w-8 h-8 rounded-full">
                                        <img :src="message.get_image" class="h-48 w-48 p-2 mx-auto"  alt="image">
                                        <span class="h-auto ">{{message.content}}</span>
                                    </div>
                                </template>
                                <template v-else>
                                    <img v-if="message.send_by.id !== userStore.user.id" :src="message.send_by.get_avatar" alt="Dunno" class="w-8 h-8 rounded-full">
                                    <span class="h-auto ">{{message.content}}</span>
                                    <img v-if="message.send_by.id === userStore.user.id" :src="message.send_by.get_avatar" alt="Dunno" class="w-8 h-8 rounded-full">
                                </template>
                                
                            </div>
                        </div>
                        
                        
                        
                    </div>
                </div>
                
            
                <form @submit.prevent="submitForm" method="post" class="h-[25%] text-sm flex justify-between  space-y-2 p-2 items-center ">
                    <label class="custom-file-upload"> 
                        <input type="file" @change="setimage" ref="file" id="file"/>
                        <svg class="feather feather-camera" :class="[image ?'text-green-500':'text-black']"  fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
                    </label>
                    <textarea v-model="content" name="Chat" cols="10" rows="10" class="w-full resize-none p-2 h-full bg-slate-100 border border-gray-600 rounded-md placeholder-slate-400" placeholder="Escribe un mensaje"></textarea>
                    <button class="rounded-full h-10 w-10 p-1 hover:bg-gray-200 duration-200 transition"><svg class="feather feather-send" fill="none" stroke="currentColor" stroke-linecap="round" width="32" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"  xmlns="http://www.w3.org/2000/svg"><line x1="22" x2="11" y1="2" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg></button>
                </form>
            </div>
        </div>
    </div>
    
</template>

<style>
.custom-file-upload {
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}
input[type="file"] {
    display: none;
}
</style>

<script>
import Navbar from '@/components/Navbar.vue';
import Banner from '@/components/Banner.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios'

export default {
    setup() {
        const userStore = useUserStore()
        return{
            userStore,
        }
    },
    name: 'Chat',
    components:{
        Navbar,
        Banner,
    },
    data() {
        return {
            user: {},
            group: {
                exist : false
            },
            imadmin:false,
            content: '',
            messages : [],
            groups: [],
            friends:[],
            image: false ,
        }
    },
    mounted() {
        this.getUser()
        this.getGroups()
        this.getFriends()
    },
    
    methods: {
        setimage(){
            this.image = true
        },
        async getFriends(){
            await axios.get(`user/friends/`)
            .then(response => {
                console.log(response.data);
                this.friends = response.data
            })
            .catch(error => {
                console.log(error);
            })
        },  

        async getUser(){
            await axios.get(`user/${this.userStore.user.id}/`)
            .then(response => {
                this.user = response.data
            })
            .catch(error => { 
                console.log(error);
            })
        },
        async submitForm(){
            let form = new FormData()
            form.append('content',this.content)
            form.append('image',this.$refs.file.files[0])
            await axios.post(`chat/connection/${this.group.id}/`,form,{
                headers: {
                    "Content-Type":"multipart/form-data",
                }
            })
            .then(response => {
                this.messages.push(response.data)
            })
            this.content = ''
        },
        async getGroups(){
            await axios.get('chat/mygroups/')
            .then(response => {
                this.groups = response.data
            })
            .catch(error => {
                console.log(error);
            })
        },
        async getMessages(id){
            await axios.get(`chat/messages/${id}/`)
            .then(response => {
                this.messages = response.data.messages 
                this.group = response.data.group
                this.group.exist = true
                this.imadmin = response.data.state
            })
            .catch(error => {
                console.log(error);
            })
        },
        async leftGroup(id){
            await axios.delete(`chat/room/${id}/left/`)
            .then(response => {
                console.log(response.data.room);
                this.groups = this.groups.filter(object => object.id !== id)
                this.group={
                    exist : false
                }
                this.messages=[]
                
            })
            .catch(error => {
                console.log(error);
            })
        },

    },
    
}


</script>