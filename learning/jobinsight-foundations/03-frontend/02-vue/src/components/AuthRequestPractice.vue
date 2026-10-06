<script setup>
import { ref } from "vue";
import { requestJson } from "../api/practiceHttp.js";
import PracticeLoginForm from "./PracticeLoginForm.vue";
import {
  currentUser,
  setSession,
  clearSession,
} from "../stores/practiceAuth.js";


const loading = ref(false);
const errorMessage = ref("");


async function handleLogin(credentials) {
  // 请求未结束时，不再启动另一轮请求。
  if (loading.value) return;

  loading.value = true;
  errorMessage.value = "";
  clearSession();

  try {
    // 1. 提交账号密码，获得 JWT。
    const tokenData = await requestJson("/practice/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(credentials),
    });

    // 2. 携带 JWT，获取当前用户。
    const meData = await requestJson("/practice/me", {
      headers: {
        Authorization: `Bearer ${tokenData.access_token}`,
      },
    });

    // 3. 两个请求都成功后，显示用户信息。
    setSession(meData.user, tokenData.access_token);
  } catch (error) {
    errorMessage.value =
      error instanceof Error ? error.message : "请求失败，请重试";
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <section class="auth-practice">
    <h2>前后端登录练习</h2>

    <PracticeLoginForm
      :loading="loading"
      @submit-login="handleLogin"
    />

    <p v-if="errorMessage" class="error" role="alert">
      {{ errorMessage }}
    </p>

    <div v-if="currentUser">
      <h3>认证成功</h3>
      <p>用户名：{{ currentUser.username }}</p>
      <p>姓名：{{ currentUser.name }}</p>
      <p>角色：{{ currentUser.role }}</p>
    </div>
  </section>
</template>

<style scoped>
.auth-practice {
  margin: 24px 0;
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.error {
  color: #b42318;
}
</style>
