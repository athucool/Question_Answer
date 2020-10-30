import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Question from "../views/Question.vue";
import QuestionEditor from "../views/Questionedit.vue";
import AnswerEdit from "../views/AnswerEditor.vue";
// import AboutUS from "../views/AboutUs.vue";
import NotFound from "../views/NotFound.vue";


const mode= 'history'
const routes = [
 
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/home",
    name: "Home2",
    component: Home
  },
  {
    path: "/ask/:slug?",
    name: "QuestionEditor",
    component: QuestionEditor,
    props:true
  },
  {
    path: "/answer/:id",
    name: "Answer-editor",
    component: AnswerEdit,
    props:true
  },
  {
    path: "/question/:slug",
    name: "question",
    component: Question,
    props: true
  },
  {
    path:'/:pathMatch(.*)*',
    name:"page-Not-found",
    component: NotFound
  }
   
];

const router = createRouter({
  mode,
  history: createWebHistory(),
  routes
});

export default router;
