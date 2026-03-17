---
title: OpenClaw教程-妙想金融skill使用指南  
cover: /Users/lzc/TNTprojectZ/CoolMessageInformationKnowledge/asset/微信公众号头像.png
---

# 妙想skill简介

妙想skill集成海量专业金融数据，涵盖4大功能，每个skill支持单独调用，为您的投研和投资决策提供全方位支持！

同时妙想skill兼容OpenClaw，开箱即用。

| skill名称                    | skill描述                                                                                                                                                                                                                                                                                         | 功能说明                                                                    |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **智能选股**                   | 通过自然语言查询进行选股、选板块、选基金。类型支持 A股、港股、美股、基金、ETF、可转债、板块。调用 MCP 股票基金筛选工具获取数据，将返回的 datalist 按 columns 映射为中文列名，输出全量 CSV 及数据说明文件。调用前需配置 EM_API_KEY。clawhub地址：<https://clawhub.ai/Financial-AI-Analyst/mx-stockpick>                                                                                      | 快速筛选符合特定条件的股票。支持多维度选股条件设置，包括基础财务指标、MACD等技术指标，帮助投资者快速锁定潜力标的      |
| **MX_FinSearch** **市场搜索** | 通过自然语言检索时效性金融资讯（新闻、公告、研报），提取正文并可保存为本地文本文件。调用前需配置 EM_API_KEY。clawhub地址：<https://clawhub.ai/Financial-AI-Analyst/mx-finsearch>                                                                                                                                                                  | 提供全面的金融资讯检索能力。通过接入多个权威资讯源，支持实时新闻搜索、事件追踪、公告查询等功能，快速获取市场动态        |
| **MX_MacroData宏观查询**      | 通过自然语言查询宏观经济数据，结果转为 CSV 并生成描述文件。支持查询 GDP、CPI、货币供应量等宏观指标。调用前需配置 EM_API_KEY。clawhub地址：<https://clawhub.ai/Financial-AI-Analyst/mx-macrodata>                                                                                                                                                    | 提供全面的宏观经济数据查询能力。整合全球主要经济体官方数据源，覆盖核心宏观指标，帮助投资者洞察经济周期、把握市场大势      |
| **MX_FinData** **财务查数**   | 一个面向多金融品种与多金融主体的数据查询技能。支持使用自然语言查询股票、板块、指数、企业发行人、债券、非上市公司等对象的各类金融指标与报表数据，包括量化数据、实时行情、主力资金、估值、公司基本信息、财务、高管、主营业务、股东、融资等各类金融指标；也可查询股票、非上市公司、股东、高管人物等主体之间的关系数据。技能执行后会生成一个包含查数结果的 xlsx 文件，以及一个对查询结果进行说明和描述的 txt 文件。调用前需配置 EM_API_KEY。clawhub地址：<https://clawhub.ai/Financial-AI-Analyst/mx-findata> | 提供详尽的股票财务数据查询能力。覆盖A股、港股、美股市场，支持查询PE、PB、ROE、营收、利润等核心财务指标，助力基本面分析 |

# 典型场景效果

| skill名称                    | 问句                                  |
| -------------------------- | ----------------------------------- |
| **MX_StockPick智能选股**      | 今日首板涨停的股票，非ST                       |
| **MX_FinSearch** **市场搜索** | 宁德时代近期公告                            |
| **MX_MacroData宏观查询**      | 中美近十年GDP对比                          |
| **MX_FinData** **财务查数**   | 宁德时代近一个月走势分析，并查询25年分业务收入情况并用图表可视化展示 |
| **多skill综合使用**             | 今日A股收盘点评，并生成可视化报告                   |

# 快速开始

前置说明

openclaw🦞有本地部署和云端部署两种方式，部署后，均可通过飞书/QQ等IM工具进行操控：

- 本地部署：本地部署是指您在本地电脑上安装了openclaw，可进行本地电脑的操作。
- 云端部署：云端部署是指您的openclaw部署在云端，通过云端的服务器完成任务，无法对本地电脑进行操作，具体情形包括：
- 接入云厂商的openclaw：包括腾讯云、火山ark、阿里云、百度云等云厂商提供的claw入口。 - 接入三方平台的claw：包括kimi claw、maxclaw等大模型厂商和三方厂商提供的claw入口。

## 方式一：一句话安装（推荐）

1. **首先访问**[妙想官网](https://ai.eastmoney.com/mxClaw)**获取skill的API key**


2. **将复制好的API key替换以下内容中的xxxxxx：**

> 帮我安装以下四个skill，我的API key为xxxxxx：
>
> <https://clawhub.ai/Financial-AI-Analyst/mx-macrodata>
>
> <https://clawhub.ai/Financial-AI-Analyst/mx-stockpick>
>
> <https://clawhub.ai/Financial-AI-Analyst/mx-finsearch>
>
> <https://clawhub.ai/Financial-AI-Analyst/mx-findata>

无论您是本地部署，还是云端部署，均可**直接给您的claw🦞发送以上内容，实现一句话自动安装妙想skill**（通过本地openclaw webUI、 云端claw或已配置的飞书/企业微信/QQ等渠道发送均可）。

1. **开启你的金融任务吧！**

> 示例问句：今日A股收盘点评，并生成可视化报告

claw将通过妙想专业的选股、查数和资讯检索skill，生成准确的金融报告。


注意，由于claw背后仍使用通用的大模型，无法精细化处理金融业务逻辑，因此对skill的选择可能出现偏差。您可通过以下方式，让claw默认调用专业的妙想skill进行分析！

**方式一：每次发送问句时，前缀指定调用妙想skill：**

> “**调用MX_Skills/调用MX_FinData/调用MX_StockPick/调用MX_FinSearch/调用MX_MacroData**进行xxxxx分析”

**方式二：将调用妙想skill作为分析金融的默认选项，放到claw的执行原则和长期记忆里，示例指令如下：**

> 把这个执行原则写到你的Agent.md和memory里，即当我查询或分析金融相关问题时，默认调用MX_Skills进行分析，具体如下：
>
> 如果是查询金融数据，包括股票、基金、债券、行业、指数、板块等相关数据时，调用MX_FinData skill 进行金融数据查询，例如问股票的基本面指标、技术面指标、经营和财务指标等各类数据；
>
> 如果是筛选符合条件的股票、基金和行业板块等，则调用MX_StockPick skill 进行选股/选基金/选行业板块，例如问今日上涨股票等选股问句；
>
> 如果是查询宏观经济相关的数据，则调用MX_MacroData skill 进行宏观经济数据查询，例如问GDP、cpi、原材料价格等宏观经济数据；
>
> 如果是联网检索，查询金融资讯、时事新闻、市场热点、公告、研报等内容，则调用MX_FinSearch 进行金融资讯搜索，例如问股票相关资讯、市场热点、实时事件等；
>
> 根据你需要收集的信息类型，按上述原则选择对应的skill执行。

## 方式二：下载skill压缩包安装

如果您使用 方式一 安装失败，可选择下载skill压缩包进行安装，但skill压缩包需要根据您所使用的claw🦞情形，选择不同的操作方法，具体如下：

### 本地部署claw--skill安装指南

如果您是本地部署的claw，请参考以下步骤进行妙想skill安装：

| 步骤                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. 访问[妙想官网](https://ai.eastmoney.com/mxClaw)获取skill压缩包                                                                                                                                                                                                                                                           |
| 2. 打开压缩包所在文件夹，复制压缩包                                                                                                                                                                                                                                                                                              |
| 3. 将压缩包发送给本地open claw，可通过open claw入口，或飞书、QQ等已配置渠道发送  |
| 4. 安装成功🎉，开启你的金融任务吧！                                                                                                                                                                                                                                                                                             |

常见问题

## Git接入问题

### Q：Clawhub地址在哪里？

A：

宏观查询skill地址：<https://clawhub.ai/Financial-AI-Analyst/mx-macrodata>

智能选股skill地址：<https://clawhub.ai/Financial-AI-Analyst/mx-stockpick>

市场搜索skill地址：<https://clawhub.ai/Financial-AI-Analyst/mx-finsearch>

财务查数skill地址：<https://clawhub.ai/Financial-AI-Analyst/mx-findata>

### Q：Clawhub Git 接入后，版本更新是否会更便捷？

A：是的。接入 Git 后，仅需执行 `git pull` 命令即可拉取最新版本代码，配合内置的自动配置脚本，可一键完成版本更新。

## 故障排查

### Q：**API Key 无效**

A：确认申请的 Key 未过期、未绑定其他设备，或重新申请新 Key。

### Q：API 已达到使用限额

A：目前每日有使用次数上限，超过上限后需等待次日方可使用。

### Q：妙想skill返回结果为空或报错

A：claw具有自主问题解决能力，skill执行出现问题可直接通过指令让其自主排查问题并修复。

## 常见养虾指令

### Q：claw回复环境不支持怎么办？

A：直接回复“修复上述环境”，这样claw会自行想办法修复。

### Q：claw回复缺少依赖怎么办？

A：直接回复“安装一下上述缺少的依赖”，这样claw会自行想办法安装。

### Q：claw回复缺少工具怎么办？

A：直接回复“安装一下上述缺少的工具”，这样claw会自行想办法安装。

备注：妙想skill目前共6个，只不过仅开放4个。

参考文档：<https://my.feishu.cn/wiki/QdQfwpb0RiNiKhkHsRkc2nT3n5y>

妙想claw官网：<https://ai.eastmoney.com/mxClaw>

妙想skills ClawHub官网：<https://clawhub.ai/u/Financial-AI-Analyst>
