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

待完成：
- 前端编辑候选人
- 前端筛选与分页控件
- Vue 基础及组件化实现
