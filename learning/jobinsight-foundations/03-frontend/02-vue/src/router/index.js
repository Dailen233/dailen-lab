import { createRouter, createWebHistory } from "vue-router";

import CandidatePage from "../CandidatePage.vue";
import LearningPage from "../LearningPage.vue";
import StatisticsPage from "../StatisticsPage.vue";
import PracticePage from "../PracticePage.vue";
import CandidateRoutePractice from "../CandidateRoutePractice.vue";

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
        },
        {
            path: "/statistics",
            component: StatisticsPage
        },
        {
            path: "/practice",
            component: PracticePage
        },
        {
            path: "/practice/candidates/:id",
            name: "practice-candidate",
            component: CandidateRoutePractice
        }
    ]
});

export default router;
