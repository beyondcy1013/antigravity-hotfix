# Antigravity Hotfix — AGY 紧急救援与全技巧实战手册

> 在线阅读：<https://beyondcy1013.github.io/antigravity-hotfix/>
>
> **救火 · 排障 · 高效实战**：系统整理 Google Antigravity（**CLI `agy`**、**Antigravity IDE**、**Antigravity 2.0 桌面端**、**Python SDK**）的急救技巧、防踩坑策略、自定义扩展（Rules / Skills / Plugins / Hooks / MCP）与自动化工作流。

---

## 目录导航

| 文档 | 内容概要 |
| :--- | :--- |
| [01. 四大终端形态与核心交互技巧](docs/01-surfaces-and-shortcuts.md) | CLI (`agy`)、IDE、Antigravity 2.0、Python SDK 定位差异；Tab 智能补全/跳转、内联指令、`@` 上下文引用与媒体上传 |
| [02. 斜杠命令、多智能体与自动化调度](docs/02-slash-commands-and-workflows.md) | `/plan`、`/goal`、`/grill-me`、`/compact`、`/schedule`、`/swarm`、`/boost` 等内置斜杠命令与 Subagent / Workflow 编排 |
| [03. 规则系统（Rules）与上下文预算管理](docs/03-rules-and-context-budget.md) | `GEMINI.md` / `AGENTS.md` 层级发现、去重机制、单文件 24 KB 上限与 20,000 Token 预算控制技巧 |
| [04. 技能（Skills）、插件（Plugins）与 JSON 配置](docs/04-skills-and-plugins.md) | 渐进式披露（Progressive Disclosure）、`SKILL.md` 编写规范、Plugin 打包、5 级加载优先级与团队共享 |
| [05. 生命周期钩子（Hooks）深度实战](docs/05-hooks-and-automation.md) | `hooks.json` 6 大生命周期事件、工具拦截与参数改写（`overwrite`）、上下文注入及防死循环技巧 |
| [06. MCP 协议集成与安全沙箱策略](docs/06-mcp-and-security.md) | `mcp_config.json`（Stdio & Streamable HTTP）、全局/项目级权限覆盖、命令白名单与终端沙箱 |
| [07. Python SDK 与工程化最佳实践](docs/07-python-sdk-and-best-practices.md) | `google-antigravity` 异步编程、思维链/工具调用实时流监听、交互式循环与高频避坑指南 |
| [08. 谷歌账号救火：扫码验证、RT 失效与登录问题汇编](docs/08-account-rescue-and-qr-downgrade.md) | 统一扫码方法（手机 YouTube 相机扫码）、扫码类问题修复（短信发不出用 `google-qr-sms-helper`、反复 verify 走年龄验证）、冷门节点/iPad Mini 思路、RT 失效与设备锁救援，附登录问题原文 |
| [09. 新号养号 SOP 与封号申诉指南](docs/09-account-security-sop-and-appeal.md) | IP 自检、Chrome 多开隔离、安全设置 6 步严格顺序、Antigravity 停用表单与英文申诉技巧 |

---

## 快速概览：Antigravity 4 大核心提效法则

1. **按场景选对交互入口**
   - 局部微调 / 加注释：IDE 中使用 **`Ctrl+I` / `Cmd+I`**（仅修改选中代码块）。
   - 连续编码预测：善用 **Antigravity Tab**（`Tab` 接受、`Esc` 取消、`Ctrl/Cmd + →` 按词接受、Tab to Jump / Tab to Import）。
   - 复杂多步工程：使用 **Agent Mode** 配合 `/plan`、`/grill-me` 先对齐方案再执行。
   - 轻量终端 / 批处理：使用 `agy` CLI。
2. **用“渐进式披露”省下 80% 上下文**
   - 把通用项目规范放进 `AGENTS.md` / `GEMINI.md`（常驻但受 20,000 Token 总预算限制）。
   - 把特定工作流放进 `SKILL.md`（仅注入 `name` 与 `description`，触发时才加载正文），大块参考资料放进 `references/`，复杂命令封装进 `scripts/`。
3. **用斜杠命令驱动高阶模式**
   - 复杂重构先 `/grill-me` 或 `/plan`，长对话及时 `/compact`，长时间无人值守用 `/goal`，定时巡检用 `/schedule`。
4. **用 Hooks + 权限策略兜底安全**
   - 通过 `.agents/hooks.json` 的 `PreToolUse` / `PostToolUse` / `Stop` 在工具执行前审计/改写参数、在工具执行后自动 lint、在任务未达标时阻止退出。

---

## 官方文档索引（支持 `.md` 直读）

所有 Antigravity 官方文档页面均支持在 URL 末尾追加 `.md` 直接获取精简 Markdown 原文：

- 全站文档索引：`https://antigravity.google/llms.txt`
- 快速开始：`https://antigravity.google/docs/getting-started.md`
- CLI 参考与最佳实践：`https://antigravity.google/docs/cli/reference.md`、`https://antigravity.google/docs/cli/best-practices.md`
- 自定义系统：`https://antigravity.google/docs/skills.md`、`https://antigravity.google/docs/rules.md`、`https://antigravity.google/docs/hooks.md`、`https://antigravity.google/docs/plugins.md`、`https://antigravity.google/docs/mcp.md`
- 更新日志：`https://antigravity.google/docs/changelog.md`
