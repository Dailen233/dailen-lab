import { ref } from "vue";

export const currentUser = ref(null);
export const accessToken = ref("");

export function setSession(user, token) {
  currentUser.value = user;
  accessToken.value = token;
}

export function clearSession() {
  currentUser.value = null;
  accessToken.value = "";
}
