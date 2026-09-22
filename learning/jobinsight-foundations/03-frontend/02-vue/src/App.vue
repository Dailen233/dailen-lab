<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
    <nav class="navigation">
        <RouterLink to="/candidates">候选人管理</RouterLink>
        <RouterLink to="/learning">学习说明</RouterLink>
        <RouterLink to="/statistics">岗位统计</RouterLink>
    </nav>

    <RouterView />
</template>

<style scoped>
.navigation {
    display: flex;
    gap: 20px;
    max-width: 900px;
    margin: 24px auto;
    padding: 0 20px;
}

.navigation a {
    color: #333333;
    text-decoration: none;
}

.navigation a.router-link-active {
    color: #2563eb;
    font-weight: bold;
}
</style>
