from getpass import getpass

import httpx


API_URL = "http://202.204.64.234:11434/v1/chat/completions"
MODEL_NAME = "qwen3.8-27b"


def main():
    print("诊断版本 V2，正在运行：", __file__)
    
    api_key = getpass("请输入学院 API Key（输入时不会显示）：").strip()

    if not api_key:
        print("API Key 不能为空。")
        return

    question = input("请输入你的问题：").strip()

    if not question:
        print("问题不能为空。")
        return

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "你是一名编程学习助手，请用中文清楚、简洁地回答。"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }

    try:
        print("正在等待模型回答……")

        response = httpx.post(
            API_URL,
            headers={
                "Authorization": "Bearer " + api_key
            },
            json=payload,
            timeout=120.0,
            trust_env=False
        )

        print("HTTP 状态码：", response.status_code)
        print("响应类型：", response.headers.get("content-type"))

        response.raise_for_status()

        try:
            result = response.json()
        except ValueError:
            print("响应不是有效的 JSON，正文前 1500 个字符：")
            print(response.text[:1500].replace(api_key, "[已隐藏密钥]"))
            return

        print("解析后的数据类型：", type(result).__name__)

        if isinstance(result, dict):
            print("顶层字段：", list(result.keys()))

        try:
            answer = result["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as error:
            print("提取回答失败：", type(error).__name__, str(error))
            print("响应正文前 1500 个字符：")
            print(response.text[:1500].replace(api_key, "[已隐藏密钥]"))
            return

        if answer:
            print("\n模型回答：")
            print(answer)
        else:
            print("接口返回了响应，但回答内容为空。")

    except httpx.HTTPStatusError as error:
        print("接口返回错误，状态码：", error.response.status_code)

    except httpx.RequestError as error:
        print("请求未完成：", error)

    except (KeyError, IndexError, TypeError, ValueError) as error:
        import traceback

        print("实际异常类型：", type(error).__name__)
        detail = traceback.format_exc()
        print(detail.replace(api_key, "[已隐藏密钥]"))


if __name__ == "__main__":
    main()