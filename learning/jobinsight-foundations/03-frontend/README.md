## 原生前端与 FastAPI 联调

已完成：
- HTML：表格、表单、输入框和按钮
- CSS：选择器、盒模型、Flex 布局和悬停样式
- JavaScript：变量、对象、数组、循环、条件和函数
- DOM：读取输入、监听点击、动态生成表格
- fetch 与 async/await：调用 FastAPI 接口
- GET：加载数据库中的候选人
- POST：新增候选人并刷新列表
- DELETE：删除候选人并刷新列表
- 区分保存失败与保存成功后的列表刷新失败
- 验证新增和删除结果在刷新页面后仍然有效

运行方式：
- 后端：在 02-fastapi 中运行
  `python -m uvicorn candidate_app.main:app --reload`
- 前端：在 03-frontend/01-html 中运行
  `python3 -m http.server 5500 --bind 127.0.0.1`
- 浏览器访问：http://127.0.0.1:5500

## 当前实践进度

- [x] 使用 HTML、CSS、JavaScript 编写候选人管理页面
- [x] 原生 JavaScript 调用 FastAPI，实现候选人查询、新增和删除
- [x] 创建 Vue 3 项目，练习响应式数据、表单绑定、列表渲染和事件处理
- [x] Vue 页面调用 FastAPI，实现候选人查询、新增和删除
- [x] Vue 页面调用 AI 学习建议接口并展示结果

以上为已实现并手动测试的功能，课程知识点和练习仍需继续验收。

## 目录

- `01-html/`：原生 HTML、CSS、JavaScript 实践
- `02-vue/`：Vue 3 候选人管理与 AI 学习建议页面

## 启动 Vue 项目

在仓库根目录执行：

```bash
cd learning/jobinsight-foundations/03-frontend/02-vue
npm install
npm run dev
```

浏览器打开终端显示的地址。接口功能需要同时启动 FastAPI 后端。

## 数据保存说明

候选人数据由 FastAPI 保存到数据库。
AI 学习建议目前仅在页面中展示，没有写入数据库。
