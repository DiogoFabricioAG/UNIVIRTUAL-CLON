<template>
    <div class="text-white bg-red-800 fixed h-[10vh] top-[10vh] left-0 w-full z-50">
        <div class="mx-20 w-[30%] p-1">
            <ul class="flex space-x-5 p-5">
                <li class="active:scale-90 transition duration-300 hover:underline"><router-link :to="{name:'course', params:{id:$route.params.id}}"><div>Curso</div></router-link></li>
                <li class="active:scale-90 transition duration-300 hover:underline"><router-link :to="{name:'personsCourse', params:{id:$route.params.id}}"><div>Participantes</div></router-link></li>
                <li class="active:scale-90 transition duration-300 hover:underline"><router-link :to="{name:'practices',params:{id:$route.params.id}}"><div>Practicas</div></router-link></li>
                <li class="active:scale-90 transition duration-300 hover:underline"><router-link :to="{name:'qualification',params:{id:$route.params.id}}"><div>Calificaciones</div></router-link></li>
            </ul>
        </div>
    </div>
    <div class="w-full h-[10vh]" ></div> <!--Ayudenme-->
</template>