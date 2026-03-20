---
title: TradingAgents多智能体LLM金融交易框架
cover: /Users/lzc/TNTprojectZ/CoolMessageInformationKnowledge/asset/TA封面图.png
---

# TradingAgents多智能体LLM金融交易框架

🚀 [框架介绍](#tradingagents-框架) | ⚡ [安装与CLI](#安装与cli) | 🎬 [演示视频](https://www.youtube.com/watch?v=90gr5lwjIho) | 📦 [包使用](#tradingagents-包) | 📄 [引用](#引用)

## TradingAgents 框架

TradingAgents 是一个模拟真实交易公司运作模式的多智能体交易框架。通过部署由大语言模型驱动的专业智能体——从基本面分析师、情绪分析师、技术分析师，到交易员和风险管理团队，平台能够协同评估市场状况并制定交易决策。这些智能体还会进行动态讨论以确定最优策略。


> TradingAgents 框架仅供研究用途。交易表现可能因多种因素而异，包括所选基础语言模型、模型温度参数、交易周期、数据质量以及其他非确定性因素。[本框架不作为财务、投资或交易建议。](https://tauric.ai/disclaimer/)

我们的框架将复杂交易任务分解为专业角色。这种设计确保系统采用稳健、可扩展的方法进行市场分析和决策制定。

### 分析师团队

- 基本面分析师：评估公司财务和业绩指标，识别内在价值和潜在风险信号
- 情绪分析师：运用情绪评分算法分析社交媒体和公众情绪，研判短期市场情绪
- 新闻分析师：监测全球新闻和宏观经济指标，解读事件对市场状况的影响
- 技术分析师：运用MACD、RSI等技术指标识别交易模式并预测价格走势


### 研究团队

- 由多头和空头研究员组成，他们会对分析师团队提供的见解进行批判性评估。通过结构化辩论，权衡潜在收益与固有风险。


### 交易员代理

- 整合分析师和研究员的报告，做出明智的交易决策。基于全面的市场洞察，决定交易时机和规模。


### 风险管理与投资组合经理

- 通过评估市场波动性、流动性及其他风险因素，持续监控投资组合风险。风险管理团队评估并调整交易策略，向投资组合经理提交评估报告以供最终决策。
- 投资组合经理审批交易提案。若获批准，订单将发送至模拟交易所执行。


## 安装与命令行界面

### 安装

克隆TradingAgents仓库：

```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
```

使用您偏好的环境管理工具创建虚拟环境：

```bash
conda create -n tradingagents python=3.13
conda activate tradingagents
```

安装依赖项：

```bash
pip install -r requirements.txt
```

### 所需API

TradingAgents 支持多个 LLM 提供商。请为您选择的提供商设置 API 密钥：

```bash
export OPENAI_API_KEY=...          # OpenAI (GPT)
export GOOGLE_API_KEY=...          # Google (Gemini)
export ANTHROPIC_API_KEY=...       # Anthropic (Claude)
export XAI_API_KEY=...             # xAI (Grok)
export OPENROUTER_API_KEY=...      # OpenRouter
export ALPHA_VANTAGE_API_KEY=...   # Alpha Vantage
```

对于本地模型，请在配置中使用 `llm_provider: "ollama"` 来配置 Ollama。

或者，将 `.env.example` 复制为 `.env` 并填入您的密钥：

```bash
cp .env.example .env
```

### 命令行使用

可直接运行CLI：

```bash
python -m cli.main
```

界面将显示可选参数：股票代码、日期、大语言模型、研究深度等。


运行时会实时显示加载结果，可追踪代理执行进度。


## TradingAgents包

### 实现细节

我们使用 LangGraph 构建 TradingAgents，以确保灵活性和模块化。该框架支持多个 LLM 提供商：OpenAI、Google、Anthropic、xAI、OpenRouter 和 Ollama。

### Python调用

在代码中导入`tradingagents`模块并初始化`TradingAgentsGraph()`对象。`.propagate()`函数将返回决策结果。可运行`main.py`，以下是快速示例：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())

# forward propagate
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

您也可以调整默认配置，设置您偏好的大语言模型（LLMs）、辩论轮次等参数。

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"        # openai, google, anthropic, xai, openrouter, ollama
config["deep_think_llm"] = "gpt-5.2"     # Model for complex reasoning
config["quick_think_llm"] = "gpt-5-mini" # Model for quick tasks
config["max_debate_rounds"] = 2

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

所有配置选项请参见 `tradingagents/default_config.py`。


## 引用

```
@misc{xiao2025tradingagentsmultiagentsllmfinancial,
      title={TradingAgents: Multi-Agents LLM Financial Trading Framework}, 
      author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
      year={2025},
      eprint={2412.20138},
      archivePrefix={arXiv},
      primaryClass={q-fin.TR},
      url={https://arxiv.org/abs/2412.20138}, 
}
```