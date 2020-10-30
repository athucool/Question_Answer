<template>
    <div class="home">
        <div class="container mt-2">
            <div v-for="question in questions"
                    :key="question.pk">
                <p class="mb-0">posted by <span style="color:red;font-weight:bold"> {{question.author}} </span> </p>
                <h2>
                    <router-link 
                        :to="{name: 'question', params: {slug: question.slug} }" class="question_cls">
                        {{ question.content }}
                    </router-link>
                </h2>
                <p>Answer: {{question.answers_count }}</p>
                <hr>
            </div>
        <div class="mt-4">
            <p v-show="loadingQuestion">...Loading...</p>
            <button v-show="next"
                    @click="getQuestions"
                    class="btn btn-success">Load more
            </button>
        </div>
         </div>
        
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name: "Home",

    data() {
        return {
            questions: [],
            next: null,
            loadingQuestion: false
        }
    },

    methods: {
        getQuestions() {
            let endpoint = "/api/questions/";
            if (this.next) {
                endpoint=this.next;
            }
            this.loadingQuestion= true;
            apiService(endpoint)
            .then(data => {
                this.questions.push(...data.results)
                this.loadingQuestion= false;
                if(data.next) {
                    this.next = data.next;
                } else {
                    this.next =false
                }
            })
        }
    },
    created() {
        var that = this;
        that.getQuestions()
        console.log(that.questions)
    }
};
</script>

<style >

.question_cls {
    font-weight:bold;
    color: rgb(87, 164, 236);
}
.question_cls:hover{
    color: chartreuse;
    text-decoration: none;
}
</style>