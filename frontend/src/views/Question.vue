<template>
    <div class="single_question mt-2">
        <div v-if="question" class="container">
            <h1>{{question.content}}</h1>
            <p class="mb-0">
                posted by
                <span style="color:red;font-weight:bold">{{question.author}}</span>
            </p>
            <p>created at: {{question.created_at}}</p>
            <hr />
             
            <QuestionActions
                :slug=question.slug
            />
            <div v-if="userHasAnswered">
                <p style="color:green">user has answer</p>
            </div>
            <div v-else-if="showForm">
                <form class="card" @submit.prevent="Onsubmit">
                    <div class="card-header px-3">Answer the question</div>
                    <div class="card-block">
                        <textarea
                            class="form-control"
                            placeholder="Answer the question"
                            v-model="newAnswerBody"
                            rows="10"
                        ></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-success">Submit your answer</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2">error: {{error}}</p>
            </div>
            <div v-else>
                <button class="btn btn-success" @click="showForm = true">Answer the question</button>
            </div>
        </div>
        <div v-else>
            <h1 id="notfound">{{message}}</h1>

        </div>

        <div v-if="question" class="container">
            <AnswerComponent v-for="answer in answers"  :answer="answer" :requestUser="requestUser" :key="answer.id" @delete-answer="deleteAnswer" />
             <div class="mt-4">
                <p v-show="loadingAnswer">...Loading...</p>
                <button v-show="next" @click="getQuestionAnswer" class="btn btn-success">Load more</button>
            </div>
        </div>
    </div>
</template>


<script>
import AnswerComponent from "../components/Answerss.vue";
import QuestionActions from "../components/QuestionAction.vue";
import { apiService } from "../common/api.service.js";
export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    components: { AnswerComponent,
    QuestionActions },
    data() {
        return {
            question: {},
            answers: [],
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false,
            next: null,
            loadingAnswer: false,
            requestUser:null
        };
    },
    computed: {
            isQuestionAuthor() 
            {
                return this.question.author === this.requestUser;
            }
        },
    methods: {
        setPageTitle(title) {
            document.title = title;
        },
        setRequestUser(){
            this.requestUser=window.localStorage.getItem("username")
        },
        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint).then(data => {
                if (data){
                    this.question = data;
                    this.userHasAnswered = data.user_has_answered;
                    this.setPageTitle(data.content);
                }else{
                    this.question=null;
                    this.setPageTitle="404-page not found"
                }

               
            });
        },
        getQuestionAnswer() {
            let endpoint = `/api/questions/${this.slug}/answers/`;
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingAnswer = true;
            apiService(endpoint).then(data => {
                this.answers.push(...data.results);
                this.loadingAnswer = false;
                if (data.next) {
                    this.next = data.next;
                } else {
                    this.next = false;
                }
            });
        },
        Onsubmit() {
            console.log("newansbody", this.newAnswerBody);
            if (this.newAnswerBody) {
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint, "POST", { body: this.newAnswerBody }).then(
                    data => {
                        this.answers.unshift(data);
                    }
                );
                (this.newAnswerBody = null),
                    (this.userHasAnswered = true),
                    (this.showForm = false);
                if (this.error) {
                    this.error = null;
                }
            } else {
                this.error = "you can't send empty answer!";
            }
        },
        async deleteAnswer(answer) {
            let endpoint = `/api/answers/${answer.id}/`;
            try{
                await apiService(endpoint,"DELETE");
                this.answers.splice(this.answers.indexOf(answer), 1);
                this.userHasAnswered = false;  
            }
            catch(err){
                console.log(err)
            }
        },
    },
    created() {
        this.getQuestionData();
        this.getQuestionAnswer();
        this.setRequestUser();
    }
};
</script>

<style scoped>
#notfound{
        color: red;
        text-align: center;
    }
.error {
    color: red;
}
</style>