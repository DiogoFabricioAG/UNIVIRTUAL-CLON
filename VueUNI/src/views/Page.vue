<template >
    <nav class="border-gray-200 dark:bg-white ">
        <div class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="#" class="flex items-center space-x-3 rtl:space-x-reverse no-underline">
                <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Uni-logo_transparente_granate.png/611px-Uni-logo_transparente_granate.png" class="h-[8vh] mx-3"/>
                <p class="font-bold text-black text-sm">Pagina principal</p>
            </a>
            <div class="w-auto md:block" id="navbar-solid-bg">
                <router-link :to="{name:'login'}" class="text-cyan-700  no-underline text-sm">Acceder</router-link>
            </div>
        </div>
    </nav>
    <div class=" w-full ">
        <img alt="logo" class="rounded-md w-[90%] mx-auto mt-8 " src="https://univirtual.uni.pe/pluginfile.php/1/theme_moove/sliderimage1/1704278506/UNI%20Dron.jpeg"/>
    </div>
            
</template>

