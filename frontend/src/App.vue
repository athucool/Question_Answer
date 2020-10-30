<template>
    <div id="app">
        <NavbarComponant />
        <router-view />
    </div>
</template>


<script>
import { apiService } from "../src/common/api.service.js"

import NavbarComponant from "./components/Navbar";
export default {
    name: "App",
    components: {
        NavbarComponant
    },
    methods: {
        async setUserInfo() {
            const data = await apiService("/api/users/");
            const requestUser =data["username"];
            console.log("requestUser",requestUser)
            window.localStorage.setItem("username",requestUser);
             
        }
    },
    created(){
        this.setUserInfo()
    }
};
</script>

<style>
html,
body {
    font-family:"Sofia";
}
.btn:focus {
    box-shadow: none !important;
}
</style>
