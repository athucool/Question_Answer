<template>
    <div class="container mt-2">
        <h1 class="mb-2">Edit Your Answer</h1>
        <form @submit.prevent="onSubmit">
            <textarea
                v-model="answerBody"
                class="form-control"
                rows="3"
            ></textarea>
            <br />
            <button type="submit" class="btn btn-success">Publish Your Answer</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>
<script>
import { apiService } from '../common/api.service.js';

export default {
    name:"AnswerEdit",
    props: {
        id: {
            type: String,
            required: true
        },
        previousAnswer: {
            type: String,
            required: true
        },
        questionSlug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            answerBody:this.previousAnswer,
            error:null
        }
    },
    methods: { 
        onSubmit()
        {
            console.log("this.answerbody",this.answerBody)
            if(this.answerBody)
            {
                console.log("this.answerbody",this.answerBody)
                let endpoint =`/api/answers/${this.id}/`;
                apiService(endpoint,"PUT", {body: this.answerBody })
                .then(()=> {
                    this.$router.push({
                        name:"question",
                        params: {slug: this.questionSlug}
                    })
                })
            }else{
              this.error ="You can't submit an empty answer"
            }
        }  
    },
    async beforeRouteEnter(to,form,next)
    {
        let endpoint = `/api/answers/${to.params.id}/`;
        let data = await apiService(endpoint);
        console.log("data",data)
        console.log("data.body",data.question_slug)

        to.params.previousAnswer = data.body;
        to.params.questionSlug=data.question_slug;
        console.log("to.params",to.params)
        return next();
    }
}
</script>