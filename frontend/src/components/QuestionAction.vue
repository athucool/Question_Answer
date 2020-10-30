<template>
    <div>
        <router-link 
            :to="{name: 'QuestionEditor', params: {slug:slug} }"
            class="btn btn-sm btn-outline-info mr-2">
            Edit
        </router-link>
        <button class="btn btn-sm btn-outline-danger" @click="DelectQuestion">Delete</button>
    </div>
     
</template>
<script>
import { apiService } from "../common/api.service.js"

export default {
    name:"QuestionActions",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    methods: {
        async DelectQuestion(){
            let endpoint = `/api/questions/${this.slug}/`;
            try{
                await apiService(endpoint,"DELETE");
                this.$router.push("/");
            }
            catch(err){
                console.log(err)
            }
        }
    }
    
}
</script>

<style scoped>

</style>