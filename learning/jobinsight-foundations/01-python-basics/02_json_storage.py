import json

def save_candidates(file_path, candidates):
    """保存候选人列表到json文件"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)


def load_candidates(file_path):
    """读取json，文件不存在/格式错误返回空列表"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def main():
    # 候选人数据
    candidates = [
        {
            "name": "小明",
            "target_job": "Python 后端开发",
            "skills": ["Python", "Git"]
        },
        {
            "name": "小红",
            "target_job": "前端开发",
            "skills": ["HTML", "CSS", "JavaScript"]
        }
    ]

    # 1.保存文件
    save_candidates("candidates.json", candidates)
    print(f"已保存 {len(candidates)} 位候选人")

    # 2.读取文件
    data = load_candidates("candidates.json")
    print(f"成功读取 {len(data)} 位候选人")

    # 3.循环输出
    for idx, person in enumerate(data, start=1):
        name = person["name"]
        job = person["target_job"]
        skill_str = "、".join(person["skills"])
        print(f"{idx}.{name}|{job}|{skill_str}")


if __name__ == "__main__":
    main()
