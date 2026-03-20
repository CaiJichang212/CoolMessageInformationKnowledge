---
title: OpenClaw 的 Token 黑洞：每次对话都在烧钱，系统提示词到底有多臃肿？
cover: /Users/lzc/TNTprojectZ/CoolMessageInformationKnowledge/openclaw-token/openclaw-token2.png
---
# 💰 OpenClaw 的 Token 黑洞：每次对话都在烧钱，系统提示词到底有多臃肿？

> 💸 你以为只是在和 AI 对话？实际上每开启一次会话，真金白银正在化为乌有。

## 🌋 引子：一个被忽视的成本黑洞

深夜 11 点，开发者小李揉了揉眼睛，看着屏幕上 OpenClaw 的对话记录。今天他已经开启了 15 次新会话，每次都是为了解决不同的编程问题。直到他打开 token 使用监控，才倒吸一口凉气：**仅仅一天，token 消耗就超过了 50 万，相当于每天烧掉几十美元**。

这不是个例。在 OpenClaw 的社区里，越来越多的用户开始意识到：**这个强大的 AI 自动化工具，正在变成一个 token 吞噬机器** 🌀。

![OpenClaw的Token黑洞](/Users/lzc/TNTprojectZ/CoolMessageInformationKnowledge/openclaw-token/openclaw-token1.png)

## 📋 一、系统提示词：被忽视的"重量级选手"

根据 OpenClaw 官方文档，每次智能体运行都会构建一个自定义的系统提示词。这个提示词包含以下固定部分：

- 🛠️ **Tooling**：工具列表和描述
- 🛡️ **Safety**：安全防护提醒
- 🎯 **Skills**：可用技能列表和加载指令
- 🔄 **OpenClaw Self-Update**：自我更新机制
- 📁 **Workspace**：工作目录配置
- 📚 **Documentation**：文档路径指引
- 📄 **Workspace Files**：引导文件注入
- 🏖️ **Sandbox**：沙箱运行时信息
- ⏰ **Current Date & Time**：时间时区
- 🏷️ **Reply Tags**：回复标签语法
- 💓 **Heartbeats**：心跳确认机制
- 🖥️ **Runtime**：运行环境信息
- 🧠 **Reasoning**：推理可见性级别

看起来每个部分都很必要？**问题就出在"必要"这两个字上** ⚠️。

### 📥 1.1 引导文件的无差别注入

OpenClaw 会在每次会话开始时，自动注入以下引导文件：

```
AGENTS.md
SOUL.md
TOOLS.md
IDENTITY.md
USER.md
HEARTBEAT.md
BOOTSTRAP.md
MEMORY.md（及 memory.md 若存在）
```

官方文档明确说明：这些文件受 `bootstrapMaxChars`（单个文件上限，默认 20000 字符）和 `bootstrapTotalMaxChars`（总上限，默认 150000 字符）限制。

**150000 字符是什么概念？** 按照英文 4 字符/token 计算，仅引导文件就可能消耗 37500+ token。而这还只是基础配置，实际项目中这些文件往往更大。

更致命的是：**这些文件在每次新会话时都会被重新加载，无论你是否需要它们** 🔄。

值得注意的是：子 agent 只注入 AGENTS.md + TOOLS.md，这是官方的精简设计 ✅。

### 🎒 1.2 Skills：80% 的功能永远用不上

官方文档中写道：

> 当存在符合条件的 Skills 时，OpenClaw 注入一个紧凑的可用 Skills 列表...提示词指示模型使用 read 加载列出位置的 SKILL.md。

听起来很智能？现实是：**内置的 Skills 多达几十个，但 80% 的用户真正用到的只有 3-5 个** 📊。

每个 Skill 的描述文件平均 500-1000 token，假设有 20 个 Skills，就意味着每次会话要多消耗 10000-20000 token。**而这些 Skills 中，大部分用户可能永远只会用到其中两三个**。

这就好比你每次去餐厅，服务员都要把整本菜单从头到尾念一遍，而你每次都只点那两道菜 🍜。

## 💵 二、token 消耗的真实账单

让我们算一笔账。假设一个典型的 OpenClaw 使用场景：

### 🔢 2.1 单次会话的 token 构成

**系统提示词部分**：

- 基础框架（Tooling、Safety 等）：约 2000 token
- Skills 列表和加载指令：约 5000 token（按 10 个 Skills 计算）
- 引导文件注入：约 15000-37500 token（按 bootstrapTotalMaxChars 默认 150000 字符计算）
- 文档和配置信息：约 2000 token
- **小计：24000-46500 token** 📈

**对话内容部分**：

- 用户问题：平均 500 token
- AI 回答：平均 2000 token
- 多轮对话（假设 5 轮）：12500 token
- **小计：13000 token** 💬

**单次会话总计：37000-59500 token** 🔥

看起来不多？**如果你每天开启 10 次新会话呢？那就是 37 万 -59.5 万 token。一个月下来，就是 1110 万 -1785 万 token。** 📅

按照 Claude API 的定价（$3/百万 input token），**仅系统提示词部分每月就要花费约 21.6-41.85 美元**——这还只是保守估计（每天仅 10 次）💰。

官方文档明确：OpenClaw 跟踪 Token 而非字符（英文约 4 字符/Token）。打开设置 → 面板 → Token 监控，可以实时查看 Input/Output Token 和预估费用 📊。

### ♻️ 2.2 被浪费的钱从哪里来

根据社区用户的实际反馈，通过正确的优化策略，**可以将 OpenClaw 的 token 使用量减少 30% 到 50%** ✂️。

换句话说：**你当前花费的 token 费用中，至少有一半是可以省下来的** 💡。

## 🤔 三、为什么官方没有优化？

这就引出了一个更深层的问题：**OpenClaw 的开发团队难道不知道这些问题吗？** ❓

### ⚖️ 3.1 设计哲学的取舍

从官方文档可以看出，OpenClaw 的设计哲学是"**功能完整性优先**"。系统提示词中包含了：

- 完整的工具链信息
- 全面的安全防护
- 所有可用的 Skills
- 详细的文档指引
- 运行时环境信息

这种设计的好处是：**模型在任何情况下都有足够的上下文来执行任务**。但代价就是：**token 消耗居高不下** ⬆️。

### 📦 3.2 技术债务的累积

OpenClaw 作为一个快速迭代的开源项目，在功能快速扩张的同时，**技术债务也在不断累积** 📈。

每个新功能都会向系统提示词中添加一些内容，但很少有人去删除那些已经过时或不常用的部分。这就是典型的"**功能蔓延**"（Feature Creep）🌀。

### 👥 3.3 用户分层的需求

官方文档提到：

> OpenClaw 可以为子智能体渲染更小的系统提示词。运行时为每次运行设置一个 promptMode：full（默认）、minimal、none。

这说明官方已经意识到了问题，并提供了 `minimal` 模式用于子智能体。**但问题是，主智能体默认仍然使用** **`full`** **模式** ⚙️。

为什么？因为**高级用户需要完整的功能**，而新手用户可能根本不知道有优化选项 🎯。

## 🚀 四、优化方案：从被动接受到主动出击

面对高昂的 token 成本，用户并非无能为力。以下是经过验证的优化策略：

### 💾 4.1 启用 Prompt Caching（提示词缓存）

这是官方最推荐的高性价比方案。在 Anthropic API 中，**缓存读取的成本显著低于输入 token** ✨。

配置方法：

```yaml
cacheRetention: long
heartbeat: 55m  # 略低于 1 小时 TTL
```

实测可节省 **30%-60%** 的 Input Token。对于重复性高的客服问答或数据提取任务，输入 token 成本节省 20%-50% 📉。

**技能安装方法**：

```bash
# 方式 1：使用 npx 命令
npx clawhub@latest install <skill-name>

# 方式 2：使用 clawhub 命令
clawhub install <skill-name>
```

**⚠️ 技能选择建议**（重要）：

根据社区实测，ClawHub 上技能质量参差不齐：

- 📦 ClawHub 收录技能：13,000+ 个
- 🔴 高风险技能：21%（含恶意软件）
- 🟡 中风险技能：17%
- 🟢 低风险技能：62%

**安装技能前的安全检查**：

1. **必装安全检查工具** 🔍：
   ```bash
   npx clawhub install skill-vetter
   ```
   `skill-vetter` 会扫描技能代码，检查权限申请，识别潜在恶意行为
2. **查询技能信息** 📋：
   ```bash
   npx clawhub search <skill-name>
   ```
3. **访问官网查看** 🌐：
   - 官方技能市场：<https://clawhub.ai/skills>
   - 按下载量排序：<https://clawhub.ai/skills?sort=downloads>
4. **上传 VirusTotal 扫描** 🛡️：
   - 下载技能包后，上传到 <https://www.virustotal.com/> 进行安全检测

**社区推荐的热门技能类型**（需自行验证）🔥：

- 🔍 联网搜索类：`tavily-search`
- 🌐 浏览器自动化：`agent-browser`
- 🧠 长期记忆：`agent-memory`、`elite-longterm-memory`
- 📁 文件操作：`filesystem`
- 💻 代码解释器：`code-interpreter`

**⚠️ 避坑提醒**：

- ❌ 不要盲目安装高下载量技能（曾有毒瘤技能排名第一）
- 🚫 拒绝不必要的敏感权限（如"读取所有文件"）
- ✅ 优先选择官方认证或社区高口碑技能
- 🧹 定期清理不用的技能

### 🗜️ 4.2 使用 /compact 命令压缩历史

长时间会话的聊天记录会不断累积在上下文中。使用 `/compact` 命令，模型会用一段摘要压缩整个历史，同时写入 memory 文件供后续检索 📝。

**建议触发时机** ⏰：

- 大型重构完成时（200+ 轮对话）
- 每次完成一个功能模块后
- 上下文窗口接近饱和时

**关键命令** 🔑：

- `/status`：查看当前会话的上下文使用情况
- `/usage tokens`：追踪每次回复的 token 消耗
- `/compact`：压缩历史会话

### ✂️ 4.3 精简 Skills 配置

**这是最关键的一步** 🎯。检查你的 Skills 目录，问自己三个问题：

1. 过去一个月我用过这个 Skill 吗？
2. 如果现在删除它，会影响我的工作流吗？
3. 我真的需要一次性加载所有 Skills 吗？

如果答案是否定的，**那就删除或禁用它** 🗑️。

### ⚙️ 4.4 自定义引导文件

通过内部钩子 `agent:bootstrap`，可以拦截引导文件注入步骤，修改或替换注入的内容 🔧。

例如：**将 SOUL.md 替换为更精简的版本**，或者完全移除不需要的配置文件 ✂️。

配置示例：

```yaml
# 在配置文件中设置
bootstrapMaxChars: 10000  # 降低单个文件上限
bootstrapTotalMaxChars: 50000  # 降低总上限
```

这样可以强制限制引导文件的大小，避免无意义的 token 消耗 💡。

### 🎚️ 4.5 选择合适的 promptMode

如果不是所有功能都需要，可以尝试使用 `minimal` 模式 🔽：

```yaml
promptMode: minimal
```

这会省略 Skills 列表、Memory Recall 指令、Self-Update、Reply Tags、Messaging、Heartbeats 等部分，**仅保留核心的 Tooling、Safety、Workspace、Sandbox、Current Date & Time、Runtime 等信息** ✅。

**三种 Prompt 模式对比** 📊：

- `full`：主 agent 使用，包含所有部分（默认）
- `minimal`：子 agent 使用，精简模式
- `none`：仅返回基本身份行

**注意**：promptMode 不是面向用户的配置，而是运行时为每次运行设置的内部模式 ⚙️。

## 💭 五、深度思考：AI 工具的成本意识

OpenClaw 的 token 消耗问题，折射出的是整个 AI 行业的一个盲点：**成本意识的缺失** 🎯。

### 👨‍💻 5.1 开发者的盲区

在开发阶段，开发者往往更关注功能的实现，而忽视了使用成本。毕竟：

- 测试环境的 token 费用由公司承担
- 功能演示时只关注效果，不关注效率
- 优化工作被视为"后期优化"，优先级不高

### 👤 5.2 用户的被动

普通用户在使用 AI 工具时，往往处于被动地位：

- 不了解 token 计费的细节
- 不知道有哪些优化选项
- 即使知道，也缺乏技术能力进行配置

### 🏢 5.3 行业的责任

AI 工具提供商应该承担起教育用户的责任 📚：

- **默认配置应该是最优的**，而不是功能最全的
- 提供清晰的成本监控和预警机制
- 将优化选项放在显眼位置，而不是深埋在文档中

## 🔮 六、未来展望：平衡功能与成本

OpenClaw 的 token 消耗问题并非无解。事实上，社区已经涌现出许多优化方案 🌟：

- **动态 Skills 加载**：按需加载，而非全量注入（Skills 系统只列清单 + 路径，按需 read SKILL.md）
- **增量引导**：只在必要时加载完整引导文件（子 agent 只注入 AGENTS.md + TOOLS.md）
- **智能缓存**：识别重复内容，避免重复计费（cacheRetention: long + prompt-guard）
- **分层配置**：为不同使用场景提供不同配置模板（promptMode: full/minimal/none）
- **三层治理**：上下文窗口压缩、配对修复与溢出恢复

**关键是要在功能完整性和成本效率之间找到平衡点** ⚖️。

根据社区反馈，通过综合使用上述优化策略，**可以将总成本削减 70%-95%**，实现真正的"token 自由" 🎉。

## 💎 结语：每一 token 都值得珍惜

AI 工具的强大功能让我们惊叹，但高昂的使用成本也不容忽视。OpenClaw 的系统提示词臃肿问题，只是 AI 应用成本优化的一个缩影 🔍。

作为用户，我们需要：

1. **了解成本构成**：知道钱花在哪里 💡
2. **主动优化配置**：不满足于默认设置 ⚙️
3. **反馈给开发者**：推动产品改进 📢

作为开发者，我们需要：

1. **默认即最优**：将成本意识融入设计 ✨
2. **透明化成本**：让用户清楚每一笔开销 📊
3. **持续优化**：技术债务要及时清理 🧹

**毕竟，只有让 AI 工具既强大又经济，才能真正实现普惠 AI 的愿景** 🌍。

***

**官方文档** 📖：<https://docs.openclaw.ai/zh-CN/concepts/system-prompt>

**关键命令速查** ⌨️：

- `/status`：查看当前会话的上下文使用情况
- `/usage tokens`：追踪每次回复的 token 消耗
- `/compact`：压缩历史会话
- `/context list` 或 `/context detail`：检查每个注入文件的贡献（原始 vs 注入、截断，加上工具 schema 开销）

**社区讨论** 💬：更多优化方案和使用技巧，欢迎在 OpenClaw 社区交流分享。

**成本监控** 📊：打开设置 → 面板 → Token 监控，实时查看 Input/Output Token 和预估费用。

***

## 📎 附录：

> /context list

```Markdown
🧠 Context breakdown
Workspace: /Users/xxx/.openclaw/workspace
Bootstrap max/file: 20,000 chars
Bootstrap max/total: 150,000 chars
Sandbox: mode=off sandboxed=false
System prompt (estimate): 40,486 chars (~10,122 tok) (Project Context 13,026 chars (~3,257 tok))

Injected workspace files:
- AGENTS.md: OK | raw 7,823 chars (~1,956 tok) | injected 7,823 chars (~1,956 tok)
- SOUL.md: OK | raw 1,607 chars (~402 tok) | injected 1,607 chars (~402 tok)
- TOOLS.md: OK | raw 959 chars (~240 tok) | injected 959 chars (~240 tok)
- IDENTITY.md: OK | raw 425 chars (~107 tok) | injected 425 chars (~107 tok)
- USER.md: OK | raw 455 chars (~114 tok) | injected 455 chars (~114 tok)
- HEARTBEAT.md: OK | raw 167 chars (~42 tok) | injected 167 chars (~42 tok)
- BOOTSTRAP.md: MISSING | raw 0 | injected 0
- MEMORY.md: OK | raw 938 chars (~235 tok) | injected 938 chars (~235 tok)

Skills list (system prompt text): 17,203 chars (~4,301 tok) (48 skills)
Skills: qqbot-cron, qqbot-media, 1password, apple-notes, apple-reminders, bear-notes, blogwatcher, blucli, camsnap, clawhub, coding-agent, eightctl, gemini, gifgrep, github, gog, healthcheck, himalaya, imsg, mcporter, … (+28 more)
Tool list (system prompt text): 2,453 chars (~614 tok)
Tool schemas (JSON): 18,796 chars (~4,699 tok) (counts toward context; not shown as text)
Tools: read, edit, write, exec, process, browser, canvas, nodes, cron, message, tts, gateway, agents_list, sessions_list, sessions_history, sessions_send, sessions_yield, sessions_spawn, subagents, session_status, web_search, web_fetch, memory_search, memory_get

Session tokens (cached): unknown / ctx=200000

Inline shortcut: a command token inside normal text (e.g. “hey /status”) that runs immediately (allowlisted senders only) and is stripped before the model sees the remaining message.
```

<br />

> /context detail

```Markdown
🧠 Context breakdown (detailed)
Workspace: /Users/xxx/.openclaw/workspace
Bootstrap max/file: 20,000 chars
Bootstrap max/total: 150,000 chars
Sandbox: mode=off sandboxed=false
System prompt (estimate): 40,486 chars (~10,122 tok) (Project Context 13,026 chars (~3,257 tok))
Injected workspace files:
- AGENTS.md: OK | raw 7,823 chars (~1,956 tok) | injected 7,823 chars (~1,956 tok)
- SOUL.md: OK | raw 1,607 chars (~402 tok) | injected 1,607 chars (~402 tok)
- TOOLS.md: OK | raw 959 chars (~240 tok) | injected 959 chars (~240 tok)
- IDENTITY.md: OK | raw 425 chars (~107 tok) | injected 425 chars (~107 tok)
- USER.md: OK | raw 455 chars (~114 tok) | injected 455 chars (~114 tok)
- HEARTBEAT.md: OK | raw 167 chars (~42 tok) | injected 167 chars (~42 tok)
- BOOTSTRAP.md: MISSING | raw 0 | injected 0
- MEMORY.md: OK | raw 938 chars (~235 tok) | injected 938 chars (~235 tok)
Skills list (system prompt text): 17,203 chars (~4,301 tok) (48 skills)
Skills: qqbot-cron, qqbot-media, 1password, apple-notes, apple-reminders, bear-notes, blogwatcher, blucli, camsnap, clawhub, coding-agent, eightctl, gemini, gifgrep, github, gog, healthcheck, himalaya, imsg, mcporter, … (+28 more)
Top skills (prompt entry size):
- coding-agent: 832 chars (~208 tok)
- qveris-official: 797 chars (~200 tok)
- skill-creator: 759 chars (~190 tok)
- self-improvement: 643 chars (~161 tok)
- github: 572 chars (~143 tok)
- node-connect: 541 chars (~136 tok)
- stock-analysis: 539 chars (~135 tok)
- healthcheck: 491 chars (~123 tok)
- things-mac: 436 chars (~109 tok)
- clawhub: 432 chars (~108 tok)
- stock-analysis-a-share: 429 chars (~108 tok)
- weather: 416 chars (~104 tok)
- xurl: 387 chars (~97 tok)
- qqbot-media: 385 chars (~97 tok)
- himalaya: 383 chars (~96 tok)
- apple-notes: 375 chars (~94 tok)
- 1password: 348 chars (~87 tok)
- skill-vetter: 337 chars (~85 tok)
- wechat-article-formatter: 322 chars (~81 tok)
- wechat-product-manager-writer: 318 chars (~80 tok)
- mcporter: 312 chars (~78 tok)
- apple-reminders: 310 chars (~78 tok)
- summarize: 296 chars (~74 tok)
- wechat-tech-writer: 295 chars (~74 tok)
- wechat-draft-publisher: 293 chars (~74 tok)
- wacli: 277 chars (~70 tok)
- oracle: 276 chars (~69 tok)
- session-logs: 253 chars (~64 tok)
- songsee: 251 chars (~63 tok)
- ordercli: 248 chars (~62 tok)
… (+18 more skills)
Tool list (system prompt text): 2,453 chars (~614 tok)
Tool schemas (JSON): 18,796 chars (~4,699 tok) (counts toward context; not shown as text)
Tools: read, edit, write, exec, process, browser, canvas, nodes, cron, message, tts, gateway, agents_list, sessions_list, sessions_history, sessions_send, sessions_yield, sessions_spawn, subagents, session_status, web_search, web_fetch, memory_search, memory_get
Top tools (schema size):
- message: 4,860 chars (~1,215 tok)
- browser: 2,799 chars (~700 tok)
- nodes: 1,800 chars (~450 tok)
- sessions_spawn: 1,179 chars (~295 tok)
- exec: 1,086 chars (~272 tok)
- web_search: 1,084 chars (~271 tok)
- process: 961 chars (~241 tok)
- cron: 690 chars (~173 tok)
- canvas: 661 chars (~166 tok)
- edit: 591 chars (~148 tok)
- gateway: 497 chars (~125 tok)
- read: 392 chars (~98 tok)
- web_fetch: 374 chars (~94 tok)
- write: 313 chars (~79 tok)
- sessions_send: 273 chars (~69 tok)
- tts: 223 chars (~56 tok)
- sessions_list: 212 chars (~53 tok)
- subagents: 191 chars (~48 tok)
- sessions_history: 161 chars (~41 tok)
- memory_search: 139 chars (~35 tok)
- memory_get: 128 chars (~32 tok)
- session_status: 89 chars (~23 tok)
- sessions_yield: 60 chars (~15 tok)
- agents_list: 33 chars (~9 tok)
Top tools (summary text size):
- cron: 2,689 chars (~673 tok)
- browser: 1,683 chars (~421 tok)
- gateway: 464 chars (~116 tok)
- memory_search: 334 chars (~84 tok)
- read: 298 chars (~75 tok)
- session_status: 207 chars (~52 tok)
- sessions_spawn: 198 chars (~50 tok)
- exec: 181 chars (~46 tok)
- web_search: 175 chars (~44 tok)
- tts: 152 chars (~38 tok)
- memory_get: 151 chars (~38 tok)
- edit: 129 chars (~33 tok)
- web_fetch: 129 chars (~33 tok)
- write: 127 chars (~32 tok)
- nodes: 122 chars (~31 tok)
- agents_list: 118 chars (~30 tok)
- canvas: 106 chars (~27 tok)
- subagents: 105 chars (~27 tok)
- sessions_yield: 97 chars (~25 tok)
- message: 89 chars (~23 tok)
- process: 85 chars (~22 tok)
- sessions_send: 84 chars (~21 tok)
- sessions_list: 54 chars (~14 tok)
- sessions_history: 36 chars (~9 tok)
Tools (param count):
- message: 91 params
- browser: 48 params
- nodes: 37 params
- canvas: 18 params
- sessions_spawn: 17 params
- cron: 13 params
- exec: 12 params
- process: 12 params
- gateway: 12 params
- web_search: 9 params
- edit: 6 params
- sessions_send: 5 params
- read: 4 params
- sessions_list: 4 params
- subagents: 4 params
- write: 3 params
- sessions_history: 3 params
- web_fetch: 3 params
- memory_search: 3 params
- memory_get: 3 params
- tts: 2 params
- session_status: 2 params
- sessions_yield: 1 params
- agents_list: 0 params
Session tokens (cached): unknown / ctx=200000
Inline shortcut: a command token inside normal text (e.g. “hey /status”) that runs immediately (allowlisted senders only) and is stripped before the model sees the remaining message.
```

