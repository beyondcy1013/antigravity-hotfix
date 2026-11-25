# 05. 生命周期钩子（Hooks）深度实战

`hooks.json` 允许你在 Agent 执行循环的关键节点插入外部脚本，实现**高危命令拦截、参数自动改写、工具执行后自动格式化、上下文动态注入、阻止未完成任务提前退出**等硬核能力。

放置位置：`.agents/hooks.json`（工作区）、`~/.gemini/config/hooks.json`（全局）或插件根目录 `<plugin_dir>/hooks.json`。

---

## 一、6 大生命周期事件一览

| 事件 | 触发时机 | 是否需要 `matcher` | 典型用途 |
| :--- | :--- | :--- | :--- |
| **`SessionStart`** | 新会话启动时触发一次 | 否（扁平数组） | 注入欢迎语、环境检查提示或初始化上下文 |
| **`PreToolUse`** | 工具执行**前** | 是（正则匹配工具名） | 安全门禁（`allow`/`deny`/`ask`/`force_ask`）、**改写工具参数（`overwrite`）** |
| **`PostToolUse`** | 工具执行**后** | 是（正则匹配工具名） | 自动运行 lint/format、记录审计日志、错误分析 |
| **`PreInvocation`** | 调用大模型**前** | 否（扁平数组） | 拦截用户输入、注入实时系统提示或阻断执行 |
| **`PostInvocation`** | 工具调用结束后 | 否（扁平数组） | 检查输出并强制继续循环（`force_continue`） |
| **`Stop`** | 执行循环准备终止时 | 否（扁平数组） | 检查后台任务或测试是否真完成，未完成则阻止退出 |

### `matcher` 写法（用于 `PreToolUse` / `PostToolUse`）
- `"*"` 或 `""`：匹配所有工具
- `"run_command"`：精确匹配终端命令工具
- `"run_command|view_file"`：正则匹配多个工具
- `"browser_.*"`：匹配所有浏览器工具

---

## 二、输入/输出契约（camelCase JSON）

Hook 脚本通过 **stdin** 接收上下文 JSON，通过 **stdout** 返回决策 JSON。所有字段名均采用 **camelCase**：

- 公共输入字段包含：`conversationId`、`workspacePaths`、`transcriptPath`、`artifactDirectoryPath`、`modelName`、`lastUserInput`、`hookEventName`、`cwd`。
- 注意：脚本的当前工作目录是 **`hooks.json` 所在目录**，而 Agent 的工作目录在 payload 的 `cwd` 字段中。
- 插件内的 Hook 还会收到环境变量 `PLUGIN_ROOT` 和 `PLUGIN_DATA`。

---

## 三、高阶实战技巧

### 1. `PreToolUse` 拦截与参数改写（`overwrite`）
除了返回 `decision`（`"allow"` / `"deny"` / `"ask"` / `"force_ask"`），还可以用 `overwrite` 对工具参数做**顶层浅合并（shallow merge）**替换：

```json
{
  "decision": "allow",
  "overwrite": {
    "CommandLine": "cargo test --offline"
  }
}
```
> 改写后，工具实际执行新参数，且系统会在结果前自动附加提示告知 Agent 参数已被 Hook 改写。

### 2. `PreInvocation` / `SessionStart` 静默注入与用户提示分离
通过 `injectSteps` 注入 `systemMessage`：
- 需要跨轮次持久化给模型看的指令：设置 `{"systemMessage": {"systemMessage": "..."}}`。
- **只想在 UI 展示 Markdown 给用户看、不想发给模型浪费 Token**：设置 `metadata.user_markdown`，同时把 `systemMessage` 设为 `""`。
- 需要直接报错并终止本轮：注入 `errorMessage` 并配合 `"terminationBehavior": "terminate"`。

### 3. `Stop` Hook 防死循环铁律
当 `Stop` Hook 返回 `{"decision": "continue", "reason": "..."}` 时，Agent 会重新进入执行循环。
- 务必检查输入中的 **`continuationActive`**（boolean）和 **`terminationReason`**（如 `"NO_TOOL_CALL"`、`"USER_CANCELED"`、`"MAX_INVOCATIONS"`）。
- 当 `continuationActive` 为 `true`（说明当前已经是在执行 `Stop` Hook 要求继续的工作）或用户主动取消（`"USER_CANCELED"`）时，**不要再次返回 `continue`**，否则会陷入无限循环！

### 当前限制
- 目前仅支持 `"type": "command"`（Shell 命令，Unix 下 `sh -c`，Windows 下 `cmd /c`），默认超时 `30` 秒。
- Hooks 为同步阻塞执行，请确保脚本轻量快速。
