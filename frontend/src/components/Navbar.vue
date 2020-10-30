<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light mynav">
        <div class="container">
            <router-link :to="{ name: 'Home' }" class="navbar-brand">Question Time</router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <router-link :to="{ name: 'Home2' }" class="btn btn-sm btn-success">home</router-link>
                    </li>
                    <li class="nav-item mx-2">
                        <router-link :to="{ name: 'QuestionEditor' }" class="btn btn-sm btn-danger">Ask Question</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="btn btn-sm btn-warning" href="/accounts/logout/">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponant"
};
</script>

<style scoped>
.mynav {
    border: 1px solid gray;
}
.navbar-brand {
    font-weight: bold;
    font-size: 135%;
}
.navbar-brand:hover {
    color: darkorange;
}
</style>