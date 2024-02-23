import { defineStore } from "pinia";
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        user : {
            isAuthenticated : false,
            id : null,
            first_name : null,
            last_name : null,
            email: null,
            get_avatar:null,
            role: null,
            access: null,
            refresh: null,
        }
    }),
    actions: {
        initStore() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.first_name = localStorage.getItem('user.first_name')
                this.user.last_name = localStorage.getItem('user.last_name')
                this.user.role = localStorage.getItem('user.role')
                this.user.get_avatar = localStorage.getItem('user.get_avatar')            
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthenticated = true
                this.refreshToken()

                console.log('Initialized user:',this.user); 
            }
        },
        setToken(data){

            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true
            
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh',data.refresh)
        },
        removeToken(){
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = false
            this.user.role = false
            this.user.name = false
            this.user.get_avatar=null
            this.user.first_name = false
            this.user.last_name = false

            localStorage.setItem('user.access','')
            localStorage.setItem('user.refresh','')
            localStorage.setItem('user.id','')
            localStorage.setItem('user.first_name','')
            localStorage.setItem('user.last_name','')
            localStorage.setItem('user.role','')
            localStorage.setItem('user.get_avatar','')
            localStorage.setItem('user.email','')
        },
        setUserInfo(user){
            this.user.id =  user.id
            this.user.first_name =  user.first_name
            this.user.last_name =  user.last_name
            this.user.role =  user.role
            this.user.email =  user.email
            this.user.get_avatar =  user.get_avatar
            localStorage.setItem('user.id',this.user.id)
            localStorage.setItem('user.first_name',this.user.first_name)
            localStorage.setItem('user.last_name',this.user.last_name)
            localStorage.setItem('user.role',this.user.role)
            localStorage.setItem('user.email',this.user.email)
            localStorage.setItem('user.get_avatar',this.user.get_avatar)
        },
        refreshToken(token) {
            axios.post('/user/refresh/',{
                refresh : this.user.refresh
            }).then((response) => {
                this.user.access = response.data.access
                localStorage.setItem('user.access',response.data.access)

                axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
            }).catch((error) => {
                console.log(error);

                this.removeToken()
            })
            this.user.token = token
        } 
    }
})