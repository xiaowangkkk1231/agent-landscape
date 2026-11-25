# Agent Landscape on GitHub

A map of the agent projects people actually use, organized by track into one list you can search, filter and sort. It answers one question: **you want to build an agent — which project do you start reading?**

**Browse online → https://xiaowang018.github.io/agent-landscape/index-en.html** · [中文版](README.md)

The bottom of the page carries a WeChat QR code: if you're stuck choosing between projects, can't get one running, or want to talk through how to adapt it, scan and ask. Click the code to enlarge it if you're scanning off the screen. It's embedded as a data URI, so the page stays a single file.

**137 repositories / 17 tracks / 8.46M stars.** Every project carries a hand-written positioning note, who it is for, the effort it takes and its maintenance status — not just a star ranking. The page ends with a "Research front" section covering 18 papers and benchmarks from 2025–2026 that change how agents are designed or evaluated (not counted in the repository totals).

---

## What's on the page

| Track | What it is | Count |
| --- | --- | :--: |
| Orchestration frameworks / SDKs | The skeleton you build an agent on | 21 |
| Coding agents | Write code, patch repos, run tests | 21 |
| Low-code platforms / Workflows | Drag-and-drop or node-based, less code | 7 |
| Browser control | Let the agent use the web itself | 6 |
| General autonomous agents | Give a goal, it decomposes and executes | 9 |
| Multi-agent collaboration | Roles split the work | 6 |
| Desktop / Computer use | See the screen, move the mouse, drive the machine | 6 |
| Voice agents | Real-time speech in and out | 3 |
| Knowledge base / RAG | Turn private documents into agent context | 8 |
| Deep research / Retrieval | Research a topic and write the report | 6 |
| Memory layers | Remember people and facts across sessions | 7 |
| Tool protocols / MCP | A standard interface for hands and feet | 9 |
| Skill packs / Workflows | Engineering discipline written into the prompt layer | 4 |
| Observability / Evaluation | See what it did and how well it did it | 6 |
| Agentic RL / Training environments | Train the agent's own policy | 5 |
| Agent infrastructure | Sandboxes, runtimes and other foundations | 1 |
| Tutorials / Learning resources | Read how others built it before you start | 12 |

Top eight by stars (as of 2026-11-24):

| # | Project | Stars | Language | License |
| :-: | --- | --: | --- | --- |
| 1 | [morluto/rea](https://github.com/morluto/rea) | 475,682 | TypeScript | MIT |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 395,121 | TypeScript | MIT |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | 331,701 | Shell | MIT |
| 4 | [obra/superpowers](https://github.com/obra/superpowers) | 325,437 | Shell | MIT |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 309,604 | JavaScript | MIT |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 286,111 | TypeScript | MIT |
| 7 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 265,675 | Python | MIT |
| 8 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 228,818 | TypeScript | MIT |

The observation still holds: **six of the top eight are finished agents or harnesses, and not one is a classic framework.** But add this: **third and fourth place are skill packs, which are not "programs" in any code sense.** rea, at the top, does reverse engineering with an agent and carries 476k stars; runtimes like OpenClaw and Hermes — "install it and it works, all day" — hold second and seventh. n8n sits at ninth; LangChain, the framework ancestor, is still outside the eight. Once the entry point shifted from "build it yourself" to "install and run", the next layer of competition moved to **how you make an installed agent behave**.

That is why the "Skill packs / Workflows" track exists. Its four packages answer four different questions rather than competing:

| Package | The question it asks | Where it intervenes | When to use it |
| --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Are we building the same thing? | Aligns intent before code, via `/grill-me`, one question at a time | The requirement is still foggy and the code must live long |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Did we finish the whole loop? | Six-stage SDLC: `/spec` → `/plan` → `/build` → `/test` → `/review` → `/ship` | Teams shipping to production that need predictable quality gates |
| [obra/superpowers](https://github.com/obra/superpowers) | Was every step actually executed? | 15 skills in a fixed order, documented as mandatory rather than advisory | You want one complete discipline out of the box |
| [backnotprop/pstack](https://github.com/backnotprop/pstack) | Can you prove it actually runs? | Post-hoc reproduction, forensics, multi-model review; deliberately no planning skill | Bugs that resist reproduction, migrations, overnight autonomous runs |

In practice, mix rather than install everything: changing a button color needs no PRD, an overnight migration needs evidence. Too many skills crowd the context and fight over command names (two "main entry points" both want `/tdd`).

Tutorials are the opposite case: **the best `datawhalechina/hello-agents` has only 88k stars, less than a third of the third-place skill pack (331k), and cannot reach the top eight.** Within the same "does not make decisions" category, `read` has a visibly lower ceiling than `install` — skill packs get called repeatedly inside a workflow, tutorials get read once. So this track does not rank by stars; the cards say "what you need to know first" and "which gap it fills", and reading in order beats sorting by popularity.

The third shift is that **training** finally has a layer, the new **Agentic RL / Training environments** track: verl, slime, prime-rl, ART, OpenEnv. Over the past six months the arXiv center of gravity moved from "how to prompt" to "how to build verifiable environments and verifiers": SETA built 4,500+ terminal environments, Tencent Hunyuan is making environments harder alongside the model, BIRD-RL is solving space efficiency in stateful data environments. Selection now includes a new question: should a working flow be distilled into a small model to save per-inference cost.

One more addition fills in the "invisible wiring": **A2A** (started by Google, now under the Linux Foundation) covers the half MCP does not — how agents discover each other and delegate tasks; **promptfoo** and **inspect_ai** put evaluation into CI and make it auditable; **graphiti** pushes memory from "what was said" to "is this still valid".

The rest comes from 2026 roundups: DeepSeek's official Harness, Orca which runs a coding fleet on your own subscriptions, the 100-line mini-swe-agent, and cc-switch which manages every CLI agent from one panel.

---

## How to use the page

The page is for someone who needs to pick a project and start now, not a leaderboard, so every filter serves that goal:

| Control | Effect | Notes |
| --- | --- | --- |
| Search | Matches repo name, positioning, audience, notes and GitHub topics | Press `/` to focus, `Esc` to clear; matched terms are highlighted |
| Track chips | Show one category | "All" returns to the full list |
| Language | Keep one implementation language | Sorted by count; `-` means GitHub could not detect one |
| Effort | Easy / Medium / Hard | In the Tutorials track this means **reading effort**: Easy = no prerequisites, Hard = needs theory |
| Active only | Pushed within 45 days | Turn it on when you're in a hurry and want dormant projects out of the way |
| Sort | Stars / last push | Affects order within a track only |

Three details:

- **Filter state is written into the URL** (e.g. `#q=rag&diff=easy&lang=Python`), so a refresh keeps it and you can send the link to a colleague.
- **Some matches come from fields you can't see.** Searching `browser` can hit a GitHub topic that isn't rendered on the card, so such cards get a small "tag xxx" badge explaining why they matched.
- When a filter is applied, the star total at the right of each track header is recomputed for the visible projects, not the whole track.

---

## Learning path

"Understand the loop, then orchestration, then validation." Course and documentation links point to the publisher's or project's official page; content, availability and certificate policies change, so check the source before starting.

Repository-shaped tutorials, Chinese notes, resource lists and interview question banks live in the **Tutorials / Learning resources** track (12 projects); filter by effort to pick.

| Stage | Resource | Who / what you learn | Suggested output |
| --- | --- | --- | --- |
| 1. Build a mental model | [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Everyone; the boundary between workflows and agents, prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer | Draw one task as both a fixed workflow and an agent loop, and justify the choice |
| 2. Build your first agent | [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit1/introduction) | Beginners; Think → Act → Observe, tools, smolagents, publish to Spaces | An agent that calls tools and checks its results |
| 3. Understand state and control flow | [DeepLearning.AI: AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) · [LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) | Python basics; moving from a hand-written loop to a graph, persistence, streaming, human-in-the-loop | A long task that can pause, resume and require approval |
| 4. Compare the official stacks | [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) · [Google ADK](https://google.github.io/adk-docs/) · [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) | Can already write a simple agent; compare tool use, handoffs, workflows, sessions and observability | Two implementations of the same small task, with notes on state and error handling |
| 5. Evaluation and reliability | [SWE-bench leaderboard](https://www.swebench.com/) · [OSWorld](https://os-world.github.io/) · [WebArena](https://webarena.dev/) · [τ-bench](https://github.com/sierra-research/tau-bench) | Want to verify real task ability; pick a benchmark by domain | An external checker, failure taxonomy and regression set for your own task |

### Projects worth doing while learning

- **Minimal tool agent**: write one observe → decide → act loop without a framework; add schemas, timeouts, error returns and step limits. Whatever a script can solve, don't hand to a model.
- **Research agent with recovery**: use LangGraph or Microsoft Agent Framework for search, citation collection, drafting and fact-checking; add persistent state and human approval, then simulate a process restart.
- **Small coding agent**: pick a small open-source repo and have the agent fix one issue; tests must run outside the agent; track success rate, retries, latency and token cost.
- **Benchmark reproduction**: run one SWE-bench Verified sample or one OSWorld task, saving versions, model, prompt, tools and the full trajectory. Only compare leaderboard numbers when configurations match.

Don't start with a "multi-agent autonomous company": find the failure point of a single trajectory first, and only add delegation when a single executor is genuinely stuck — then define input, output, permissions and a verifier for every sub-task.

### Official project entry points

| Project | Start here | What to learn |
| --- | --- | --- |
| [smolagents](https://huggingface.co/docs/smolagents/index) | [Tutorial](https://huggingface.co/docs/smolagents/tutorials/overview) | Minimal code agents, tools, execution boundaries |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | [Quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) | State, nodes and edges, persistence, human-in-the-loop |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | [Guide](https://developers.openai.com/api/docs/guides/agents) | Tools, handoffs, guardrails, tracing |
| [Google ADK](https://google.github.io/adk-docs/) | [Python quickstart](https://google.github.io/adk-docs/get-started/quickstart/) | Agents and workflows, tools, evaluation |
| [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) | [First agent](https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent) | Agents, harness, workflows, sessions and middleware |
| [Claude Agent SDK](https://docs.anthropic.com/en/docs/claude-code/sdk) | [Python SDK](https://github.com/anthropics/claude-agent-sdk-python) | Embedding Claude Code's tool loop in an application |
| [Deep Agents](https://github.com/langchain-ai/deepagents) | [Docs](https://docs.langchain.com/oss/python/deepagents/overview) | Long-task planning, filesystem, sub-agents; a high-level harness, so understand its default permissions and state |

### Benchmark entry points

| Benchmark | What it measures | Official page |
| --- | --- | --- |
| SWE-bench | Fixing real GitHub issues | [Project and leaderboard](https://www.swebench.com/) |
| OSWorld | Cross-application desktop GUI tasks | [Project](https://os-world.github.io/) · [Code](https://github.com/xlang-ai/OSWorld) |
| WebArena | Browser tasks in self-hosted sites | [Project](https://webarena.dev/) · [Code](https://github.com/web-arena-x/webarena) |
| τ-bench | Multi-turn tool use with business rules | [Code and tasks](https://github.com/sierra-research/tau-bench) |
| Terminal-Bench | Multi-step operations in a terminal | [Project and leaderboard](https://www.tbench.ai/) |

---

## Where the data comes from

| Field | Source | Notes |
| --- | --- | --- |
| Stars, forks, language, license, last push, archived flag, creation date | GitHub REST API `/repos/{owner}/{repo}` | Fetched live, not typed by hand |
| Category, positioning, audience, notes, effort | Hand-written annotation | Subjective and open to debate |

Maintenance status is derived automatically, and the archived flag outranks the push date (a freshly archived repo can have a very recent last commit):

- **Archived** — the repo is read-only, no further updates (not a good choice for a new build)
- **Active** — pushed within 45 days
- **Maintained** — pushed within 210 days
- **Dormant** — no push for over 210 days (not a good choice for a new build)

Effort follows "does it run once installed": **Easy** (runs out of the box) / **Medium** (read the docs, change code) / **Hard** (understand the architecture or research background).

> Entries marked `NOASSERTION` (n8n, Dify, AutoGPT, Flowise and others) were checked by hand; most carry additional terms or Sustainable Use clauses and are **not fully open**. High stars do not mean free commercial use — read the LICENSE.

---

## Repository layout

```
agent-landscape/
├── index.html                  # Chinese page, generated
├── index-en.html               # English page, generated
├── data.json                   # Machine-fetched metadata (137 entries), written by fetch.py
├── README.md                   # Chinese README
└── scripts/
    ├── fetch.py                # Fetch GitHub API, refresh data.json and snapshot.json
    ├── annotations.json        # Chinese annotations (positioning, audience, notes, effort, track)
    ├── annotations.en.json     # English overlay: pitch / aud / note only
    ├── tracks.json             # Chinese track order, titles and subtitles
    ├── tracks.en.json          # English track titles and subtitles
    ├── i18n.json               # UI strings (stats, card labels, JS messages) for both languages
    ├── snapshot.json           # Snapshot date, written by fetch.py, read by build.py
    ├── template.html           # Chinese page template
    ├── template.en.html        # English page template
    ├── partials/
    │   ├── style.css           # Shared CSS for both pages
    │   ├── app.js              # Shared search / filter / sort logic, strings from i18n.json
    │   └── wechat-qr.png       # Footer WeChat QR (build.py inlines it as a data URI, page stays single-file)
    └── build.py                # Merge everything and render both pages
```

Both HTML files are pure static single files: no CDN, no build step at runtime, no network requests, so filtering works offline. **They are generated — don't edit them by hand**: the next `build.py` run overwrites changes. Edit the sources under `scripts/`.

`build.py` validates consistency: every repo in `data.json` must have an annotation and vice versa; every track must be registered; effort must be 易/中/难; the English overlay must cover all 137 entries. Any failure aborts instead of emitting half a page.

---

## How to update

Data is refreshed by hand, in three steps:

```bash
# 1. Refresh metadata (stars, forks, language, license, last push)
GITHUB_TOKEN=ghp_xxx python scripts/fetch.py --check   # preview changes first
GITHUB_TOKEN=ghp_xxx python scripts/fetch.py           # then write data.json

# 2. Add annotations (new repos must be annotated or build fails)
#    Edit scripts/annotations.json and scripts/annotations.en.json;
#    new tracks go in scripts/tracks.json and scripts/tracks.en.json

# 3. Render pages
python scripts/build.py                 # writes index.html and index-en.html
python scripts/build.py --check         # validate without writing
python scripts/build.py --lang en       # English page only
```

Without `GITHUB_TOKEN` it still runs, but the unauthenticated quota is **60 requests/hour** and 504 timeouts also count — 137 repos takes three or four rounds. With a token it is 5000/hour and one pass is enough.

`fetch.py` handles the two annoying parts of fetching:

1. **Rate limits**: on 403/429 it reads `X-RateLimit-Reset` and waits, capped at 90 seconds; repos that still fail **keep their old data** instead of disappearing.
2. **Renames**: on 404 it checks the `ALIAS` map, then falls back to search by repository name. Confirmed migrations:

   | Old address | Current address |
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
   | `microsoft/autogen` / `microsoft/semantic-kernel` | `microsoft/agent-framework` (Microsoft's successor; the old repos remain useful history) |

---

## About

This list came from a real selection problem: too many frameworks, evaluation articles that are out of date, and star counts that cannot stand in for quality. So stars and "what does it actually do and is it for me" are shown together.

The scope has a clear boundary: **agents only** — pure LLM application frameworks, inference engines and chat clients are out. The test is whether the thing can decide its own next step.

Two exceptions don't pass that test and get their own tracks:

- **Skill packs / Workflows**: they make no decisions, they are Markdown discipline for an agent to read. They are included because you cannot avoid them when choosing: you already have a pile of agents that work, and the next problem is whether they work reliably.
- **Tutorials / Learning resources**: not even programs — other people's courses, notes and lists. Included because "which project do I start with" often really means "read these first". In this track stars are only a hint; the cards describe prerequisites and which gap each resource fills.

If a category is wrong, a description is off, or an important project is missing, open an issue. This repository only organizes public information; copyright and licenses belong to the original authors.
