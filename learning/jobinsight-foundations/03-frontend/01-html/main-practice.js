console.log("JobInsight 页面已加载");

const candidateName = "小金";
let targetJob = "C++";
console.log(candidateName);
console.log(targetJob);
targetJob = "Python 后端开发";
console.log(targetJob);

let candidateCount = 4;
const isLoading = false;

console.log(candidateCount);
console.log(isLoading);

console.log(typeof candidateName);
console.log(typeof candidateCount);
console.log(typeof isLoading);

candidateCount = candidateCount + 1;
console.log(candidateCount);

console.log(4 + 1);
console.log("4" + 1);

const newCandidate = {
    id: 5,
    name: "小李",
    target_job: "Vue 前端开发",
};

console.log(newCandidate.name)
newCandidate.target_job = "AI 应用开发"
console.log(newCandidate.target_job)


const candidates = [
    {
        id: 1,
        name: "小明",
        target_job: "Python 后端开发"
    },
    {
        id: 2,
        name: "小红",
        target_job: "Vue 前端开发"
    },
    {
        id: 3,
        name: "小刚",
        target_job: "AI 应用开发"
    }
];

console.log(candidates[2].name);
console.log(candidates.length);

for (const candidate of candidates) {
    console.log(candidate.name, candidate.target_job);
}

for (const candidate of candidates) {
    if (candidate.target_job === "AI 应用开发") {
        console.log(candidate.name);
    }
}

function getCandidateText(person) {
    return person.name + ":" + person.target_job;
}

for (const candidate of candidates) {
    const text = getCandidateText(candidate);
    console.log(text);
}

const nameInput = document.querySelector("#candidate-name");
const jobInput = document.querySelector("#candidate-job");
const addButton = document.querySelector("#add-candidate");
const preview = document.querySelector("#candidate-preview");
const tableBody = document.querySelector("#candidate-table-body");

// 当前练习数组中的编号是 1、2、3，下一名从 4 开始
let nextCandidateId = 4;

function renderCandidates() {
    tableBody.replaceChildren();

    for (const candidate of candidates) {
        const row = document.createElement("tr");

        const values = [
            candidate.id,
            candidate.name,
            candidate.target_job
        ];

        for (const value of values) {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        }

        tableBody.appendChild(row);
    }
}

function addCandidate() {
    const name = nameInput.value.trim();
    const job = jobInput.value.trim();

    if (name === "" || job === "") {
        preview.textContent = "请填写姓名和目标岗位。";
        return;
    }

    candidates.push({
        id: nextCandidateId,
        name: name,
        target_job: job
    });

    nextCandidateId = nextCandidateId + 1;

    renderCandidates();

    preview.textContent = "已添加到当前页面：" + name;
    nameInput.value = "";
    jobInput.value = "";
}

addButton.addEventListener("click", addCandidate);

renderCandidates();

async function checkCandidateApi() {
    try {
        const response = await fetch(
            "http://127.0.0.1:8000/candidates"
        );

        if (!response.ok) {
            throw new Error("请求失败，状态码：" + response.status);
        }

        const result = await response.json();

        console.log("后端返回的数据：", result);
        console.log("候选人总数：", result.total);
        console.log("候选人列表：", result.data);
    } catch(error) {
        console.error("读取候选人失败：", error);
    }
}

checkCandidateApi();

