# 大模型 API 入门实践

使用 Python 和 httpx 调用学院提供的模型接口。

## 已完成的练习

- `01_chat_api.py`：单轮问答、HTTP 状态和响应结构检查
- `02_chat_history.py`：多轮对话，通过 messages 传递历史消息

## 运行

在本目录中激活已有虚拟环境：

```bash
source .venv/bin/activate
python -m pip install httpx

python 01_chat_api.py
# 或：
python 02_chat_history.py
```

按提示输入学院 API Key 和问题。
多轮对话中输入 exit 退出。

## 实现说明

API Key 在运行时输入，不写入代码。
多轮对话历史保存在当前进程内存中，退出后不会保留。
请求使用 trust_env=False，避免本机代理环境变量影响本次调用。

## 已排查的问题

代理 URL 使用不受支持的协议，导致请求初始化失败。
API Key 大小写输入错误，导致 HTTP 401。
修正后已完成单轮和多轮对话测试。

## 后续内容

流式输出、结构化输出和 Token 管理尚待学习。