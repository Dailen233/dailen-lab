<script setup>
import { ref, onMounted } from "vue";

const API_URL = "http://127.0.0.1:8000/candidates";

const candidateName = ref("");
const targetJob = ref("");
const candidates = ref([]);
const total = ref(0);
const message = ref("");
const isSaving = ref(false);
const deletingId = ref(null);
const aiTargetJob = ref("");
const aiAdvice = ref("");
const aiMessage = ref("");
const isGenerating = ref(false);

function clearForm() {
    candidateName.value = "";
    targetJob.value = "";
}

// 查询数据库，更新响应式数据
async function loadCandidates() {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error("加载失败，状态码：" + response.status);
    }

    const result = await response.json();

    candidates.value = result.data;
    total.value = result.total;
}

// 新增候选人
async function addCandidate() {
    if (isSaving.value || deletingId.value !== null) {
        return;
    }

    const name = candidateName.value.trim();
    const job = targetJob.value.trim();

    if (name === "" || job === "") {
        message.value = "请填写姓名和目标岗位。";
        return;
    }

    isSaving.value = true;
    message.value = "正在保存……";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                target_job: job
            })
        });

        if (!response.ok) {
            throw new Error("新增失败，状态码：" + response.status);
        }

        const savedCandidate = await response.json();

        clearForm();
        message.value = "已保存到数据库：" + savedCandidate.name;

        try {
            await loadCandidates();
        } catch (error) {
            message.value =
                "已保存，但列表刷新失败，请刷新页面查看。";
            console.error(error);
        }
    } catch (error) {
        message.value = error.message;
        console.error(error);
    } finally {
        isSaving.value = false;
    }
}

async function deleteCandidate(candidateId) {
    if (isSaving.value || deletingId.value !== null) {
        return;
    }

    deletingId.value = candidateId;
    message.value = "正在删除……";

    try {
        const response = await fetch(
            API_URL + "/" + candidateId,
            {
                method: "DELETE"
            }
        );

        if (!response.ok) {
            throw new Error(
                "删除失败，状态码：" + response.status
            );
        }

        const result = await response.json();

        message.value =
            "已从数据库删除：" + result.data.name;

        try {
            await loadCandidates();
        } catch (error) {
            message.value =
                "已删除，但列表刷新失败，请刷新页面查看。";
            console.error(error);
        }
    } catch (error) {
        message.value = error.message;
        console.error(error);
    } finally {
        deletingId.value = null;
    }
}

async function generateAdvice() {
    if (isGenerating.value) {
        return;
    }

    const job = aiTargetJob.value.trim();

    if (job === "") {
        aiMessage.value = "请先填写目标岗位。";
        return;
    }

    isGenerating.value = true;
    aiAdvice.value = "";
    aiMessage.value = "正在生成建议，请稍候……";

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/ai/study-advice",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    target_job: job
                })
            }
        );

        const result = await response.json();

        if (!response.ok) {
            const detail =
                typeof result.detail === "string"
                    ? result.detail
                    : "请求失败，状态码：" + response.status;

            throw new Error(detail);
        }

        aiAdvice.value = result.advice;
        aiMessage.value = "已生成：" + result.target_job;
    } catch (error) {
        aiMessage.value = error.message;
    } finally {
        isGenerating.value = false;
    }
}

// 组件挂载后，首次加载列表
onMounted(async function () {
    try {
        await loadCandidates();
    } catch (error) {
        message.value = error.message;
        console.error(error);
    }
});

</script>



<template>
    <main class="page">
        <h1>JobInsight 候选人管理</h1>
        <h2>候选人预览</h2>

        <div class="form-row">
            <label for="candidate-name">姓名：</label>
            <input
                id="candidate-name"
                v-model="candidateName"
                type="text"
            >
        </div>

        <div class="form-row">
            <label for="candidate-job">目标岗位：</label>
            <input
                id="candidate-job"
                v-model="targetJob"
                type="text"
            >
        </div>

        <p>姓名：{{ candidateName }}</p>
        <p>目标岗位：{{ targetJob }}</p>

        <button type="button" @click="clearForm">
            清空输入
        </button>

        <button 
            type="button" 
            :disabled="isSaving || deletingId !== null"
            @click="addCandidate"
        >
            {{ isSaving ? "正在保存……" : "新增候选人" }}
        </button>

        <p>{{ message }}</p>

        <h2>候选人列表</h2>
        <p>
            数据库共 {{ total }} 人，
            本次显示 {{ candidates.length }} 人
        </p>

        <table>
            <thead>
                <tr>
                    <th>编号</th>
                    <th>姓名</th>
                    <th>目标岗位</th>
                    <th>操作</th>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="candidate in candidates"
                    :key="candidate.id"
                >
                    <td>{{ candidate.id }}</td>
                    <td>{{ candidate.name }}</td>
                    <td>{{ candidate.target_job }}</td>
                    <td>
                        <button
                            type="button"
                            :disabled="isSaving || deletingId !== null"
                            @click="deleteCandidate(candidate.id)"
                        >
                            {{
                                deletingId === candidate.id
                                    ? "正在删除……"
                                    : "删除"
                            }}
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>

        <section>
            <h2>AI 学习建议</h2>

            <div class="form-row">
                <label for="ai-job">目标岗位：</label>
                <input
                    id="ai-job"
                    v-model="aiTargetJob"
                    type="text"
                    maxlength="50"
                    :disabled="isGenerating"
                >
            </div>

            <button
                type="button"
                :disabled="isGenerating"
                @click="generateAdvice"
            >
                {{ isGenerating ? "正在生成……" : "生成学习建议" }}
            </button>

            <p>{{ aiMessage }}</p>
            <p class="ai-advice">{{ aiAdvice }}</p>
        </section>
    </main>
</template>



<style scoped>
.page {
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    font-family: sans-serif;
    color: #333;
}

.form-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}

label {
    width: 80px;
    flex-shrink: 0;
}

input {
    padding: 8px 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 20px;
    background-color: #2563eb;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 16px;
}

th,
td {
    border: 1px solid #ccc;
    padding: 10px 16px;
    text-align: left;
}

th {
    background-color: #e8eef8;
}

.ai-advice {
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    line-height: 1.8;
}
</style>
