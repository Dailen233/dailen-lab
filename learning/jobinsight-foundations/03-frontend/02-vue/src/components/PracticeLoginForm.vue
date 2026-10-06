<script setup>
import { ref } from "vue";

const props = defineProps({
  loading: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(["submit-login"]);

const username = ref("learner");
const password = ref("");

function submitLogin() {
  if (props.loading) return;

  emit("submit-login", {
    username: username.value.trim(),
    password: password.value,
  });
}
</script>

<template>
  <form @submit.prevent="submitLogin">
    <fieldset :disabled="props.loading">
      <legend>练习账号登录</legend>

      <label>
        用户名
        <input
          v-model="username"
          autocomplete="username"
          required
        />
      </label>

      <label>
        密码
        <input
          v-model="password"
          type="password"
          autocomplete="current-password"
          required
        />
      </label>

      <button type="submit">
        {{ props.loading ? "登录中…" : "登录" }}
      </button>
    </fieldset>
  </form>
</template>

<style scoped>
fieldset {
  padding: 16px;
  border: 1px solid #ccc;
}

label {
  display: block;
  margin-bottom: 12px;
}

input {
  margin-left: 8px;
  padding: 6px;
}
</style>
