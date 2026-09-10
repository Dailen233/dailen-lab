# FastAPI 基础学习

本目录记录 JobInsight 项目的 FastAPI 后端基础练习。

## 开发环境

- Python 3.12.3
- FastAPI 0.141.1
- Pydantic 2.13.5
- Uvicorn 0.52.4
- Apipost 8.2.7

## 练习内容

### 01_hello_api.py

- 创建 FastAPI 应用
- 编写 GET 接口
- 返回 JSON 数据
- 使用 `/docs` 查看自动生成的接口文档
- 使用 Apipost 测试接口

### 02_parameters.py

- 路径参数 `candidate_id`
- 查询参数 `skill`、`target_job`、`limit`
- 多条件候选人筛选
- 使用 `Query` 校验参数范围
- 使用 `HTTPException` 返回 404
- 理解 200、404 和 422 状态码

### 03_request_body.py

- 使用 Pydantic `BaseModel` 定义请求体
- 使用 `Field` 校验字符串和列表长度
- 使用 POST 新增候选人
- 使用 `model_dump()` 转换模型数据
- 理解 201 和 422 状态码

## 运行方法

激活虚拟环境：

```bash
source .venv/bin/activate
```

运行第一个接口：

```bash
fastapi dev 01_hello_api.py
```

运行参数练习：

```bash
fastapi dev 02_parameters.py
```

接口文档：

http://127.0.0.1:8000/docs

