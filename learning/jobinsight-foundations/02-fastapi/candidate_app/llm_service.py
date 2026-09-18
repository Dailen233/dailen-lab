import os

import httpx


API_URL = "http://202.204.64.234:11434/v1/chat/completions"
MODEL_NAME = "qwen3.8-27b"


def generate_study_advice(target_job: str) -> str:
    api_key = os.environ.get("SCHOOL_LLM_API_KEY", "").strip()

    if not api_key:
        raise RuntimeError("后端尚未配置模型 API Key")

    messages = [
        {
            "role": "system",
            "content": (
                "你是一名编程学习规划助手。"
                "根据用户提供的目标岗位，给出适合初学者的学习建议。"
                "使用中文，包含学习重点、一个练习任务和验收标准。"
                "尽量控制在300字以内，不输出完整代码。"
            )
        },
        {
            "role": "user",
            "content": "我的目标岗位是：" + target_job
        }
    ]

    response = httpx.post(
        API_URL,
        headers={
            "Authorization": "Bearer " + api_key
        },
        json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False
        },
        timeout=120.0,
        trust_env=False
    )

    response.raise_for_status()
    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    if not isinstance(answer, str) or not answer.strip():
        raise ValueError("模型回答为空")

    return answer.strip()
