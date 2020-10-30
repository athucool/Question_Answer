<template>
    <div class="container mt-3">
        <h1 class="mb-2">Ask Question</h1>
        <form @submit.prevent="OnSubmit">
            <textarea
                v-model="question_body"
                class="form-control"
                placeholder="what do u want to ask?"
                rows="3"
            ></textarea>
            <br />
            <button type="submit" class="btn btn-success">Publish</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
    import { apiService } from '../common/api.service';

export default {
    name:"QuestionEditor",
    props: {
        slug: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            question_body: null,
            error: null
        }
    },
    methods: {
        OnSubmit() 
        {
            if (!this.question_body)
            {
                this.error = " You can't send an empty question!"
            }else if (this.question_body.length > 240)
            {
                this.error ="Ensure that your body field is no more than 240"
            }else 
            {
                let endpoint = "/api/questions/";
                let method = "POST";
                if (this.slug !==undefined)
                {
                    endpoint += `${this.slug}/`;
                    method = "PUT";
                }
                apiService(endpoint,method,{content: this.question_body })
                .then(question_data => {
                this.$router.push({
                    name: 'question', 
                    params: { slug: question_data.slug }
                    })
                })
            } 
            
        }
    },
    async beforeRouteEnter(to,form,next)    {
        if (to.params.slug!==undefined)
            {
                let endpoint=`/api/questions/${to.params.slug }/`;
                let data=await apiService(endpoint);
                console.log(data)
                return next(vm =>(vm.question_body = data.content))
            }
        else{
            next();
        }
    },
    created(){
        document.title="Editor-Questiontime";

}

}
</script>