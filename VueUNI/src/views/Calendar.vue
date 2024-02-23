<template>
    <Navbar/>
    <div class="max-w-screen-2xl m-5 mx-20">
        <div>
            <h1 class="text-3xl font-sans font-bold">Area Personal 📌</h1>
        </div>
    </div> 
    <div class="bg-white max-w-[80vw] rounded-md mx-auto p-2" >
        <div class="flex justify-between mt-4 items-center w-full">
            <h1 class="text-2xl font-sans font-bold">Calendario 📅</h1>
            <router-link :to="{name:'createevent'}" class="bg-blue-600 mx-3 text-white rounded-xl hover:bg-blue-800 duration-300 p-2">Crear Evento</router-link>
        </div>
        {{ currentday }}
        <div class="rounded-t-2xl border m-5 border-black">
            <div class="rounded-t-2xl w-full flex justify-between text-white p-2 bg-black">
                <button @click="yearGrow('DOWN')"><svg class="feather feather-chevron-left" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><polyline points="15 18 9 12 15 6"/></svg></button>
                <p>{{ year }}</p>
                <button @click="yearGrow('UP')"><svg class="feather feather-chevron-right" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><polyline points="9 18 15 12 9 6"/></svg></button>
            </div>
            <div class="w-full flex justify-between text-black p-1 bg-gray-300">
                <button @click="monthGrow('DOWN')"><svg class="feather feather-chevron-left" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><polyline points="15 18 9 12 15 6"/></svg></button>
                <p>{{ formatmonth }}</p>
                <button @click="monthGrow('UP')"><svg class="feather feather-chevron-right" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><polyline points="9 18 15 12 9 6"/></svg></button>
            </div>
            <div class="grid grid-cols-7 text-black text-center">
                <span v-for="index in 7" :key="index" class="border border-black">{{ createdays(index) }}</span>
            </div>
            <div class="grid grid-cols-7 text-black ">
                <div v-for="(index) in initialday" :key="index" class="text-center h-[20vh] border border-black   bg-white">

                </div>
                <router-link :to="{name:'eventdescription',query:{date:String(year)+'-'+String(month+1).padStart(2, '0')+'-'+String(index).padStart(2,'0')}}"  v-for="(index) in daysinamonth" :key="index" class="text-center h-[20vh] border border-black  text-white "
                :class="[currentday === String(year)+'-'+String(month+1).padStart(2, '0')+'-'+String(index).padStart(2,'0') ? 'bg-slate-700 hover:bg-slate-800' : 'bg-blue-800 hover:bg-blue-900', '']">
                    <div @click="" class="p-3 w-full items-center flex flex-col justify-center h-full">
                        {{ index }}

                        <div v-for="(item, index) in getEventsFromDate(String(year)+'-'+String(month+1).padStart(2, '0')+'-'+String(index).padStart(2,'0'))" :key="index">
                            <p class="text-xs">Evento {{ index + 1 }}: {{ item.title }}</p>
                        </div>
                    </div>
                    
                </router-link>
                
                
                
            </div>
        </div>
    </div>
    
</template>
<script>
import Navbar from '@/components/Navbar.vue';
import dayjs from 'dayjs'
import axios from 'axios'
export default {
    components:{
        Navbar
    },
    data() {
        return {
            year: dayjs().year(),
            month: dayjs().month(),
            day: dayjs().day(1),
            events: []
        }
    },
    computed: {
        formatmonth: function() {
            return dayjs().month(this.month).format('MMMM')
        },
        daysinamonth: function(){
            return dayjs().month(this.month).year(this.year).daysInMonth()
        },
        initialday: function(){
            let day = dayjs().year(this.year).month(this.month).startOf('month').$d
            let daysarray = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
            return daysarray.indexOf(day.toLocaleDateString('en-US', { weekday: 'long' }).substring(0,3)) ;
        },
        currentday: function(){
            return dayjs().year() + '-' + String(dayjs().month()+1).padStart(2,'0') +  '-' + String(dayjs().date()).padStart(2,'0')
        }

    },
    mounted() {
        this.getEvents()
    },
    methods: {
        createdays(days){
            let date = dayjs().day(days).$d
            return date.toLocaleDateString('en-US', { weekday: 'long' }).substring(0,3)
        },
        async getEvents(){
            await axios.get(`calendar/get-events/`)
            .then(response => {
                this.events = response.data
            })
            .catch(error => {
                console.log(error); 
            })
        },
        getEventsFromDate(date){
            return this.events.filter(object => object.date_event === date);
        },
        yearGrow(state){
            let date = this.day.$d
            console.log(date.toLocaleDateString('en-US', { weekday: 'long' }).substring(0,3));

            if (state == 'UP'){
                this.year++
                
            } 
            else{
                this.year--
            }
        },
        monthGrow(state){
            if (state == 'UP'){
                if (this.month === 11){
                    this.year++
                    this.month=-1
                }
                this.month++ 
                
                 
            } 
            else{
                if (this.month === 0){
                    this.year--
                    this.month=12
                }
                this.month--
            }
        },
        getDate(day){
            let date = new Date(this.year,this.month,day)
            console.log(date);
        }
    },
}
</script>
