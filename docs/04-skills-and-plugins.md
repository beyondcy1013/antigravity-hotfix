# 04. 技能（Skills）、插件（Plugins）与 JSON 配置

如果说 Rules 是“时刻遵守的纪律”，那么 **Skills** 就是“按需翻阅的操作手册”，**Plugins** 则是“一键打包分发的工具箱”。

---

## 一、Skills：渐进式披露（Progressive Disclosure）

Antigravity 默认**不会**把所有 Skill 的全文塞进上下文窗口，而是仅注入每个 Skill 的 `name` 和 `description`。只有当模型（或用户）判断当前任务匹配时，才会读取 `SKILL.md` 及关联文件。

### 标准目录结构
```text
.agents/skills/<skill-name>/
├── SKILL.md          # 必填：含 YAML Frontmatter 的主指令
├── scripts/          # 可选：辅助脚本（如校验、部署、数据清洗）
├── references/       # 可选：大篇幅参考文档，主文件用相对链接按需引用
├── examples/         # 可选：参考实现
└── resources/        # 可选：模板或静态资源
```

### `SKILL.md` 编写最佳实践
```markdown
---
name: service-deploy
description: >-
  Use when deploying, restarting, or verifying the billing service.
  Covers build queue submission, health checks, and rollback steps.
---

# Billing Service Deployment

1. Run preflight check: [preflight.sh](./scripts/preflight.sh)
2. Submit build & deploy via queue...
3. Verify health endpoint returns HTTP 200.
```

**四个关键技巧：**
1. **`description` 决定命中率**：用第三人称写清楚 **做什么（what）** 和 **何时触发（when）**，包含用户常说的关键词或报错特征。
2. **主文件保持精简**：把长篇 API 手册、历史排障案例放到 `references/`，在 `SKILL.md` 中用相对路径链接，避免一次性撑爆上下文。
3. **复杂命令脚本化**：把容易拼错的多步 Shell 命令封装进 `scripts/`，让 Agent 直接调用并检查退出码。
4. **必须包含验收步骤**：告诉 Agent 执行完后如何验证成功（查日志、调接口、跑 dry-run）。

---

## 二、Plugins：打包分发整套能力

Plugin 将相关的 **Skills、Rules、Hooks、MCP Server** 打包为一个带命名空间的独立单元，适合团队共享：

```text
.agents/plugins/<plugin-name>/
├── plugin.json       # 必填：插件清单（name / author / homepage / repository / disabled）
├── hooks.json        # 可选：注意！原生插件必须放在插件根目录，不能放在 hooks/ 下
├── mcp_config.json   # 可选：该插件自带的 MCP 服务
├── rules/            # 可选：建议合并为一个 rules/AGENTS.md
│   └── AGENTS.md
└── skills/           # 可选：插件暴露的技能
    └── <skill-name>/
        └── SKILL.md
```

> [!IMPORTANT]
> **原生插件 `hooks.json` 路径陷阱**：原生插件（包含 `plugin.json`、`.antigravity-plugin/plugin.json` 或 `.gemini-plugin/plugin.json`）在运行时**严格从插件根目录 `<plugin_dir>/hooks.json` 加载**，不会像 `agy plugin install` 导入外部扩展那样把 `hooks/hooks.json` 搬运到根目录。

### 插件开关控制（`config.json` 优先）
- 插件可在 `plugin.json` 中设置 `"disabled": true` 默认关闭。
- 用户在设置 UI 或通过 CLI `plugin enable` / `plugin disable` 切换状态时，会写入 `config.json` 的 `plugins.<dir-name>.enabled`。
- **`config.json` 优先级高于 `plugin.json`**，且不会污染插件自身目录，重装或升级插件时用户偏好依然保留。

---

## 三、JSON 配置（`skills.json` / `plugins.json`）与 5 级优先级

当自定义目录不在默认扫描路径（如放在共享子目录 `tools/agents/skills/`）时，可通过 `.agents/skills.json` 或 `~/.gemini/config/skills.json` 显式注册与继承：

```json
{
  "inherits": [
    {
      "path": "/path/to/shared/skills.json",
      "include_only": ["linter-skill"],
      "exclude": ["deprecated-skill"]
    }
  ],
  "entries": [
    { "path": "tools/agents/skills", "exclude": ["experimental-.*"] },
    { "path": "~/personal-skills" }
  ]
}
```

- **路径解析规则**：`/` 开头为绝对路径，`~/` 开头相对用户主目录，其余相对仓库根目录（`.git` 所在目录，优先回退到包含该 dot-dir 的目录）。
- **`entries` 扫描深度**：每个 entry 目录仅扫描**一层子目录**。

### 加载优先级（从高到低，同名覆盖）
1. **Workspace Project**：从 CWD 向上回溯至仓库根的层级发现（`.agents/`、`AGENTS.md` 等）
2. **Declared Configurations**：工作区 `skills.json` / `plugins.json` 显式声明
3. **Global Discovery**：`~/.gemini/config/`
4. **Built-in Customizations**：应用内置挂载的默认技能
5. **Global Declared Configurations**：全局 JSON 配置中声明的条目
