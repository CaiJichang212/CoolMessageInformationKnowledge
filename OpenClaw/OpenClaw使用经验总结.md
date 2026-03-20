---
title: OpenClaw 使用经验总结  
cover: /Users/lzc/TNTprojectZ/CoolMessageInformationKnowledge/asset/openclaw教程.png
---

## 🧭 OpenClaw 使用经验总结

### 一、核心入口（Quick Access）
| 用途 | 命令/地址 |
|------|----------|
| Web 控制台 | `http://127.0.0.1:18789/` |
| Gateway 状态 | `openclaw gateway status` |
| TUI | `openclaw tui`（无独立 `openclaw-tui` 命令） |
| 记忆状态检查 | `openclaw memory status --deep` |

---

### 二、核心工具（Tools）
**最常用 5 个：**
1. **read/write/edit** — 读写/修改本地文件
2. **exec/process** — 执行终端命令、管理后台进程
3. **web_search/web_fetch** — 搜索网页、抓取正文
4. **browser** — 浏览器自动化（点击/输入/截图）
5. **memory_search/memory_get** — 语义检索记忆（需配置 Embeddings）

---

### 三、技能（Skills）使用经验

#### 已安装技能
- **qveris-official** — 聚合工具搜索（需 `QVERIS_API_KEY`）
- **tavily-search** — AI 优化搜索（需 `TAVILY_API_KEY`）
- **stock-analysis** — 美股/加密货币分析（Yahoo Finance 数据）
- **stock-analysis-a-share** — A 股分析（Sina/Eastmoney/Tushare）
- **self-improvement** — 错误复盘/经验沉淀
- **skill-vetter** — 技能安全审计

#### ⚠️ 技能安装注意事项
- **ClawHub 安全拦截**：部分技能标记为 `suspicious`，需 `--force` 安装
- **安装前审查**：用 `skill-vetter` 检查权限范围、可疑代码
- **技能热更新**：修改 `SKILL.md` 后，当前会话可能不生效，需 **新开 session** 验证

---

### 四、记忆系统（Memory）

#### 配置要点（Embeddings）
```json
{
  "agents.defaults.memorySearch.provider": "openai",
  "agents.defaults.memorySearch.model": "BAAI/bge-m3",
  "agents.defaults.memorySearch.remote.baseUrl": "https://api.siliconflow.cn/v1/",
  "agents.defaults.memorySearch.remote.apiKey": "<SiliconFlow key>"
}
```

#### ⚠️ 常见问题
- **Memory search 不可用**：通常是 Embeddings API 限流（403 RPM limit）
- **索引为 0**：需要 `memory/` 目录存在且有 `YYYY-MM-DD.md` 文件
- **解决方案**：检查 API key、创建记忆文件、等待限流恢复

---

### 五、定时提醒（Cron/Reminder）

#### 使用场景
- **WRD 盘中监控**：每 15 分钟检查脚本输出
- **日终摘要**：每日收盘后自动推送
- **一次性提醒**：如"今晚 20:30 提醒报名"

#### 最佳实践
- **Heartbeat vs Cron**：
  - 用 `HEARTBEAT.md` 做批量周期性检查（邮件/日历/天气）
  - 用 `cron` 做精确时间任务（如"9:00 AM sharp"）
- **提醒文本**：写清楚是提醒，包含时间 gap 和上下文

---

### 六、消息通道（Messaging）

#### QQBot 富媒体标签（必须正确闭合）
```
<qqimg>URL</qqimg>     — 图片
<qqvoice>路径</qqvoice> — 语音
<qqvideo>路径</qqvideo> — 视频
<qqfile>路径</qqfile>   — 文件
```

#### ⚠️ 注意事项
- 标签必须闭合，否则消息无法解析
- 必须嵌入文字回复中，不能只调 tool
- 图片/语音/视频/文件用不同标签，不要混用

---

### 七、股票分析实战经验

#### 技能对比
| 技能 | 数据源 | 适用市场 |
|------|--------|----------|
| stock-analysis | Yahoo Finance | 美股/加密货币 |
| stock-analysis-a-share | Sina/Eastmoney/Tushare | A 股（600xxx/000xxx/300xxx） |

#### WRD 分析案例教训
- **依赖安装慢**：用 `uv run` 临时环境，避免污染主环境
- **表格输出**：QQBot/WhatsApp 不支持 Markdown 表格，改用 bullet lists
- **数据解读**：结合板块对比（如 WRD vs PONY）更有价值

---

### 八、会话管理（Session）

#### 关键经验
- **技能快照**：会话启动时快照 available skills，新增技能需 **新 session** 生效
- **验证方法**：修改 `SKILL.md` 后问"能用哪些技能"，若无变化则需 `/new`
- **会话日志**：`~/.openclaw/agents/main/sessions/*.jsonl`

---

### 九、安全边界
- **不删除文件**：未经授权不得删除任何文件/数据
- **隐私保护**：不读取 `~/.ssh`、`~/.aws`、`MEMORY.md` 等敏感文件
- **外部操作**：发送邮件/推文/公开内容前需确认

---

### 十、快速排查清单
| 问题 | 检查点 |
|------|--------|
| Memory search 失败 | 检查 Embeddings API key、`memory/` 目录 |
| 技能不显示 | 新开 session、检查 `SKILL.md` 格式 |
| Cron 不执行 | `cron list` 查看任务状态、检查 Gateway 日志 |
| QQBot 发图失败 | 检查 `<qqimg>` 标签闭合、URL 可访问 |
