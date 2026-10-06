<script setup>
import { computed } from "vue";
import { RouterLink, useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

const candidateId = computed(() => route.params.id);

const source = computed(() => {
  return typeof route.query.from === "string"
    ? route.query.from
    : "未指定";
});

function switchCandidate() {
  const nextId = candidateId.value === "1" ? "2" : "1";

  router.push({
    name: "practice-candidate",
    params: {
      id: nextId,
    },
    query: {
      from: "switch-button",
    },
  });
}
</script>

<template>
  <main class="route-practice">
    <h1>候选人路由参数练习</h1>

    <p>当前候选人 ID：{{ candidateId }}</p>
    <p>来源标记：{{ source }}</p>

    <button type="button" @click="switchCandidate">
      切换候选人 1 / 2
    </button>

    <p>
      <RouterLink to="/practice">返回综合练习</RouterLink>
    </p>
  </main>
</template>

<style scoped>
.route-practice {
  max-width: 900px;
  margin: 24px auto;
  padding: 0 20px;
}
</style>
