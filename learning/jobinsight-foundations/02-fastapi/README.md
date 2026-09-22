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


### 12：多文件项目结构

将单文件 API 拆分为 candidate_app 包：

- database.py：数据库连接、ORM 基类和会话依赖。
- models.py：ORM 模型。
- schemas.py：请求与响应模型。
- routers/candidates.py：候选人 CRUD 路由。
- main.py：创建 FastAPI 应用并注册路由。

使用 APIRouter 组织接口，使用 include_router 注册到应用。
已验证多文件版本的列表查询、单人查询和不存在记录的响应。

在 02-fastapi 目录启动：

```bash
python -m uvicorn candidate_app.main:app --reload
```

使用第 07 节创建的 candidates_learning.db。

### 13：候选人筛选与分页

- 使用 target_job 按岗位模糊筛选。
- 使用 offset 和 limit 实现数据库分页。
- 总数统计与明细查询使用相同筛选条件。
- total 表示分页前的匹配总数，data 表示当前页数据。
- 验证正常分页、岗位筛选、超出范围的分页及非法 limit。

实现位置：candidate_app/routers/candidates.py

## AI 学习建议接口

已新增：

- `candidate_app/llm_service.py`：组织模型请求并提取回答
- `candidate_app/routers/ai.py`：提供 AI 学习建议接口

接口：`POST /ai/study-advice`

请求示例：

```json
{
  "target_job": "Python 后端开发"
}
```

响应包含 `target_job` 和 `advice`。

前端只提交目标岗位。后端读取环境变量中的 API Key，
组织提示词并调用学院模型接口。当前没有将学习建议写入数据库。

## 配置和启动

在本目录中激活后端虚拟环境，并安装模型调用依赖：

```bash
source .venv/bin/activate
python -m pip install httpx
```

在同一个 Bash 终端中设置密钥并启动：

```bash
read -rsp "请输入学院 API Key: " SCHOOL_LLM_API_KEY
echo
export SCHOOL_LLM_API_KEY

python -m uvicorn candidate_app.main:app --reload
```

密钥输入时不显示。新开终端后，如需启动 AI 功能，应重新设置环境变量。
前后端联调时，前端访问地址须包含在后端 CORS 允许来源中。

## 输入校验、依赖注入与事务练习

- 使用 Pydantic 去除输入字符串首尾空白，并校验长度。
- 使用 Depends 提取和复用分页参数校验逻辑。
- 使用 yield 与 finally 观察依赖资源的准备、使用和清理。
- 使用独立的内存数据库练习 flush、commit 和 rollback。
- 区分候选人提交异常与提交成功后 refresh 读取异常。
- 使用模拟 Session 验证两个异常处理分支。

验证记录：
- 空字符串、纯空格输入被拒绝，正常输入的首尾空格被去除。
- 分页默认参数和指定参数返回正常，limit=0 返回 422。
- 资源依赖在接口正常返回及抛出异常时均执行清理代码。
- 事务回滚后，已提交数据保留，当前事务未提交的数据被撤销。
- candidate_error_practice.py 的 commit、refresh 异常分支均通过。

注意：
- 模拟 Session 测试验证的是函数处理逻辑，不代表真实数据库故障测试。
- commit 成功后，即使 refresh 失败，也不能通过 rollback 撤销此前已提交的数据。
