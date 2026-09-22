<script setup>
import { ref, computed } from 'vue';

const candidates = ref([
    { id: 1, name: "小明", target_job: "Python 后端开发" },
    { id: 2, name: "小红", target_job: "Vue 前端开发" },
    { id: 3, name: "小刚", target_job: "AI 应用开发" },
    { id: 4, name: "小金", target_job: "Java 后端开发" }
]);

let nextCandidateId = 5;

// 在这里添加计算属性和按钮处理函数
const totalCount = computed(() => {
    return candidates.value.length;
});

const backendCount = computed(() => {
    return candidates.value.filter(item => 
    item.target_job.includes("后端")).length;
});

const frontendCount = computed(() => {
    return candidates.value.filter(item => 
    item.target_job.includes("前端")).length;
});

const aiCount = computed(() => {
    return candidates.value.filter(item => 
    item.target_job.includes("AI")).length;
});

function addBackendCandidate() {
    const name = "新增候选人" + nextCandidateId;
    const job = "Python 后端开发";
    candidates.value.push({
        id: nextCandidateId, 
        name: name,
        target_job: job
    });
    nextCandidateId += 1;
}
</script>


<template>
    <section class="statistics-page">
        <h1>岗位统计</h1>

        <!-- 在这里显示统计结果并添加按钮 -->
        <p>候选人总数： {{ totalCount }}</p>
        <p>后端岗位人数： {{ backendCount }}</p>
        <p>前端岗位人数： {{ frontendCount }}</p>
        <p>AI 岗位人数： {{ aiCount }}</p>

        <button type="button" @click="addBackendCandidate">
            添加一名后端候选人
        </button>
    </section>
</template>


<style scoped>
.statistics-page {
    max-width: 900px;
    margin: 32px auto;
    padding: 0 20px;
}
</style>