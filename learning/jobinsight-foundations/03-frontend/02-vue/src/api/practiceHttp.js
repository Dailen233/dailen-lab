const API_BASE = import.meta.env.VITE_API_BASE_URL;

export async function requestJson(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, options);

  const data = await response.json();

  if (!response.ok) {
    const message =
      typeof data.detail === "string"
        ? data.detail
        : `请求失败，状态码：${response.status}`;

    throw new Error(message);
  }

  return data;
}
