---
title: Claude Code 速查指南
cover: /Users/lzc/TNTprojectZ/CoolExplore/.trae/skills/wenyan-publish/asset/微信公众号头像.png
---

# Claude Code 速查指南（The Shorthand Guide to Everything Claude Code）

> **作者**: @affaan (cogsec)
> **日期**: 2026-01-17
> **链接**: https://x.com/affaan/status/2012378465664745795
> **互动**: ❤️ 10624  🔁 1223  💬 159

## 简介

**Claude Code 速查指南（The Shorthand Guide to Everything Claude Code）**

这是作者 affaan 连续 10 个月深度使用 Claude Code 后整理的完整配置总结，涵盖 skills、hooks、subagents、MCPs、plugins，以及实践中真正有效的工作方法。

自二月份实验性发布以来，affaan 一直是 Claude Code 的重度用户，并与 @DRodriguezFX 一起，凭借完全使用 Claude Code 构建的 [Zenith](https://zenith.chat) 赢得了 Anthropic x Forum Ventures 黑客松。

[嵌入推文: https://x.com/i/status/1967797706757394906]

---

## Skills and Commands

Skills 类似于 rules（规则），但更聚焦于特定作用域和工作流。需要执行某类固定流程时，它们相当于提示词的快捷封装。

在与 Opus 4.5 进行长时间编码会话后，如果需要清理死代码和散落的 .md 文件，可以运行 `/refactor-clean`。

需要测试时，可以使用 `/tdd`、`/e2e`、`/test-coverage`。Skills 和 commands 也可以在单个提示中串联使用。

此外，也可以创建一个 skill，在 checkpoint 更新 codemaps —— 这是一种让 Claude 快速导航代码库、避免消耗过多上下文进行探索的方式。

```
~/.claude/skills/codemap-updater.md
```

Commands 是通过斜杠命令执行的 skills。它们有重叠，但存储位置不同：

- **Skills**: `~/.claude/skills` —— 更广泛的工作流定义
- **Commands**: `~/.claude/commands` —— 快速可执行的提示词

```bash
# Skill 结构示例
~/.claude/skills/
  pmx-guidelines.md      # 项目特定模式
  coding-standards.md    # 语言最佳实践
  tdd-workflow/          # 包含 README.md 的多文件 skill
  security-review/       # 基于检查清单的 skill
```

---

## Hooks

Hooks 是基于触发器的自动化机制，会在特定事件发生时执行。与 skills 不同，它们主要绑定在工具调用和生命周期事件上。

### Hook 类型

1. **PreToolUse** —— 工具执行前（验证、提醒）
2. **PostToolUse** —— 工具完成后（格式化、反馈循环）
3. **UserPromptSubmit** —— 当你发送消息时
4. **Stop** —— 当 Claude 完成响应时
5. **PreCompact** —— 上下文压缩前
6. **Notification** —— 权限请求

### 示例：长时间运行命令前的 tmux 提醒

```json
{
  "PreToolUse": [
    {
      "matcher": "tool == \"Bash\" && tool_input.command matches \"(npm|pnpm|yarn|cargo|pytest)\"",
      "hooks": [
        {
          "type": "command",
          "command": "if [ -z \"$TMUX\" ]; then echo '[Hook] Consider tmux for session persistence' >&2; fi"
        }
      ]
    }
  ]
}
```

**专业提示**：使用 `hookify` 插件以对话方式创建 hooks，而无需手动编写 JSON。运行 `/hookify` 并描述你想要的即可。

---

## Subagents

Subagents 是编排器（主 Claude）可用于委派任务的独立进程，通常具备明确的作用域。它们可以在后台或前台运行，从而释放主 agent 的上下文压力。

Subagents 与 skills 配合得很好 —— 一个能够执行 skills 子集的 subagent 可以被委派任务并自主使用这些 skills。它们还可以使用特定工具权限进行沙盒化。

```bash
# Subagent 结构示例
~/.claude/agents/
  planner.md           # 功能实现规划
  architect.md         # 系统设计决策
  tdd-guide.md         # 测试驱动开发
  code-reviewer.md     # 质量/安全审查
  security-reviewer.md # 漏洞分析
  build-error-resolver.md
  e2e-runner.md
  refactor-cleaner.md
```

为每个 subagent 配置允许的工具、MCPs 和权限，以实现正确的范围限定。

---

## Rules and Memory

你的 `.rules` 文件夹保存 Claude 应该**始终遵循**的最佳实践的 `.md` 文件。两种方案：

1. **单一 CLAUDE.md** —— 所有内容放在一个文件中（用户级或项目级）
2. **Rules 文件夹** —— 按关注点分组的模块化 `.md` 文件

```bash
~/.claude/rules/
  security.md      # 无硬编码密钥，验证输入
  coding-style.md  # 不可变性，文件组织
  testing.md       # TDD 工作流，80% 覆盖率
  git-workflow.md  # 提交格式，PR 流程
  agents.md        # 何时委派给 subagents
  performance.md   # 模型选择，上下文管理
```

### Rules 示例

- 代码库中不使用 emoji
- 前端避免使用紫色调
- 部署前始终测试代码
- 优先使用模块化代码而非巨型文件
- 永不提交 console.log

---

## MCPs (Model Context Protocol)

MCPs 可以将 Claude 直接连接到外部服务。它不是 API 的替代品，而是围绕 API 构建的、由提示词驱动的封装层，在信息检索和操作编排上提供更高灵活性。

**示例**：Supabase MCP 让 Claude 直接拉取特定数据，直接在源头上运行 SQL，无需复制粘贴。数据库、部署平台等也是一样。

**Chrome in Claude**：是一个内置的插件 MCP，让 Claude 自主控制你的浏览器 —— 点击查看事物如何运作。

### ⚠️ 关键：上下文窗口管理

**谨慎选择 MCPs**。affaan 将所有 MCPs 保存在用户配置中，但会禁用未使用的项目。可以导航到 `/plugins` 向下滚动查看，或运行 `/mcp`。

在压缩之前，你的 200k 上下文窗口在启用过多工具时可能只剩 70k。性能会显著下降。

**经验法则**：配置中保留 20-30 个 MCPs，但保持少于 10 个启用 / 少于 80 个活动工具。

---

## Plugins

Plugins 会将工具打包成便于安装的形式，减少繁琐的手动配置。一个 plugin 可以是 skill + MCP 的组合，也可以将 hooks/tools 一并打包。

### 安装 plugins

```bash
# 添加市场
claude plugin marketplace add https://github.com/mixedbread-ai/mgrep

# 打开 Claude，运行 /plugins，找到新市场，从中安装
```

**LSP Plugins**：如果你经常在编辑器之外运行 Claude Code，LSP Plugins 会非常有用。Language Server Protocol 能让 Claude 实时获得类型检查、转到定义和智能补全等能力，而无需打开 IDE。

```bash
# 已启用插件示例
typescript-lsp@claude-plugins-official  # TypeScript 智能
pyright-lsp@claude-plugins-official     # Python 类型检查
hookify@claude-plugins-official         # 对话式创建 hooks
mgrep@Mixedbread-Grep                   # 比 ripgrep 更好的搜索
```

与 MCPs 同样的警告 —— 注意你的上下文窗口。

---

## Tips and Tricks

### 键盘快捷键

- `Ctrl+U` —— 删除整行（比反复按退格键快）
- `!` —— 快速 bash 命令前缀
- `@` —— 搜索文件
- `/` —— 启动斜杠命令
- `Shift+Enter` —— 多行输入
- `Tab` —— 切换思考显示
- `Esc Esc` —— 中断 Claude / 恢复代码

### 并行工作流

`/fork` —— 分叉对话以并行执行不重叠的任务，而不是刷屏排队消息

**Git Worktrees** —— 用于重叠的并行 Claude 而无冲突。每个 worktree 是独立的 checkout

```bash
git worktree add ../feature-branch feature-branch
# 现在在每个 worktree 中运行独立的 Claude 实例
```

**tmux 用于长时间运行的命令**：流式传输并观察 Claude 运行的日志/bash 进程。

```bash
tmux new -s dev
# Claude 在这里运行命令，你可以分离并重新连接
tmux attach -t dev
```

**mgrep > grep**：`mgrep` 是对 ripgrep/grep 的重大改进。通过插件市场安装，然后使用 `/mgrep` skill。支持本地搜索和网络搜索。

```bash
mgrep "function handleSubmit"  # 本地搜索
mgrep --web "Next.js 15 app router changes"  # 网络搜索
```

### 其他有用的命令

- `/rewind` —— 回到之前的状态
- `/statusline` —— 使用分支、上下文 %、todos 自定义
- `/checkpoints` —— 文件级撤销点
- `/compact` —— 手动触发上下文压缩

### GitHub Actions CI/CD

使用 GitHub Actions 在你的 PR 上设置代码审查。配置后 Claude 可以自动审查 PR。

### 沙盒化

对有风险的操作使用沙盒模式 —— Claude 在受限环境中运行，不影响你的实际系统。（使用 `--dangerously-skip-permissions` 则做相反的事情，让 Claude 自由漫游，如果不注意可能具有破坏性。）

---

## 关于编辑器

虽然不一定必须依赖编辑器，但它会显著影响 Claude Code 工作流的体验。Claude Code 可以在任何终端中运行，但搭配功能完善的编辑器，可以获得实时文件跟踪、快速导航和集成命令执行等能力。

### Zed（作者的首选）

affaan 使用 [Zed](https://zed.dev) —— 这是一个基于 Rust 的编辑器，轻量、快速且高度可定制。

**为什么 Zed 与 Claude Code 配合良好：**

- **Agent 面板集成** —— Zed 的 Claude 集成让你实时跟踪 Claude 编辑时的文件更改。在 Claude 引用的文件之间跳转而无需离开编辑器
- **性能** —— 用 Rust 编写，瞬间打开，处理大型代码库无卡顿
- **CMD+Shift+R 命令面板** —— 在可搜索的 UI 中快速访问所有自定义斜杠命令、调试器和工具。即使你只想运行一个快速命令而不切换到终端
- **极低的资源占用** —— 不会在重负载操作期间与 Claude 争夺系统资源
- **Vim 模式** —— 如果你用的话，完整的 vim 键位

1. **分屏** —— 一边是带 Claude Code 的终端，另一边是编辑器
2. `Ctrl + G` —— 在 Zed 中快速打开 Claude 当前正在处理的文件
3. **自动保存** —— 启用自动保存以使 Claude 的文件读取始终是最新的
4. **Git 集成** —— 使用编辑器的 git 功能在提交前审查 Claude 的更改
5. **文件监视器** —— 大多数编辑器自动重新加载已更改的文件，请确认已启用

### VSCode / Cursor

这也是一个可行的选择，与 Claude Code 配合良好。你可以以终端格式使用它，使用 `\ide` 启用 LSP 功能（与 plugins 现在有点冗余）来自动与编辑器同步。或者你可以选择更集成的扩展，与编辑器匹配 UI。

---

## affaan 的配置

### Plugins

已安装：（通常一次只启用 4-5 个）

```markdown
ralph-wiggum@claude-code-plugins       # 循环自动化
frontend-design@claude-code-plugins    # UI/UX 模式
commit-commands@claude-code-plugins    # Git 工作流
security-guidance@claude-code-plugins  # 安全检查
pr-review-toolkit@claude-code-plugins  # PR 自动化
typescript-lsp@claude-plugins-official # TS 智能
hookify@claude-plugins-official        # Hook 创建
code-simplifier@claude-plugins-official
feature-dev@claude-code-plugins
explanatory-output-style@claude-code-plugins
code-review@claude-code-plugins
context7@claude-plugins-official       # 实时文档
pyright-lsp@claude-plugins-official    # Python 类型
mgrep@Mixedbread-Grep                  # 更好的搜索
```

### MCP Servers

已配置（用户级）：

```json
{
  "github": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"] },
  "firecrawl": { "command": "npx", "args": ["-y", "firecrawl-mcp"] },
  "supabase": {
    "command": "npx",
    "args": ["-y", "@supabase/mcp-server-supabase@latest", "--project-ref=YOUR_REF"]
  },
  "memory": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"] },
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  },
  "vercel": { "type": "http", "url": "https://mcp.vercel.com" },
  "railway": { "command": "npx", "args": ["-y", "@railway/mcp-server"] },
  "cloudflare-docs": { "type": "http", "url": "https://docs.mcp.cloudflare.com/mcp" },
  "cloudflare-workers-bindings": {
    "type": "http",
    "url": "https://bindings.mcp.cloudflare.com/mcp"
  },
  "cloudflare-workers-builds": {
    "type": "http",
    "url": "https://builds.mcp.cloudflare.com/mcp"
  },
  "cloudflare-observability": {
    "type": "http",
    "url": "https://observability.mcp.cloudflare.com/mcp"
  },
  "clickhouse": { "type": "http", "url": "https://mcp.clickhouse.cloud/mcp" },
  "AbletonMCP": { "command": "uvx", "args": ["ableton-mcp"] },
  "magic": { "command": "npx", "args": ["-y", "@magicuidesign/mcp@latest"] }
}
```

按项目禁用（上下文窗口管理）：

```markdown
# 在 ~/.claude.json 的 projects.[path].disabledMcpServers 中
disabledMcpServers: [
  "playwright",
  "cloudflare-workers-builds",
  "cloudflare-workers-bindings",
  "cloudflare-observability",
  "cloudflare-docs",
  "clickhouse",
  "AbletonMCP",
  "context7",
  "magic"
]
```

**这是关键** —— 虽然配置了 14 个 MCPs，但每个项目只启用约 5-6 个，以保持上下文窗口健康。

### 关键 Hooks

```json
{
  "PreToolUse": [
    // 长时间运行命令的 tmux 提醒
    { "matcher": "npm|pnpm|yarn|cargo|pytest", "hooks": ["tmux reminder"] },
    // 阻止不必要的 .md 文件创建
    { "matcher": "Write && .md file", "hooks": ["block unless README/CLAUDE"] },
    // git push 前审查
    { "matcher": "git push", "hooks": ["open editor for review"] }
  ],
  "PostToolUse": [
    // 使用 Prettier 自动格式化 JS/TS
    { "matcher": "Edit && .ts/.tsx/.js/.jsx", "hooks": ["prettier --write"] },
    // 编辑后 TypeScript 检查
    { "matcher": "Edit && .ts/.tsx", "hooks": ["tsc --noEmit"] },
    // 警告 console.log
    { "matcher": "Edit", "hooks": ["grep console.log warning"] }
  ],
  "Stop": [
    // 会话结束前审计 console.logs
    { "matcher": "*", "hooks": ["check modified files for console.log"] }
  ]
}
```

### 自定义 Status Line

显示用户、目录、git 分支（带脏标记）、剩余上下文 %、模型、时间和 todo 数量。

### Rules 结构

```markdown
~/.claude/rules/
  security.md      # 强制性安全检查
  coding-style.md  # 不可变性，文件大小限制
  testing.md       # TDD，80% 覆盖率
  git-workflow.md  # 约定式提交
  agents.md        # Subagent 委派规则
  patterns.md      # API 响应格式
  performance.md   # 模型选择（Haiku vs Sonnet vs Opus）
  hooks.md         # Hook 文档
```

### Subagents

```markdown
~/.claude/agents/
  planner.md           # 拆解功能
  architect.md         # 系统设计
  tdd-guide.md         # 先写测试
  code-reviewer.md     # 质量审查
  security-reviewer.md # 漏洞扫描
  build-error-resolver.md
  e2e-runner.md        # Playwright 测试
  refactor-cleaner.md  # 死代码移除
  doc-updater.md       # 保持文档同步
```

---

## 关键要点

1. **不要过度复杂化** —— 把配置当作微调，而不是架构
2. **上下文窗口是宝贵的** —— 禁用未使用的 MCPs 和 plugins
3. **并行执行** —— 分叉对话，使用 git worktrees
4. **自动化重复性工作** —— hooks 用于格式化、linting、提醒
5. **限定 subagent 范围** —— 有限的工具 = 专注的执行

---

## 参考资料

- [Plugins Reference](https://code.claude.com/docs/en/plugins-reference)
- [Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [Interactive Mode](https://code.claude.com/docs/en/interactive-mode)
- [Memory System](https://code.claude.com/docs/en/memory)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [MCP Overview](https://code.claude.com/docs/en/mcp-overview)

---

> 注：这只是细节的一部分。如果大家感兴趣，作者后续可能会发布更具体的内容。

---

> 本文档为英文原文的中文翻译，原始链接：https://x.com/affaan/status/2012378465664745795
