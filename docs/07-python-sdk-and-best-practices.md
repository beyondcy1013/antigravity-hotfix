# 07. Python SDK 与工程化最佳实践

当你需要把 Antigravity 集成进 CI/CD 流水线、自动化测试套件或自定义编排脚本时，可以使用官方开源的 Python SDK（`google-antigravity/antigravity-sdk-python`）。

---

## 一、安装与环境说明

```bash
pip install google-antigravity
```

> [!IMPORTANT]
> SDK 依赖平台特定的预编译运行时二进制文件（随 PyPI wheel 一起分发），**务必通过 `pip` 安装**以确保运行时二进制可用。

---

## 二、快速上手与安全默认行为

`Agent` 类通过异步上下文管理器自动管理运行时发现、工具挂载、Hook 注册与策略默认值。

> **安全默认**：`LocalAgentConfig` 默认以**只读模式（read-only）**运行！若需允许 Agent 执行写文件、跑命令等操作，必须显式传入 `capabilities=CapabilitiesConfig()`。

```python
import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

async def main():
    config = LocalAgentConfig(
        system_instructions="You are an expert assistant for codebase navigation.",
        capabilities=CapabilitiesConfig(),  # 显式开启写与执行工具
    )

    async with Agent(config) as agent:
        response = await agent.chat("Write a short python script to list files.")
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 三、进阶用法

### 1. 实时监听思考过程与工具调用
在构建可观测性界面或审计流水线时，可以直接订阅 `response.thoughts` 和 `response.tool_calls`：

```python
# 实时流式获取思维增量
async for thought in response.thoughts:
    print(f"[Thinking] {thought}")

# 实时获取强类型 ToolCall 事件
async for call in response.tool_calls:
    print(f"[Executing Tool] {call.name} with args: {call.args}")
```

### 2. 一键启动终端交互循环
```python
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from google.antigravity.utils.interactive import run_interactive_loop

config = LocalAgentConfig(capabilities=CapabilitiesConfig())
async with Agent(config) as agent:
    await run_interactive_loop(agent)
```

---

## 四、高频工程避坑清单

1. **大文件不要整文件硬读**
   使用行号范围（`StartLine` / `EndLine`）配合 `rg` / `grep` 精准定位后再读取，能大幅降低上下文膨胀并延长有效推理轮次。
2. **并行调用独立工具**
   把互不依赖的只读搜索、文件读取、文件写入放在同一轮并发发出，减少总往返延迟与重复 Token 开销。
3. **测试与校验必须“到达断言”**
   不要用提前 `return`、忽略失败或放宽断言来制造“伪绿”；确保记录真实测试命令、非零执行数与退出码。
4. **产品目录区分**
   不同入口的本地会话/产物目录互不混用：
   - CLI：`~/.gemini/antigravity-cli/`
   - Antigravity 2.0：`~/.gemini/antigravity/`
   - IDE：`~/.gemini/antigravity-ide/`
   - 全局配置：`~/.gemini/config/`
