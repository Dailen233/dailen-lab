<script setup>
import { ref } from 'vue';

const inputText = ref("");
</script>

<template>
    <section class="learning-page">
        <h1>学习说明：构建测试</h1>

        <p>这个项目用于练习 Vue、FastAPI 和数据库联调。</p>

        <ul>
            <li>候选人管理：展示、新增和删除候选人。</li>
            <li>组件练习：响应式数据、组件通信和生命周期。</li>
            <li>AI 功能：通过后端生成学习建议。</li>
        </ul>

        <h2>文本显示练习</h2>

        <label>
            输入内容：
            <input v-model="inputText">
        </label>

        <p>显示结果：{{ inputText }}</p>
    </section>
</template>

<style scoped>
.learning-page {
    max-width: 900px;
    margin: 32px auto;
    padding: 0 20px;
}
</style>
