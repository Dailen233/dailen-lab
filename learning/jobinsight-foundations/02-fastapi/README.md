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

### 04_crud.py

- 使用 GET 查询候选人
- 使用 POST 新增候选人
- 使用 PUT 完整更新候选人
- 使用 DELETE 删除候选人
- 使用辅助函数查找候选人的列表位置
- 使用 HTTPException 处理资源不存在
- 理解内存数据在服务器重启后会丢失

### 05：类型提示与函数练习

- 理解类型提示与运行时校验的区别。
- 理解默认参数、None 和空字符串的区别。
- 使用容器类型提示和联合类型。
- 实现按岗位筛选姓名、按姓名查找下标。
- 理解 return、enumerate 和 None 判断。

运行：`python3 05_type_hints.py`

### 06：Pydantic 数据校验

- 使用 BaseModel 定义候选人数据模型。
- 理解类型解析与字段约束的区别。
- 验证年龄范围、非法整数输入和空技能列表。
- 使用 try/except 捕获 ValidationError。
- 使用 model_dump() 将模型转换为字典。

运行：`python 06_pydantic_validation.py`

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

