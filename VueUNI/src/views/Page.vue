<template >
    <nav class="border-gray-200 dark:bg-white ">
        <div class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4">
        <a href="#" class="flex items-center space-x-3 rtl:space-x-reverse no-underline">
            <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Uni-logo_transparente_granate.png/611px-Uni-logo_transparente_granate.png" class="h-8 mx-3"/>
            <p class="font-bold text-black text-sm">Pagina principal</p>
        </a>
        <button data-collapse-toggle="navbar-solid-bg" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-solid-bg" aria-expanded="false">
            <span class="sr-only">Open main menu</span>
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
            </svg>
        </button>
        <div class="hidden w-full md:block md:w-auto" id="navbar-solid-bg">
            <router-link :to="{name:'login'}" class="text-cyan-700  no-underline text-sm">Acceder</router-link>
        </div>
        </div>
    </nav>
    <div class="max-w-screen-2xl grid justify-center">
        <img alt="logo" class="rounded-md mt-8 " src="https://univirtual.uni.pe/pluginfile.php/1/theme_moove/sliderimage1/1704278506/UNI%20Dron.jpeg"/>
    </div>
            
</template>

