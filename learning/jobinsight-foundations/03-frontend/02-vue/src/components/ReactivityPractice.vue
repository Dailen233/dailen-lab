<script setup>
import { computed, ref } from "vue";

const keyword = ref("");

const candidates = ref([
    { id: 1, name: "小明", target_job: "Python 后端开发" },
    { id: 2, name: "小红", target_job: "Vue 前端开发" },
    { id: 3, name: "小王", target_job: "python 数据分析" },
]);

const filteredCandidates = computed(() => {
    const query = keyword.value.trim().toLowerCase();

    return candidates.value.filter((item) => {
        const text =
            `${item.name} ${item.target_job}`.toLowerCase();

        return text.includes(query);
    });
});

function clearSearch() {
    keyword.value = "";
}

function changeJob() {
    candidates.value[1].target_job = "Python 全栈开发";
}
</script>

<template>
    <section class="reactivity-practice">
        <h2>响应式筛选练习</h2>

        <label>
            搜索姓名或岗位：
            <input
                v-model="keyword"
                placeholder="试试 Python 或 Vue"
            />
        </label>

        <button
            type="button"
            :disabled="keyword.length === 0"
            @click="clearSearch"
        >
            清空搜索
        </button>

        <p>
            原始 {{ candidates.length }} 人，
            匹配 {{ filteredCandidates.length }} 人
        </p>

        <p v-if="filteredCandidates.length === 0">
            没有匹配的候选人
        </p>

        <ul v-else>
            <li
                v-for="item in filteredCandidates"
                :key="item.id"
            >
                {{ item.name }}｜{{ item.target_job }}
            </li>
        </ul>

        <button type="button" @click="changeJob">
            将小红岗位改为 Python 全栈开发
        </button>
    </section>
</template>

<style scoped>
.reactivity-practice {
    margin: 24px 0;
    padding: 16px;
    border: 1px solid #ccc;
    border-radius: 8px;
}

input {
    margin: 8px;
    padding: 6px;
}

button {
    margin: 8px 8px 8px 0;
}

li {
    margin: 8px 0;
}
</style>
