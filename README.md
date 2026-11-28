# Antigravity Hotfix — AGY 紧急救援与全技巧实战手册

> 在线阅读：<https://beyondcy1013.github.io/antigravity-hotfix/>
>
> **救火 · 排障 · 高效实战**：系统整理 Google Antigravity（**CLI `agy`**、**Antigravity IDE**、**Antigravity 2.0 桌面端**、**Python SDK**）的急救技巧、防踩坑策略、自定义扩展（Rules / Skills / Plugins / Hooks / MCP）与自动化工作流。

---

## 问题索引（按症状直达）

### 登录与账号

- 登录时要求**扫码验证** → [一步扫码方法](docs/08-account-rescue-and-qr-downgrade.md#二需要扫码一个使用方法手机-youtube-扫码)
- 扫码后**短信发不出去 / 发了没反应** → [用 qr-sms-helper 降级短信](docs/08-account-rescue-and-qr-downgrade.md#1-扫码后要发短信但发送不成功-google-qr-sms-helper)
- 验证成功却**反复 verify → sign in again** → [年龄验证](docs/08-account-rescue-and-qr-downgrade.md#2-验证成功却反复-verify-年龄验证)
- 浏览器登录成功但**不跳转反重力 / 一直转圈** → [登录不跳转处理](docs/08-account-rescue-and-qr-downgrade.md#1-在浏览器成功登录账号但不跳转反重力)
- 提示 **count ineligible（账号不符合资格）** → [修改账号地区](docs/08-account-rescue-and-qr-downgrade.md#2-count-ineligible账号不符合资格)
- 提示**无法验证此设备**，或频繁触发设备验证 → [设备锁解救](docs/08-account-rescue-and-qr-downgrade.md#四无法验证此设备与设备锁解救)
- 报错 **EOF / invalid_grant / context deadline exceeded** → [按错误码处理](docs/08-account-rescue-and-qr-downgrade.md#3-unexpected-issuepost-错误带-daily-cloudcode-字样)
- **RT 失效 / 频繁掉登录 / 强制扫码** → [RT 与扫码救火](docs/08-account-rescue-and-qr-downgrade.md#一rt-失效与强制扫码验证qr-code救火)
- **Gemini 提示地区不可用 / 发生错误** → [地区与 Gemini 排查](docs/08-account-rescue-and-qr-downgrade.md#4-gemini-提示发生错误-你所在的国家和地区不可用)
- 账号被**停用，需要申诉** → [申诉流程](docs/09-account-security-sop-and-appeal.md#四服务停用与封号申诉appeal指南)
- 新号**养号 / 安全改密顺序** → [养号 SOP](docs/09-account-security-sop-and-appeal.md#一登录前准备与前两周养号-sop)

### 使用与扩展

- 不知道选 **CLI / IDE / 桌面端 / SDK** → [01. 四大终端形态](docs/01-surfaces-and-shortcuts.md)
- 想用**斜杠命令、子智能体、定时任务** → [02. 斜杠命令与自动化](docs/02-slash-commands-and-workflows.md)
- **规则文件**怎么写、上下文总超预算 → [03. Rules 与上下文预算](docs/03-rules-and-context-budget.md)
- **技能 / 插件**怎么装、怎么共享 → [04. Skills 与 Plugins](docs/04-skills-and-plugins.md)
- 想用 **Hooks** 做拦截、改写、自动 lint → [05. Hooks](docs/05-hooks-and-automation.md)
- 要接 **MCP**、配置权限与沙箱 → [06. MCP 与安全](docs/06-mcp-and-security.md)
- 用 **Python SDK** 做流式监听与工程化 → [07. Python SDK](docs/07-python-sdk-and-best-practices.md)

---

## 目录导航

### 账号救援（优先）

| 文档 | 内容概要 |
| :--- | :--- |
| [08. 谷歌账号救火：扫码验证、RT 失效与登录问题汇编](docs/08-account-rescue-and-qr-downgrade.md) | 统一扫码方法（手机 YouTube 相机扫码）、扫码类问题修复（短信发不出用 `google-qr-sms-helper`、反复 verify 走年龄验证）、冷门节点/iPad Mini 思路、RT 失效与设备锁救援，附登录问题原文 |
| [09. 新号养号 SOP 与封号申诉指南](docs/09-account-security-sop-and-appeal.md) | IP 自检、Chrome 多开隔离、安全设置 6 步严格顺序、Antigravity 停用表单与英文申诉技巧 |

### 使用说明与扩展

| 文档 | 内容概要 |
| :--- | :--- |
| [01. 四大终端形态与核心交互技巧](docs/01-surfaces-and-shortcuts.md) | CLI (`agy`)、IDE、Antigravity 2.0、Python SDK 定位差异；Tab 智能补全/跳转、内联指令、`@` 上下文引用与媒体上传 |
| [02. 斜杠命令、多智能体与自动化调度](docs/02-slash-commands-and-workflows.md) | `/plan`、`/goal`、`/grill-me`、`/compact`、`/schedule`、`/swarm`、`/boost` 等内置斜杠命令与 Subagent / Workflow 编排 |
| [03. 规则系统（Rules）与上下文预算管理](docs/03-rules-and-context-budget.md) | `GEMINI.md` / `AGENTS.md` 层级发现、去重机制、单文件 24 KB 上限与 20,000 Token 预算控制技巧 |
| [04. 技能（Skills）、插件（Plugins）与 JSON 配置](docs/04-skills-and-plugins.md) | 渐进式披露（Progressive Disclosure）、`SKILL.md` 编写规范、Plugin 打包、5 级加载优先级与团队共享 |
| [05. 生命周期钩子（Hooks）深度实战](docs/05-hooks-and-automation.md) | `hooks.json` 6 大生命周期事件、工具拦截与参数改写（`overwrite`）、上下文注入及防死循环技巧 |
| [06. MCP 协议集成与安全沙箱策略](docs/06-mcp-and-security.md) | `mcp_config.json`（Stdio & Streamable HTTP）、全局/项目级权限覆盖、命令白名单与终端沙箱 |
| [07. Python SDK 与工程化最佳实践](docs/07-python-sdk-and-best-practices.md) | `google-antigravity` 异步编程、思维链/工具调用实时流监听、交互式循环与高频避坑指南 |

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
