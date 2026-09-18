from getpass import getpass

import httpx


API_URL = "http://202.204.64.234:11434/v1/chat/completions"
MODEL_NAME = "qwen3.8-27b"


def call_model(messages: list[dict[str, str]], api_key: str) -> str:
    """发送消息列表，返回模型回答。"""
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
        raise ValueError("接口没有返回有效的回答文字。")

    return answer.strip()


def main():
    api_key = getpass("请输入学院 API Key：").strip()

    if not api_key:
        print("API Key 不能为空。")
        return

    messages = [
        {
            "role": "system",
            "content": "你是一名编程学习助手，请用中文清楚、简洁地回答。"
        }
    ]

    print("开始对话，输入 exit 退出。")

    while True:
        question = input("\n你：").strip()

        if question.lower() == "exit":
            print("对话结束。")
            break

        if not question:
            print("问题不能为空。")
            continue

        user_message = {
            "role": "user",
            "content": question
        }

        # 本次请求：已有历史 + 当前问题
        request_messages = messages + [user_message]

        try:
            print("正在等待模型回答……")
            answer = call_model(request_messages, api_key)

        except httpx.HTTPStatusError as error:
            print("接口错误，状态码：", error.response.status_code)
            continue

        except httpx.RequestError as error:
            print("请求未完成：", error)
            continue

        except (KeyError, IndexError, TypeError, ValueError):
            print("响应格式异常，或回答为空。")
            continue

        # 成功取得回答后，保存这一轮对话
        messages.append(user_message)
        messages.append({
            "role": "assistant",
            "content": answer
        })

        print("\n模型：", answer)
        print("已完成对话轮数：", (len(messages) - 1) // 2)


if __name__ == "__main__":
    main()

    