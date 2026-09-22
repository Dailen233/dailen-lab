# 02-vue

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
## 已完成的学习与练习

- 响应式数据：ref、reactive、toRefs
- 计算与侦听：computed、watch、watchEffect
- 组件拆分与通信：props、emit
- 生命周期：onMounted、onUnmounted
- 条件渲染：v-if 与 v-show
- 跨层级数据传递：provide、inject、readonly
- Vue Router：路由配置、RouterLink、RouterView
- 验证页面切换时的组件卸载、重建与草稿重置

## 页面入口

- /candidates：候选人管理与组件练习
- /learning：学习说明

## 数据保存说明

- 草稿保存在组件内存中，目前切换离开候选人页面后会重置。
- 已写入数据库的候选人可以通过后端接口重新加载。

## 岗位统计与构建验证

- 新增 /statistics 页面，使用本地练习数组统计岗位人数。
- 使用 computed 派生统计结果，添加候选人后自动更新。
- 完成 npm run build，生成 dist 构建产物。
- 完成本地预览验证：页面切换、统计更新、路由刷新与列表加载。
- 验证修改源码后，需要重新构建才能更新预览内容。

## 前端输入与文本展示

- 在学习说明页面添加文本插值展示练习。
- 理解文本插值与 v-html 的区别：文本展示与 HTML 解析。
- 理解前端校验用于交互提示，后端仍须独立校验请求数据。
- API Key 应保留在后端，不能通过 VITE_ 环境变量放入前端。
