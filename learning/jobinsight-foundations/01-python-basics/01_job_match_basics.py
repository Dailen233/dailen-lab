def calculate_match(candidate_skills, required_skills):
    candidate_set = set(candidate_skills)
    required_set = set(required_skills)

    matched = []
    missing = []

    for skill in required_skills:
        if skill in candidate_set:
            matched.append(skill)
        else:
            missing.append(skill)

    total_require = len(required_set)
    if total_require == 0:
        match_rate = 0.0
    else:
        match_rate = len(matched) / total_require * 100

    return matched, missing, match_rate


def main():
    candidate = {
        "姓名": "小明",
        "掌握的技能列表": ["Python", "Git"],
        "期望岗位": "Python 后端开发"
    }

    job = {
        "岗位名称": "Python 后端开发",
        "要求的技能列表": ["Python", "Git", "FastAPI", "MySQL"]
    }

    match_skills, miss_skills, rate = calculate_match(candidate["掌握的技能列表"], job["要求的技能列表"])

    print(f"候选人：{candidate['姓名']}")
    print(f"目标岗位：{candidate["期望岗位"]}")
    print(f"匹配技能：{'、'.join(match_skills)}")
    print(f"缺少技能：{'、'.join(miss_skills)}")
    print(f"岗位匹配率：{rate:.1f}%")   

if __name__ == "__main__":
    main()

