<script setup>
import { inject } from 'vue';

const currentProjectName = inject("projectName");
</script>


<template>
    <p class="project-badge">
        所属项目：{{ currentProjectName }}
    </p>
</template>


<style scoped>
.project-badge {
    color: #666666;
    font-size: 14px;
}
</style>
