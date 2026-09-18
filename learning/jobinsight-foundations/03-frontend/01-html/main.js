const API_URL = "http://127.0.0.1:8000/candidates";

const nameInput = document.querySelector("#candidate-name");
const jobInput = document.querySelector("#candidate-job");
const addButton = document.querySelector("#add-candidate");
const preview = document.querySelector("#candidate-preview");
const tableBody = document.querySelector("#candidate-table-body");

// 把传进来的候选人数组显示到表格中
function renderCandidates(candidates) {
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

        // 第四列：操作
        const actionCell = document.createElement("td");

        const deleteButton = document.createElement("button");
        deleteButton.type = "button";
        deleteButton.textContent = "删除";

        deleteButton.addEventListener("click", function () {
            deleteCandidate(candidate.id, deleteButton);
        });

        actionCell.appendChild(deleteButton);
        row.appendChild(actionCell);

        tableBody.appendChild(row);
    }
}
// 从后端读取候选人，再更新表格
async function loadCandidates() {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error("读取失败，状态码：" + response.status);
    }

    const result = await response.json();
    renderCandidates(result.data);
}

// 把输入框里的候选人保存到后端
async function addCandidate() {
    const name = nameInput.value.trim();
    const job = jobInput.value.trim();

    if (name === "" || job === "") {
        preview.textContent = "请填写姓名和目标岗位。";
        return;
    }

    addButton.disabled = true;
    preview.textContent = "正在保存……";

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

        nameInput.value = "";
        jobInput.value = "";

        preview.textContent =
            "已保存到数据库：" + savedCandidate.name;

        // 保存成功后，重新读取数据库中的列表
        try {
            await loadCandidates();
        } catch (error) {
            preview.textContent =
                "已保存，但列表刷新失败，请刷新页面查看。";
            console.error(error);
        }
    } catch (error) {
        preview.textContent = error.message;
        console.error(error);
    } finally {
        addButton.disabled = false;
    }
}

async function deleteCandidate(candidateId, button) {
    button.disabled = true;
    preview.textContent = "正在删除……";

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

        preview.textContent =
            "已从数据库删除：" + result.data.name;

        try {
            await loadCandidates();
        } catch (error) {
            preview.textContent =
                "已删除，但列表刷新失败，请刷新页面查看。";
            console.error(error);
        }
    } catch (error) {
        preview.textContent = error.message;
        console.error(error);
    } finally {
        button.disabled = false;
    }
}

// 页面打开时加载列表
async function initializePage() {
    try {
        await loadCandidates();
    } catch (error) {
        preview.textContent = error.message;
        console.error(error);
    }
}

addButton.addEventListener("click", addCandidate);

initializePage();

