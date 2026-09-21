import { createRouter, createWebHistory } from "vue-router";

import CandidatePage from "../CandidatePage.vue";
import LearningPage from "../LearningPage.vue";

const router = createRouter({
    history: createWebHistory(),

    routes: [
        {
            path: "/",
            redirect: "/candidates"
        },
        {
            path: "/candidates",
            component: CandidatePage
        },
        {
            path: "/learning",
            component: LearningPage
        }
    ]
});

export default router;
