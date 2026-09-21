const candidates = [
    { id: 1, name: "小明", target_job: "Python 后端开发" },
    { id: 2, name: "小红", target_job: "Vue 前端开发" },
    { id: 3, name: "小刚", target_job: "AI 应用开发" },
    { id: 4, name: "小金", target_job: "Java 后端开发" }
];

const backendCandidates = [];

for (const candidate of candidates) {
    if (candidate.target_job.includes("后端")) {
        backendCandidates.push(candidate);
    }
}

console.log(backendCandidates);

// ======= filter	保留元素的条件	所有匹配元素组成的新数组========

// const filteredCandidates = candidates.filter(function (candidate) {
//     return candidate.target_job.includes("后端");
// });

// const filteredCandidates = candidates.filter((candidate) => {
//     return candidate.target_job.includes("后端");
// });

const filteredCandidates = candidates.filter(
    candidate => candidate.target_job.includes("后端")
);

console.log(filteredCandidates);


// ======== find 查找元素的条件 第一个匹配元素，或 undefined ==========
const foundCandidate = candidates.find(
    candidate => candidate.id === 2
);

console.log(foundCandidate);

const missingCandidate = candidates.find(
    candidate => candidate.id === 99
);

console.log(missingCandidate); // undefined

if (foundCandidate !== undefined) {
    console.log(foundCandidate.name);
}


// ======== map 每个元素的转换方式 转换结果组成的新数组 ==========
const candidateNames = candidates.map(
    candidate => candidate.name
);

console.log(candidateNames);

const candidateDescriptions = candidates.map(
    candidate => candidate.name + "：" + candidate.target_job
);

console.log(candidateDescriptions);

const aiCandidates = candidates.filter(
    candidate => candidate.target_job.includes("AI")
);
console.log(aiCandidates)

const jinCandidates = candidates.find(
    candidate => candidate.name === "小金"
);
console.log(jinCandidates)

const candidateJobs = candidates.map(
    candidate => candidate.target_job
);

console.log(candidateJobs)


const backendNames = candidates
    .filter(candidate => candidate.target_job.includes("后端"))
    .map(candidate => candidate.name);

console.log(backendNames); // ["小明", "小金"]
