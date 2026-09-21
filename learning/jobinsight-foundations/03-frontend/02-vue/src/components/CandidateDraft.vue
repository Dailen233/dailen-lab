<script setup>
import { reactive, toRefs, watch, ref, onMounted, onUnmounted, watchEffect } from 'vue';
import ProjectBadge from "./ProjectBadge.vue";

const emit = defineEmits(["submit-draft"]);

const draftMessage = ref("");

const props = defineProps({
    title: {
        type: String,
        default: "候选人草稿练习",
    }
});

onMounted(() => {
    console.log(props.title + ":挂载完成");
});

onUnmounted(() => {
    console.log(props.title + ":卸载完成");
});

const candidateDraft = reactive({
    name: "",
    target_job: ""
});

watchEffect(() => {
    console.log(
        "草稿变化",
        props.title,
        candidateDraft.name,
        candidateDraft.target_job
    );
});


// 直接取出字符串，保留当时的值
const { name: nameSnapshot } = candidateDraft;

// 取出与原属性保持联系的 ref
const {
    name: draftNameRef,
    target_job: draftJobRef
} = toRefs(candidateDraft);

function fillCandidateDraft() {
    candidateDraft.name = "小李";
    candidateDraft.target_job = "Vue 前端开发";
}

function clearCandidateDraft() {
    candidateDraft.name = "";
    candidateDraft.target_job = "";
}

function fillDraftViaRefs() {
    draftNameRef.value = "小红";
    draftJobRef.value = "AI 应用开发";
}

watch(
    () => candidateDraft.target_job,
    (newJob, oldJob) => {
        console.log("原岗位：", oldJob);
        console.log("新岗位：", newJob);
    }
);

function submitDraft() {
    const name = candidateDraft.name.trim();
    const job = candidateDraft.target_job.trim();

    if (name === "" || job === "") {
        draftMessage.value = "请填写姓名和目标岗位。";
        return;
    }

    draftMessage.value = "";

    emit("submit-draft", {
        name: name,
        target_job: job
    });
}

</script>





<template>
    <section>
        <h2>{{ props.title }}</h2>
        <ProjectBadge />

        <p class="form-row">
            <label>
                姓名：
                <input v-model="candidateDraft.name" type="text">
            </label>
        </p>

        <p class="form-row">
            <label>
                目标岗位：
                <input v-model="candidateDraft.target_job" type="text">
            </label>
        </p>

        <p>
            草稿：{{ candidateDraft.name }}，
            {{ candidateDraft.target_job }}
        </p>

        <p>原对象姓名：{{ candidateDraft.name }}</p>
        <p>直接解构的姓名：{{ nameSnapshot }}</p>
        <p>通过 toRefs 取得的姓名：{{ draftNameRef }}</p>

        <button type="button" @click="fillCandidateDraft">
            填入示例
        </button>
        <button type="button" @click="clearCandidateDraft">
            清空草稿
        </button>
        <button type="button" @click="fillDraftViaRefs">
            通过 ref 修改草稿
        </button>
        <button type="button" @click="submitDraft">
            交给父组件
        </button>

        <p>{{ draftMessage }}</p>
    </section>        
</template>

<style scoped>
.form-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}

.form-row label {
    width: 80px;
    flex-shrink: 0;
}

input {
    padding: 8px 12px;
    border: 1px solid #cccccc;
    border-radius: 4px;
}

button {
    margin-right: 8px;
    padding: 8px 12px;
    cursor: pointer;
}
</style>
