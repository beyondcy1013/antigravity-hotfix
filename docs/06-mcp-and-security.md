# 06. MCP 协议集成与安全沙箱策略

---

## 一、MCP Servers 配置技巧（`mcp_config.json`）

Model Context Protocol (MCP) 让 Antigravity 可以无缝接入数据库、内部 API、浏览器或自定义工具服务。

### 配置文件位置
- **全局生效**：`~/.gemini/config/mcp_config.json`
- **随插件生效**：`plugins/<plugin_name>/mcp_config.json`（仅在插件启用时加载，工具自动带命名空间防冲突）

### 支持的两种传输模式

```json
{
  "mcpServers": {
    "sqlite-helper": {
      "command": "sqlite-mcp-server",
      "args": ["/path/to/database.db"],
      "env": {
        "DB_READONLY": "true"
      }
    },
    "remote-service": {
      "url": "https://mcp.mycompany.com/mcp"
    }
  }
}
```

1. **Stdio（本地进程）**：通过 `command`、`args`、`env` 启动本地可执行文件或脚本（如 `node`、`python3`）。
2. **Streamable HTTP（远程服务）**：通过 `url`（兼容旧键名 `serverUrl`）连接远程 MCP 端点。

> [!WARNING]
> **不支持旧版 HTTP+SSE 传输（MCP spec 2024-11-05）**。请将 `url` 指向服务端的 Streamable HTTP 端点（通常是 `/mcp` 而非 `/sse`）。如果目标服务只支持旧版 SSE，请使用 `mcp-remote` 等桥接器以 **Stdio** 方式挂载。

### 调试查看
在桌面端 UI 中，可通过 **Additional Options (...) > MCP Servers** 查看当前已连接的服务及暴露的工具列表。

---

## 二、权限控制与终端沙箱（Global vs Project）

在 Antigravity 2.0 Settings 中，你可以对安全边界做精细化分级控制。**项目级配置（Project-Level Settings）优先级高于全局配置**。

### 核心策略选项
1. **工具执行策略（Tool Execution Policy）**：
   - `always-proceed`：自动放行（仅建议在高度信任或沙箱内使用）
   - `request-review`：按风险请求人工确认
   - `strict`：严格审核
   - `proceed-in-sandbox`：在沙箱内自动放行
2. **终端沙箱（Terminal Sandbox）**：
   在受限沙箱环境中运行终端命令，可按项目单独开启或关闭。
3. **工作区外文件访问（Non-Workspace File Access）**：
   控制 Agent 读写当前工作区根目录之外文件的权限（`allow` / `ask` / `deny`）。
4. **网络访问策略（Internet Access Policy）**：
   控制 Agent 发起网络请求的权限（`allow` / `ask` / `deny`）。
5. **细粒度白名单 / 黑名单**：
   - **Command Allowlist / Denylist**：指定永远放行或永远禁止的终端命令。
   - **Browser Allowlist**：限制浏览器工具允许访问的域名范围。
   - **Permission Grants**：针对特定文件、命令、URL 定义全局或项目级授权规则。

### 安全实践建议
- 对生产运维或敏感仓库：开启 **Terminal Sandbox** + **Non-Workspace File Access = `ask`/`deny`** + **Command Denylist**（或用 `PreToolUse` Hook 做二次校验）。
- 仅在受控的研发沙箱项目中考虑放宽自动执行策略，避免误操作宿主机环境。
