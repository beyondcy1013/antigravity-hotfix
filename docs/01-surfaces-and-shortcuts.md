# 01. 四大终端形态与核心交互技巧

Google Antigravity (AGY) 并非单一工具，而是一套覆盖终端、编辑器、桌面端与编程 SDK 的完整 AI 原生开发平台。

---

## 一、四大使用形态对比

| 形态 | 适用场景 | 核心入口 / 配置路径 |
| :--- | :--- | :--- |
| **Antigravity CLI (`agy`)** | 轻量终端交互、快速问答、脚本/CI 调用 | 命令 `agy`，配置 `~/.gemini/antigravity-cli/settings.json` |
| **Antigravity IDE** | 基于 VS Code 的 AI 原生编辑器，深度代码编辑与调试 | 侧边栏 Chat、`Ctrl/Cmd+I`、Tab 补全、Code Lenses |
| **Antigravity 2.0 (App)** | 独立 Electron 桌面应用，并行管理多项目、定时任务、子智能体与辅助面板 | 左侧边栏（Projects / Scheduled Tasks / Skills / Settings）、Chat Canvas |
| **Antigravity Python SDK** | 在 Python 流水线、自动化测试或脚本中以代码编排 Agent | `pip install google-antigravity` |

### CLI (`agy`) 常用快捷操作
- 启动：`agy`
- 查看全部命令行参数与子命令：`agy --help`
- 查看 TUI 内置斜杠命令：进入 `agy` 后输入 `/help`
- 退出：`Ctrl+D Ctrl+D`，或输入 `/exit` / `/quit`

---

## 二、Antigravity IDE 三大交互模态

IDE 根据任务粒度提供三种不同强度的 AI 协作方式：

### 1. 被动预测：Antigravity Tab（自动补全）
单键触发的下一意图预测，不仅补全当前行，还能预测跨行修改与光标跳转：
- **Autocomplete & Supercomplete**：Autocomplete 在光标处补全；Supercomplete 会在浮窗中给出包含**删除与重构**的大段 Diff 建议。
- **Tab to Jump**：预测你接下来要修改的位置，按 `Tab` 直接跳转。
- **Tab to Import**：使用新依赖时自动在文件顶部补全 `import` 语句。
- **按键控制**：
  - `Tab`：全部接受
  - `Esc`：取消建议
  - `Cmd + →` (macOS) / `Ctrl + →` (Linux)：**按词（word-by-word）逐步接受**，避免一次接受过多不需要的代码。

### 2. 指令式微调：Inline Command（`Cmd+I` / `Ctrl+I`）
适合局部精准修改，避免全局对话打断心流：
- **限定范围修改**：先选中一段代码再按 `Ctrl/Cmd+I`，Agent **只会修改高亮选中的代码块**，适合重构、修 Bug 或格式转换。
- **光标处生成**：不选中任何内容直接触发，可在当前光标处生成全新代码。
- **局部文档/注释**：快速为函数补充 docstring 或行内注释的最佳入口。

### 3. 协作式工程：Sidebar Chat & Agent Mode
- **Agent Mode**：具备读写文件、执行终端命令（构建/测试）、网页搜索与调用 MCP 工具的完整自主执行能力。
- **Planning Mode**：在动手改代码前先生成分步执行计划，经用户审阅或微调后再执行。
- **编辑器 UI 联动**：
  - **Inline Code Lenses**：类或函数上方直接出现操作按钮（如 *Refactor*、*Write Tests*、*Explain Code*）。
  - **Visual Diff Overlays**：编辑器内直接以红/绿 Diff 高亮展示建议修改，支持逐块 Accept/Reject。
  - **Diagnostic Auto-Fix**：直接从行内编译错误、Lint 警告或 Problems 面板一键触发修复。

---

## 三、Antigravity 2.0 桌面端高效技巧

Antigravity 2.0 的 Chat Canvas 与左侧边栏专为多任务并行设计：

1. **`@` 上下文精准挂载**
   在输入框输入 `@` 可直接挂载以下上下文，减少 Agent 盲目搜索的 Token 消耗：
   - 文件与文件夹（Files & Folders）
   - 历史对话（Previous Conversations）
   - 终端会话（Terminal Sessions）
   - 规则文件（Rules）
   - MCP 服务器与工具（MCP Servers / Tools）
2. **媒体拖拽上传（Media Uploads）**
   直接把报错截图、UI 设计稿或文件拖入或粘贴到 Chat Canvas，即可作为当前消息的多模态上下文。
3. **辅助面板（HTML Auxiliary Pane）**
   实时监控并行中的 **Subagents（子智能体）**、**Background Tasks（后台任务）**、**Artifacts（产物文档）**、**Files Changed（文件变更）** 与 **Terminals（终端）**。
4. **Scheduled Tasks（定时与延时任务）**
   直接在左侧边栏配置周期性 Cron 任务或一次性延时提醒，无需外部 crontab。
