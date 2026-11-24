# GitHub Agent 项目全景图

把 GitHub 上真正在用的 Agent 项目按赛道梳理成一张可以搜索、筛选、排序的清单，用来解决一个具体问题：**想搭一个 Agent，到底该从哪个项目开始看。**

**在线浏览 → https://xiaowang018.github.io/agent-landscape/**

收录 **87 个仓库 / 14 个赛道 / 累计 465.7 万星标**。每个项目都标注了中文定位、适用人群、上手门槛和维护状态，而不是只丢一个 star 数排名。

---

## 这个页面里有什么

| 赛道 | 说明 | 数量 |
| --- | --- | :--: |
| 编排框架 / SDK | 搭 Agent 的底层骨架 | 16 |
| 编码 Agent | 写代码、改仓库、跑测试 | 14 |
| 低代码平台 / 工作流 | 拖拽或节点式搭建，少写代码 | 6 |
| 浏览器操作 | 让 Agent 自己上网 | 5 |
| 通用自主 Agent | 给个目标自己拆解执行 | 6 |
| 多智能体协作 | 多个角色分工配合 | 4 |
| 桌面 / 电脑操作 | 看屏幕、动鼠标、控本机 | 6 |
| 语音 Agent | 能听会说的实时对话 | 2 |
| 知识库 / RAG | 把私域文档变成 Agent 的上下文 | 6 |
| 深度研究 / 检索 | 自动调研并产出报告 | 5 |
| 记忆层 | 跨会话记住人和事 | 5 |
| 工具协议 / MCP | 给 Agent 装手脚的标准接口 | 7 |
| Agent 可观测 / 评测 | 看得见它干了什么、跑得好不好 | 4 |
| Agent 基础设施 | 沙箱、运行时等底座 | 1 |

星标前八（截至 2026-11-24）：

| # | 项目 | 星标 | 语言 | 许可证 |
| :-: | --- | --: | --- | --- |
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 265,675 | Python | MIT |
| 2 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 228,818 | TypeScript | MIT |
| 3 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 211,913 | TypeScript | NOASSERTION |
| 4 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 188,155 | Python | NOASSERTION |
| 5 | [langgenius/dify](https://github.com/langgenius/dify) | 161,747 | Python | NOASSERTION |
| 6 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 156,881 | Python | MIT |
| 7 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 156,801 | TypeScript | 闭源分发 |
| 8 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 149,959 | Python | MIT |

一个值得注意的现象：**前八里已经没有「纯框架」的位置了。** 第一梯队是两类东西——装完就能自己干活的成品 Agent（Hermes 26.6 万、OpenCode 22.9 万），和拖拽就能上线的可视化平台（n8n、Dify、Langflow）。框架退到了第二梯队：真正被大量使用的入口，是"不用自己写代码就能跑起来"的东西，框架更多是给要做深度定制的团队准备的。

另一个变化是重心在往「怎么让它可靠」挪：这次扩表新增了 **Agent 可观测 / 评测** 和 **语音 Agent** 两个赛道——Langfuse、DeepEval 这类工具的总星标已经超过不少框架，说明大家开始关心「它跑得对不对、稳不稳」，而不只是「能不能跑」。

---

## 数据是怎么来的

| 字段 | 来源 | 说明 |
| --- | --- | --- |
| 星标、Fork、语言、许可证、最后提交时间、创建时间 | GitHub REST API `/repos/{owner}/{repo}` | 实时抓取，非人工录入 |
| 分类、中文定位、适用人群、点评、上手门槛 | 人工标注 | 主观判断，可讨论 |

维护状态按最后提交时间自动判定：

- **活跃** —— 45 天内有提交
- **维护中** —— 210 天内有提交
- **沉寂** —— 超过 210 天无提交（这类不建议作为新项目选型）

上手门槛按"装完能不能直接跑"来分三档：**易**（装完能跑）／**中**（需读文档改代码）／**难**（需要理解其架构或研究背景）。

> 许可证标注为 `NOASSERTION` 的（n8n、Dify、AutoGPT、Flowise 等）已逐个人工核对，多为"附加条款 / Sustainable Use"这类**不完全开放**的许可。星标高不等于能随便商用，落地前请逐条读 LICENSE。

---

## 仓库结构

```
agent-landscape/
├── index.html    # 单文件页面，无外部依赖，双击即可在本地打开
└── data.json     # 数据快照（87 条），字段与页面一致
```

`index.html` 里没有 CDN、没有构建步骤、没有网络请求，断网也能正常筛选。

---

## 怎么更新

数据不是定时任务，是手动重抓。流程：

```bash
# 1. 改候选仓库列表（agent-projects/fetch.py 里的 REPOS）
python fetch.py      # 走核心 API，60 次/小时，504 也计次
python fetch2.py     # 核心配额用完后，改走 search API（10 次/分钟）
python fetch4.py     # 按 topic 批量检索兜底
python fetch5.py     # 个别仓库用镜像拿元数据

# 2. 补充中文标注（新增仓库必须在这步加，否则不会出现在页面上）
#    编辑 meta.py 的 META 字典

# 3. 生成页面
python gen.py        # 输出 index.html
```

抓数据时会遇到的两个真实问题：

1. **核心 API 未认证只有 60 次/小时，且 504 超时同样计次。** 所以脚本设计成"核心 API 打头，配额耗尽后自动降级到 search API 和 topic 检索"。
2. **仓库改名非常频繁。** 照老教程 clone 会 404，脚本里用 `ALIAS` 做映射。目前已确认的迁移：

   | 旧地址 | 现地址 |
   | --- | --- |
   | `geekan/MetaGPT` | `FoundationAgents/MetaGPT` |
   | `All-Hands-AI/OpenHands` | `OpenHands/OpenHands` |
   | `block/goose` | `aaif-goose/goose` |
   | `jlowin/fastmcp` | `PrefectHQ/fastmcp` |
   | `modelscope/agentscope` | `agentscope-ai/agentscope` |
   | `OpenInterpreter/open-interpreter` | `openinterpreter/openinterpreter` |
   | `gpt-engineer-org/gpt-engineer` | `AntonOsika/gpt-engineer` |
   | `sst/opencode` | `anomalyco/opencode` |
   | `strands-agents/sdk-python` | `strands-agents/harness-sdk` |

---

## 关于

这份清单来自一次实际的选型需求：框架太多、评测文章太旧、star 数又不能直接当质量用。所以把"星数"和"它到底能干什么、适不适合我"放在一起看。

收录范围有明确边界：**只收 Agent 相关**，纯 LLM 应用框架、模型推理框架、聊天客户端不在内。判断标准是"这东西能不能自己决定下一步做什么"。

发现分类错了、定位写偏了、或者漏掉了重要项目，欢迎开 issue 指正。本仓库只整理公开信息，各项目的版权与许可证归属其原作者。
