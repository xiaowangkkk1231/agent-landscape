# GitHub Agent 项目全景图

把 GitHub 上真正在用的 Agent 项目按赛道梳理成一张可以搜索、筛选、排序的清单，用来解决一个具体问题：**想搭一个 Agent，到底该从哪个项目开始看。**

**在线浏览 → https://xiaowang018.github.io/agent-landscape/**
**English edition → https://xiaowang018.github.io/agent-landscape/index-en.html** · [README.en.md](README.en.md)

两版页面共用同一份数据与交互逻辑，右上角可互相切换，筛选状态会带过去。

页面最底部留了微信二维码：选型纠结、项目跑不起来、想聊怎么改，扫码直接问（点一下可放大，方便手机对屏扫）。二维码以 data URI 内嵌，页面仍然是单文件。

收录 **137 个仓库 / 17 个赛道 / 累计 846 万星标**。每个项目都标注了中文定位、适用人群、上手门槛和维护状态，而不是只丢一个 star 数排名。页面末尾另设「科研前沿」区块，收录 18 篇 2025–2026 年会改变 Agent 系统设计与评测结论的论文与基准（不计入上面的仓库统计）。本轮新增第 17 个赛道「教程 / 学习资料」，收录 12 份能跟着走的课程、清单、源码剖析与面试题集；加上第 16 个赛道「技能包 / 工作流」和「Agent 学习路线」：从官方课程和框架教程入门，接着做项目，再用公开基准验证，不把课程证书或榜单分数当成工程能力。

---

## 这个页面里有什么

| 赛道 | 说明 | 数量 |
| --- | --- | :--: |
| 编排框架 / SDK | 搭 Agent 的底层骨架 | 21 |
| 编码 Agent | 写代码、改仓库、跑测试 | 21 |
| 低代码平台 / 工作流 | 拖拽或节点式搭建，少写代码 | 7 |
| 浏览器操作 | 让 Agent 自己上网 | 6 |
| 通用自主 Agent | 给个目标自己拆解执行 | 9 |
| 多智能体协作 | 多个角色分工配合 | 6 |
| 桌面 / 电脑操作 | 看屏幕、动鼠标、控本机 | 6 |
| 语音 Agent | 能听会说的实时对话 | 3 |
| 知识库 / RAG | 把私域文档变成 Agent 的上下文 | 8 |
| 深度研究 / 检索 | 自动调研并产出报告 | 6 |
| 记忆层 | 跨会话记住人和事 | 7 |
| 工具协议 / MCP | 给 Agent 装手脚的标准接口 | 9 |
| 技能包 / 工作流 | 把工程纪律写进提示词层，管 Agent 怎么干活 | 4 |
| Agent 可观测 / 评测 | 看得见它干了什么、跑得好不好 | 6 |
| Agentic RL / 训练环境 | 训练 Agent 自己的策略 | 5 |
| Agent 基础设施 | 沙箱、运行时等底座 | 1 |
| 教程 / 学习资料 | 先读别人怎么做的，再决定自己动手 | 12 |

星标前八（截至 2026-11-24）：

| # | 项目 | 星标 | 语言 | 许可证 |
| :-: | --- | --: | --- | --- |
| 1 | [morluto/rea](https://github.com/morluto/rea) | 475,682 | TypeScript | MIT |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 395,121 | TypeScript | MIT |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | 331,701 | Shell | MIT |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | 325,437 | Shell | MIT |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 309,604 | JavaScript | MIT |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 286,111 | TypeScript | MIT |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 265,675 | Python | MIT |
| 8 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 228,818 | TypeScript | MIT |

「前八里六个是成品 Agent / Harness，没有一个传统框架」这个判断这轮仍然成立——但要加一条：**第三、第四名是两个技能包，而且都不是代码仓库意义上的「程序」**。榜首 rea 用 Agent 做逆向工程拿到 47.6 万星，OpenClaw、Hermes 这类「装完就能常驻干活」的运行时占据第二和第七；n8n 掉到第九，LangChain 这种框架鼻祖仍在八名之外。入口从「自己搭」变成「装完直接用」之后，下一层竞争已经挪到了**怎么让装好的 Agent 按规矩干活**。

这也是本轮新增「技能包 / 工作流」赛道的原因。四个包回答的是四个不同问题，不是四选一的竞品：

| 技能包 | 问的问题 | 下手位置 | 什么时候该用 |
| --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 我们是否在做同一件事？ | 写代码之前对齐意图，招牌 `/grill-me` 一次一问 | 需求还在雾里、代码要活很久 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 整条流程走完了吗？ | 六段 SDLC：`/spec` → `/plan` → `/build` → `/test` → `/review` → `/ship` | 团队要上生产、要可预期的质量门 |
| [obra/superpowers](https://github.com/obra/superpowers) | 每一步都真的执行了吗？ | 15 个技能排成固定顺序，写明是强制流程而非建议 | 想要一套开箱即用的完整纪律 |
| [backnotprop/pstack](https://github.com/backnotprop/pstack) | 你能证明它真的能跑吗？ | 事后复现、取证、多模型交叉评审；刻意不设规划技能 | 难复现的 bug、迁移、整夜自主任务 |

实践里更常见的做法是混用而不要全装：改一个按钮颜色不需要 PRD，隔夜跑的迁移必须有证据。技能装太多会挤占上下文，还会互相抢命令名（两个「总入口」都想接管 `/tdd`）。

教程类的情况正好相反：**最高的 `datawhalechina/hello-agents` 只有 8.8 万星，不到技能包第三名（33 万）的三分之一，也进不了前八。** 同属「不参与决策」的品类，`read` 的天花板明显低于 `install`——技能包会被装进工作流反复调用，教程读完一遍就走了，星数更像一次性投票。所以这一赛道不按星数当推荐依据，卡片里写的是「读它之前要会什么」「读完能补上哪块」，按顺序看比按星数排更有用。

第三个变化是「训练」这一层终于被补上了，新增赛道 **Agentic RL / 训练环境**：verl、slime、prime-rl、ART、OpenEnv。原因是这半年 arXiv 上的 Agent 研究重心明显从「怎么调提示词」挪到「怎么造可验证环境和 verifier」——SETA 造了 4,500+ 个终端环境、腾讯混元在做环境随模型一起变难、BIRD-RL 在解有状态数据环境的空间效率。选型上也多了个问题：跑通的流程要不要固化成小模型，把每次的推理钱省下来。

另一个增量是把「看不见的接线」补齐了：**A2A**（Google 发起、现归 Linux 基金会的 Agent 间通信协议）补上 MCP 没管的另一半——Agent 之间怎么发现彼此、怎么委派任务；**promptfoo** 和 **inspect_ai** 让评测能进 CI、能审计；**graphiti** 把记忆从「说过什么」推进到「这条现在还有效吗」。

另一个增量来自博主们的 2026 盘点：DeepSeek 官方的 Harness、用自己订阅跑编码舰队的 Orca、100 行代码的 mini-swe-agent、统管各家 CLI Agent 的 cc-switch 都是这轮补进来的新面孔。同时页面末尾新增「科研前沿」一节——评测基准正在从静态分数转向轨迹与环境级验证（AgentGym2、EvoClaw），记忆研究从「能不能记住」转向「何时该遗忘」（Memora），Agentic RL 的瓶颈从算法转向环境与 verifier（ToolVerse）。


---

## 页面上怎么用

页面是给「现在就要选一个项目动手」的人准备的，不是排行榜，所以筛选维度都围绕这件事：

| 操作 | 作用 | 说明 |
| --- | --- | --- |
| 搜索框 | 匹配仓库名、中文定位、适合人群、点评、GitHub topics | 按 `/` 聚焦，`Esc` 清空；命中的词在卡片上高亮 |
| 赛道 chips | 只看某一类 | 点「全部」回到全量 |
| 语言 | 只留某种实现语言 | 按数量排序，`-` 是 GitHub 未识别 |
| 门槛 | 易（装完能跑）／中（要改代码）／难（要懂架构） | 「教程 / 学习资料」赛道里指**阅读门槛**：易＝零基础能读，中＝要会写代码，难＝要懂架构 |
| 只看活跃 | 45 天内有提交 | 赶时间时先开这个，把沉寂项目挡掉 |
| 排序 | 星数 / 最近更新 | 只影响组内顺序，赛道分组保持不变 |

两个细节：

- **筛选状态会写进地址栏**（形如 `#q=rag&diff=易&lang=Python`），刷新不丢，也可以直接把链接发给同事，对方打开就是你看到的这一屏。
- **搜索命中可能来自看不见的字段**。比如搜 `browser` 会匹配到 GitHub topics 里带 browser 的项目，这些词没有显示在卡片上，所以这类卡片会在仓库名后面挂一个「标签 xxx」的小徽标，告诉你它为什么被筛出来。不想要这个召回，就只搜中文定位里的词。
- 筛出结果时，赛道标题右侧的星数会重算成「当前可见项目」的合计，不是整条赛道的总量。

---

## Agent 学习路线

按「先懂循环，再学编排，最后做验证」走。课程和文档链接均指向发布方或项目官方页面；课程内容、可用性与证书政策可能变化，开始前以原站为准。

下面三步是外部课程与文档。**仓库形态的教程、中文笔记、资源清单和面试题集已单独收进页面的「教程 / 学习资料」赛道**（12 个），可以直接按门槛筛：想先建立概念就挑「易」，想读源码就挑「难」。

| 阶段 | 资料 | 适合谁 / 学什么 | 建议产出 |
| --- | --- | --- | --- |
| 1. 建立心智模型 | [Anthropic：Building effective agents](https://www.anthropic.com/research/building-effective-agents) | 所有人；workflow 与 agent 的边界、提示词链/路由/并行/编排器-工作者/评估器-优化器 | 把一个任务分别画成固定流程和 Agent loop，说明为何选其一 |
| 2. 动手做第一个 Agent | [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit1/introduction) | 初学者；Think → Act → Observe、工具、smolagents，并发布到 Spaces | 做一个能调用工具并对结果做检查的 Agent |
| 3. 理解状态与控制流 | [DeepLearning.AI：AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) · [LangGraph 官方 quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) | 有 Python 基础；从手写循环迁移到图、持久化、streaming、人类介入 | 做一个可暂停、恢复、人工批准的长任务 |
| 4. 横向比较开发栈 | [OpenAI Agents SDK 指南](https://developers.openai.com/api/docs/guides/agents) · [Google ADK 文档](https://google.github.io/adk-docs/) · [Microsoft Agent Framework 概览](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) | 已能写简单 Agent；比较工具调用、handoff、workflow、session 与观测 | 用同一小任务做两个实现，记录状态/错误处理差异 |
| 5. 评估与可靠性 | [SWE-bench leaderboard](https://www.swebench.com/) · [OSWorld](https://os-world.github.io/) · [WebArena](https://webarena.dev/) · [τ-bench](https://github.com/sierra-research/tau-bench) | 想验证真实任务能力；按编码、桌面、浏览器、工具交互选基准 | 为自己的任务写外部 checker、失败分类和回归集 |

### 学习时优先做的项目

- **最小工具 Agent**：不用框架先写一轮 observe → decide → act，给工具加 schema、超时、错误返回和步数上限；确认脚本能解决的部分就别交给模型。
- **带恢复的研究 Agent**：用 LangGraph 或 Microsoft Agent Framework 做搜索、引用收集、草稿、事实检查；加持久状态和人工审批，模拟进程中断后继续运行。
- **小型编码 Agent**：挑一个小型开源仓库，让 Agent 修一个 issue；测试必须由 Agent 之外的命令运行，统计成功率、重试数、耗时和 token 成本。
- **基准复现**：先跑 SWE-bench Verified 的单个样例或 OSWorld 的一个任务，保存环境版本、模型、提示、工具、完整轨迹。榜单数字只在配置可比时参考。

不建议一开始就做「多 Agent 自主公司」：先找一条单 Agent 轨迹的失败点，只有单一执行者确实卡住时才引入委派，并给每个子任务定义输入、输出、权限和验收器。

### 官方项目入口

| 项目 | 从这里开始 | 要学会的核心 |
| --- | --- | --- |
| [smolagents](https://huggingface.co/docs/smolagents/index) | [教程](https://huggingface.co/docs/smolagents/tutorials/overview) | 最小代码 Agent、工具、代码执行边界 |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | [Quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) | state、节点/边、持久化、人工介入 |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | [官方指南](https://developers.openai.com/api/docs/guides/agents) | tools、handoffs、guardrails、tracing |
| [Google ADK](https://google.github.io/adk-docs/) | [Python quickstart](https://google.github.io/adk-docs/get-started/quickstart/) | Agent 与 workflow、工具、评估 |
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) | [First Agent](https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent) | agents、harness、workflows、session 与 middleware |
| [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk) | [Python SDK](https://github.com/anthropics/claude-agent-sdk-python) | 把 Claude Code 的工具循环集成到应用 |
| [Deep Agents](https://github.com/langchain-ai/deepagents) | [官方文档](https://docs.langchain.com/oss/python/deepagents/overview) | 长任务规划、文件系统、子 Agent；高层 Harness，需理解其默认授权与状态行为 |

### 常用基准入口

| 基准 | 主要测什么 | 官方入口 |
| --- | --- | --- |
| SWE-bench | 真实 GitHub issue 修复 | [项目与 leaderboard](https://www.swebench.com/) |
| OSWorld | 跨应用桌面 GUI 操作 | [项目页](https://os-world.github.io/) · [代码](https://github.com/xlang-ai/OSWorld) |
| WebArena | 自托管网站中的浏览器任务 | [项目页](https://webarena.dev/) · [代码](https://github.com/web-arena-x/webarena) |
| τ-bench | 多轮工具调用与业务规则遵循 | [代码与任务](https://github.com/sierra-research/tau-bench) |
| Terminal-Bench | 终端环境中的多步操作 | [项目与 leaderboard](https://www.tbench.ai/) |

---

## 数据是怎么来的

| 字段 | 来源 | 说明 |
| --- | --- | --- |
│ 星标、Fork、语言、许可证、最后提交时间、是否归档、创建时间 | GitHub REST API `/repos/{owner}/{repo}` | 实时抓取，非人工录入 |
| 分类、中文定位、适用人群、点评、上手门槛 | 人工标注 | 主观判断，可讨论 |

维护状态按 GitHub 数据自动判定，归档优先于提交日期（刚归档的仓库最后一次提交也可能很近）：

- **已归档** —— 仓库被 owner 归档，只读停更（不建议作为新项目选型）
- **活跃** —— 45 天内有提交
- **维护中** —— 210 天内有提交
- **沉寂** —— 超过 210 天无提交（这类不建议作为新项目选型）

上手门槛按"装完能不能直接跑"来分三档：**易**（装完能跑）／**中**（需读文档改代码）／**难**（需要理解其架构或研究背景）。

> 许可证标注为 `NOASSERTION` 的（n8n、Dify、AutoGPT、Flowise 等）已逐个人工核对，多为"附加条款 / Sustainable Use"这类**不完全开放**的许可。星标高不等于能随便商用，落地前请逐条读 LICENSE。

---

## 仓库结构

```
agent-landscape/
├── index.html                  # 中文页面，产物
├── index-en.html               # 英文页面，产物
├── data.json                   # 机器抓的元数据（137 条），由 fetch.py 写
├── README.md                   # 中文说明
├── README.en.md                # 英文说明
└── scripts/
    ├── fetch.py                # 抓 GitHub API，刷新 data.json 和 snapshot.json
    ├── annotations.json        # 人工标注（中文定位、适合谁、点评、门槛、赛道）
    ├── annotations.en.json     # 英文标注覆盖层，只含定位 / 适合谁 / 点评
    ├── tracks.json             # 17 个赛道的顺序、标题与副标题（中文）
    ├── tracks.en.json          # 赛道的英文标题与副标题
    ├── i18n.json               # 界面文案（统计标签、卡片字段、JS 提示）中英对照
    ├── snapshot.json           # 数据快照日期，fetch.py 每次写入后更新，build.py 读它算状态
    ├── template.html           # 中文页面模板
    ├── template.en.html        # 英文页面模板
    ├── partials/
    │   ├── style.css           # 两版共用的样式
    │   ├── app.js              # 两版共用的搜索 / 筛选 / 排序逻辑，文案从 i18n.json 注入
    │   └── wechat-qr.png       # 页脚微信二维码（build.py 转成 data URI 内嵌，页面仍是单文件）
    └── build.py                # 合并三者，生成两个页面
```

`index.html` 是纯静态单文件：没有 CDN、没有构建步骤、运行时也不发网络请求，断网也能正常筛选。**但它现在是由脚本生成的，不要直接改** —— 改了会在下次 `build.py` 时被覆盖，要改就改 `scripts/` 下的源文件。

`build.py` 会做一致性校验：`data.json` 里每个仓库都必须在 `annotations.json` 里有标注，反之亦然；英文版必须覆盖全部 137 条（缺一条就报错，避免中英混排）；赛道必须在 `tracks.json` / `tracks.en.json` 里登记且顺序一致；门槛只能是易/中/难。任何一条不满足就报错退出，不生成半张卡。

---

## 怎么更新

数据不是定时任务，是手动重抓。三步：

```bash
# 1. 刷新元数据（星数、Fork、语言、许可证、最后提交时间）
GITHUB_TOKEN=ghp_xxx python scripts/fetch.py --check   # 先看会变什么
GITHUB_TOKEN=ghp_xxx python scripts/fetch.py           # 确认后写入 data.json

# 2. 补中文标注（新增仓库必须在这步加，否则 build 会报错拦住）
#    编辑 scripts/annotations.json；英文版同步补 scripts/annotations.en.json；新赛道改 tracks.json / tracks.en.json

# 3. 生成页面
python scripts/build.py               # 同时写 index.html 与 index-en.html
python scripts/build.py --lang en     # 只重建英文版
python scripts/build.py --check       # 只校验不写文件
```

不带 `GITHUB_TOKEN` 也能跑，但未认证配额只有 **60 次/小时**，而且 504 超时同样计次 —— 137 个仓库需要跑三四轮。带 token 是 5000 次/小时，一次就够。

`fetch.py` 处理了抓数据时最烦的两件事：

1. **限流**：核心 API 报 403/429 时读 `X-RateLimit-Reset` 自动等待重试；仍然失败的仓库**保留旧数据**，不会从 `data.json` 里消失。
2. **仓库改名**：核心 API 报 404 时先查脚本里的 `ALIAS` 映射，再退到 search API 按名字反查。已确认的迁移：

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
   | `volcengine/verl` | `verl-project/verl` |
   | `microsoft/autogen` / `microsoft/semantic-kernel` | `microsoft/agent-framework`（微软新一代 successor；旧仓库仍可作历史参考） |

---

## 关于

这份清单来自一次实际的选型需求：框架太多、评测文章太旧、star 数又不能直接当质量用。所以把"星数"和"它到底能干什么、适不适合我"放在一起看。

收录范围有明确边界：**只收 Agent 相关**，纯 LLM 应用框架、模型推理框架、聊天客户端不在内。判断标准是"这东西能不能自己决定下一步做什么"。

有两个例外，都不计入「自主性」这条判断线，单独成赛道：

- **「技能包 / 工作流」**：它们不做决策，只是写给 Agent 看的 Markdown 纪律。收进来是因为选型时绕不过去——你已经有一堆能自己干活的 Agent 了，接下来要解决的是它们干得靠不靠谱。
- **「教程 / 学习资料」**：连程序都不是，是别人的课程、笔记和清单。收进来是因为「从哪个项目开始看」这个问题，很多时候真正的答案是「先读完这几份资料再动手」。这一赛道里星数只作参考，卡片写的是前置知识和能补上哪块。

发现分类错了、定位写偏了、或者漏掉了重要项目，欢迎开 issue 指正。本仓库只整理公开信息，各项目的版权与许可证归属其原作者。
