# Python 基础

本目录用于记录 JobInsight 项目开发所需的 Python 基础练习。

## 已完成练习

### 01 Job Match Basics

文件：`01_job_match_basics.py`

实现了一个简单的候选人与岗位技能匹配程序，包含：

- 字典与列表
- 集合运算
- 函数定义和调用
- 条件判断
- 多返回值
- f-string 格式化输出
- `main()` 程序入口

### 02 JSON Storage

文件：`02_json_storage.py`

实现了候选人数据的 JSON 存储与读取，包含：

- JSON 序列化和反序列化
- UTF-8 中文数据保存
- 文件读写
- 文件不存在和 JSON 格式错误处理
- 候选人数据循环输出

## 运行方法

```bash
python3 01_job_match_basics.py
python3 02_json_storage.py
python3 -m json.tool candidates.json

