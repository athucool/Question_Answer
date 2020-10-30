  <template>
    <div>
        <p class="text-muted">
            <strong>{{answer.author}}</strong>
            &#8901;
            {{answer.created_at}}
        </p>
        <p>{{ answer.body}}</p>
        
        <div v-if="isAnswerAuthor">
            <router-link 
            :to="{name: 'Answer-editor', params:{id: answer.id}}"
            class="btn btn-sm btn-outline-info mr-2">
            Edit
            </router-link>
            <button class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">Delete</button>
        </div>
        <div v-else>
            <button class="btn btn-sm" 
                :class="{
                'btn-danger':userLikeAnswer,
                'btn-outline-danger': !userLikeAnswer
                }" @click="ToggleLike"><strong>Like{{likeCountr}}</strong>

            </button>

        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"

export default {
    name: "AnswerComponent",
     data() {
        return {
            userLikeAnswer:this.answer.user_has_voted,
            likeCountr:this.answer.likes_count,
        }
    },   
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true
        }
    },
    computed: {
            isAnswerAuthor() 
            {
                return this.answer.author === this.requestUser;
            }
        },
    methods: {
            triggerDeleteAnswer() {
                this.$emit("delete-answer",this.answer);
            },
            ToggleLike(){
                this.userLikeAnswer === false
                ? this.LikeAns()
                : this.UnlikAns()
            },
            LikeAns(){
                this.userLikeAnswer=true
                this.likes_count+=1
                let endpoint=`/api/answers/${this.answer.id}/like/`;
                apiService(endpoint,"POST")
            },
            UnlikAns(){
                this.userLikeAnswer=false
                this.likes_count-=1
                let endpoint=`/api/answers/${this.answer.id}/like/`
                apiService(endpoint,"DELETE")
            }
        }
};
</script>

<style lang="stylus" scoped></style>