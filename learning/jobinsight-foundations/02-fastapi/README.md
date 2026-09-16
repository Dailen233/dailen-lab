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

激活虚拟环境：

```bash
source .venv/bin/activate
```

运行第一个接口：

```bash
fastapi dev 01_hello_api.py
```

### 02_parameters.py

- 路径参数 `candidate_id`
- 查询参数 `skill`、`target_job`、`limit`
- 多条件候选人筛选
- 使用 `Query` 校验参数范围
- 使用 `HTTPException` 返回 404
- 理解 200、404 和 422 状态码

运行参数练习：

```bash
fastapi dev 02_parameters.py
```

接口文档：

http://127.0.0.1:8000/docs

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

### 07：SQLite 数据库基础

- 创建磁盘数据库和候选人表。
- 使用参数绑定完成插入、查询、更新和删除。
- 理解 fetchone() 与 fetchall() 的返回值。
- 验证数据在程序结束后仍然保留。
- 使用 commit() 提交修改、rollback() 撤销未提交的修改。

运行：`python 07_sqlite_basics.py`

数据库文件 candidates_learning.db 由脚本自动创建，不纳入版本控制。

### 08：SQLAlchemy ORM 基础

- 将已有 candidates 表映射为 Candidate 类。
- 使用 Session、select、where 和 get 查询数据。
- 修改对象属性并提交，通过新会话验证保存结果。
- 理解 flush、commit 与 rollback 的区别。

运行：`python 08_sqlalchemy_basics.py`

### 09：候选人数据库 CRUD API

使用 FastAPI、Pydantic、SQLAlchemy 和 SQLite 实现候选人管理。

| 方法    |            路径            |      功能     |
|--------|----------------------------|--------------|
| GET    | /candidates                | 查询候选人列表  |
| GET    | /candidates/{candidate_id} | 查询单个候选人  |
| POST   | /candidates                | 新增候选人     |
| PUT    | /candidates/{candidate_id} | 更新候选人     |
| DELETE | /candidates/{candidate_id} | 删除候选人     |

首次运行且数据库不存在时，先初始化：

```bash
python 07_sqlite_basics.py
```

启动接口服务：

```bash
fastapi dev 09_candidate_db_api.py
```

接口文档：http://127.0.0.1:8000/docs

已通过 Apipost 验证新增、查询、更新、删除及不存在记录的错误响应。
数据库文件由本地运行生成，不纳入版本控制。

### 10：响应模型

- 区分请求模型、ORM 模型和响应模型。
- 使用 response_model 声明单人、列表和删除响应结构。
- 验证额外返回字段会被过滤。
- 在 /docs 中查看响应模型。
- 理解请求校验失败与响应校验失败的区别。

运行：`fastapi dev 10_response_model.py`

使用第 07 节创建的 candidates_learning.db。

### 11：依赖注入与数据库会话

- 使用 get_session() 统一管理 Session 的创建和关闭。
- 使用 yield 提供会话，并在依赖清理时释放资源。
- 使用 Annotated 和 Depends 声明 SessionDep。
- 五个 CRUD 接口通过参数接收会话。
- 写入操作仍由接口显式提交事务。
- 已验证新增、更新、查询、删除及删除后的查询。

运行：`fastapi dev 11_dependencies.py`
