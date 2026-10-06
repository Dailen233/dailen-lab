<script setup>
import { RouterLink, RouterView } from "vue-router";
import {
  currentUser,
  clearSession,
} from "./stores/practiceAuth.js";
</script>

<template>
    <nav class="navigation">
        <RouterLink to="/candidates">候选人管理</RouterLink>
        <RouterLink to="/learning">学习说明</RouterLink>
        <RouterLink to="/statistics">岗位统计</RouterLink>
        <RouterLink to="/practice">综合练习</RouterLink>
    </nav>


    <div class="session-bar">
        <template v-if="currentUser">
            <span>
            当前用户：{{ currentUser.name }}
            （{{ currentUser.username }}）
            </span>

            <button type="button" @click="clearSession">
            退出登录
            </button>
        </template>

        <span v-else>当前未登录</span>
    </div>
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
