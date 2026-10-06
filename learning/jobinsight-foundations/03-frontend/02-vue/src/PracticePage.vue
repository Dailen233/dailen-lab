<script setup>
import ReactivityPractice from "./components/ReactivityPractice.vue";
import AuthRequestPractice from "./components/AuthRequestPractice.vue";
import { RouterLink } from "vue-router";
</script>

<template>
  <main class="practice-page">
    <h1>综合练习</h1>
    <p>练习响应式筛选、组件通信和后端认证。</p>
    <p>
    <RouterLink
        :to="{
        name: 'practice-candidate',
        params: { id: '1' },
        query: { from: 'practice' },
        }"
    >
        打开候选人 1 的路由练习
    </RouterLink>
    </p>

    <ReactivityPractice />
    <AuthRequestPractice />
  </main>
</template>

<style scoped>
.practice-page {
  max-width: 900px;
  margin: 24px auto;
  padding: 0 20px;
}
</style>
