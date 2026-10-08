# Awesome Pareto-Flash LLMs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> The **budget segment** of the October 2026 LLM Pareto frontier — cheap models that are Pareto-optimal on price vs quality (and speed). Updated **October 2026**.

This list covers only the budget segment: every hosted model here costs **≤ $0.50 per 1M input tokens**, and each entry is non-dominated on quality-per-dollar among cheap models (see [docs/methodology.md](docs/methodology.md) for the exact rule). For the full intelligence-vs-price frontier across **all** tiers, see the sister repo [awesome-llms-pareto-frontier](https://github.com/dakotac1994/awesome-llms-pareto-frontier).

The October 2026 story: the budget tier is no longer a quality desert. **Claude Haiku 5.5** (Oct 7) scores AA Index 43.4 at $0.10/$0.50 — frontier-adjacent intelligence at commodity prices. Open-weight efficiency models (**GLM-5.3-Flash**, **DeepSeek V4 Flash**, **MiMo-V2.6-Flash**, **Qwen3.8-Flash**) cluster at $0.14–$0.16 input with AA scores in the high 30s to low 40s. And diffusion models (**Mercury 2.5**) run an order of magnitude faster than anything autoregressive in the segment.

**Pricing confidence:** every price below is stamped ✅ **verified 2026-10-08** (corroborated by ≥2 independent sources in the research pass, or read on an official pricing page) or ⚠️ **unverified** (single-sourced or disputed). **Prices are never guessed.** Machine-readable records live in [`data/pareto-flash.json`](data/pareto-flash.json) (hosted APIs) and [`data/self-host.json`](data/self-host.json) (open-weight self-host), each carrying `price_verified`, `speed_verified`, and `quality_verified` booleans.

## 2026 Highlights

- **Claude Haiku 5.5** (Anthropic, Oct 7): AA Index 43.4 at ✅ $0.10/$0.50 — the best quality-per-dollar in the survey by a wide margin.
- **GPT-6 Luna** (OpenAI, Sept 22): AA Index 37 at ✅ $0.10/$0.50, 154 tok/s — the frontier-family price floor.
- **GLM-5.3-Flash** (Z.ai, Aug): AA Index 41.8 at ✅ $0.15/$0.50, MIT open weights — the open-weight value pick.
- **DeepSeek V4.1 Flash** (Sept 10): 217 tok/s with AA Index 39.5; peak/off-peak pricing split still disputed (⚠️).
- **Mercury 2.5** (Inception Labs, ~Oct): diffusion LM at ~675 tok/s independently measured — a different speed band entirely.
- **Price floor:** Nova Micro at ⚠️ $0.035/$0.14 — cheapest API in the survey, quality unverified.
- **Self-host wave:** Nemotron 3 Nano Omni, Gemma 4 27B, Qwen3.8 27B — open weights you can run yourself at ~$0 marginal API cost.

## Contents

- [Budget models](#budget-models)
  - [Anthropic](#anthropic)
  - [OpenAI](#openai)
  - [Google DeepMind](#google-deepmind)
  - [xAI](#xai)
  - [DeepSeek](#deepseek)
  - [Alibaba](#alibaba)
  - [Zhipu AI](#zhipu-ai)
  - [Xiaomi](#xiaomi)
  - [Mistral AI](#mistral-ai)
  - [Meta](#meta)
  - [Amazon](#amazon)
  - [MiniMax](#minimax)
  - [Inception Labs](#inception-labs)
- [Value leaderboard (quality per dollar)](#value-leaderboard-quality-per-dollar)
- [Speed leaderboard](#speed-leaderboard)
- [Self-host open weights](#self-host-open-weights)
- [Excluded & why](#excluded--why)
- [Guides](#guides)
- [Related repositories](#related-repositories)
- [Contributing](#contributing)
- [License](#license)

---

## Budget models

Hosted APIs at ≤ $0.50/1M input tokens, Pareto-optimal on quality-per-dollar. `value_tier` S = top of the frontier, A = strong value, B = thin data or niche.

### Anthropic

- [Claude Haiku 5.5](https://www.anthropic.com/claude) — ✅ **$0.10 in / $0.50 out**. Anthropic's fastest Claude: frontier-class coding at commodity prices; released October 7, 2026. 1M-token context; AA Intelligence Index 43.4 (v4.3); Terminal-Bench 4.0 39.2%; $0.10/$0.50 up to 100K prompt; $0.50/$2.50 above; Released 2026-10-07. Pricing: [anthropic.com](https://www.anthropic.com/pricing). [AA Index 43.4; value tier S].

### OpenAI

- [GPT-6 Luna](https://developers.openai.com/api/docs/models) — ✅ **$0.10 in / $0.50 out**. OpenAI's efficiency-tier model: the cheapest way into the GPT-6 family, priced far below GPT-6 Sol. ~1.05M-token context; 154 tok/s (Artificial Analysis); AA Intelligence Index 37; Released 2026-09-22; >272K prompt: $0.20/$0.75. Pricing: [developers.openai.com](https://developers.openai.com/api/docs/pricing). [AA Index 37.0; 154 tok/s; value tier S].

### Google DeepMind

- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models) — ⚠️ **$0.10 in / $0.40 out** (unverified). Google's long-serving budget workhorse: still the fastest sub-$0.15 model in independent testing. 1M-token context; 244 tok/s (Artificial Analysis); LMArena Elo 1240; Released 2025-02. [quality 74/100; 244 tok/s; value tier A].
- [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models) — ⚠️ **$0.30 in / $2.50 out** (unverified). Google's lightest Gemini 3.5 tier: 192 tok/s for latency-sensitive budget workloads. 1M-token context; 192 tok/s (Artificial Analysis); LMArena Elo 1418; Released 2026-07. [quality 79/100; 192 tok/s; value tier B].

### xAI

- [grok-4-1-fast-reasoning](https://docs.x.ai/) — ✅ **$0.20 in / $0.50 out**. xAI's fast reasoning tier: 2M context at flat budget pricing. 2M-token context; Reasoning variant; Released 2025-11. Pricing: [docs.x.ai](https://docs.x.ai/developers/pricing). [quality unverified; value tier B].
- [grok-4-fast-non-reasoning](https://docs.x.ai/) — ✅ **$0.20 in / $0.50 out**. xAI's fast non-reasoning tier: lowest-latency Grok at budget pricing. 2M-token context; Non-reasoning variant; Released 2025-09. Pricing: [docs.x.ai](https://docs.x.ai/developers/pricing). [quality unverified; value tier B].

### DeepSeek

- [DeepSeek V4 Flash](https://api-docs.deepseek.com/) — ✅ **$0.14 in / $0.28 out**. DeepSeek's budget API tier: open-weights efficiency model at one of the lowest hosted prices in the survey. 1M-token context; 105 tok/s (Artificial Analysis); LMArena Elo 1441; Open weights; Released 2026-04. Pricing: [api-docs.deepseek.com](https://api-docs.deepseek.com/quick_start/pricing). [quality 84/100; 105 tok/s; open weights; value tier S].
- [DeepSeek V4.1 Flash](https://api-docs.deepseek.com/) — ⚠️ **$0.30 in / $1.20 out** (unverified). DeepSeek's current efficiency flagship: near-frontier quality at 217 tok/s, with off-peak discounts. 1M-token context; 217 tok/s (Artificial Analysis); AA Intelligence Index 39.5; SWE-bench Verified 79.0%; MIT open weights; Peak pricing shown; off-peak ~50% discount (split unconfirmed); Released 2026-09-10. [AA Index 39.5; 217 tok/s; open weights; value tier A].

### Alibaba

- [Qwen3.8-Flash](https://qwen.ai/) — ⚠️ **$0.16 in / $0.47 out** (unverified). Alibaba's efficiency tier: strong AA Index scores with open weights at budget pricing. 1M-token context; AA Intelligence Index 39.8; Open weights; Released 2026-08-26. [AA Index 39.8; open weights; value tier A].

### Zhipu AI

- [GLM-5.3-Flash](https://docs.z.ai/) — ✅ **$0.15 in / $0.50 out**. Z.ai's efficiency flagship: near-frontier quality scores at budget prices, with MIT open weights. 1M-token context; 117 tok/s (Artificial Analysis); AA Intelligence Index 41.8; DeepSWE 63.4% (vendor); MIT open weights; Released 2026-08-26. Pricing: [docs.z.ai](https://docs.z.ai/guides/overview/pricing). [AA Index 41.8; 117 tok/s; open weights; value tier S].

### Xiaomi

- [MiMo-V2.6-Flash](https://mimo.mi.com) — ✅ **$0.14 in / $0.28 out**. Xiaomi's efficiency model: 309B/15B-active MoE with MIT open weights at the survey's price floor. 1M-token context; 309B params / 15B active MoE; DeepSWE 67.9% (vendor); MIT open weights; Released 2026-09-21. Pricing: [mimo.mi.com](https://mimo.mi.com). [DeepSWE (vendor-reported): 67.9; open weights; value tier S].

### Mistral AI

- [Ministral 3 3B](https://docs.mistral.ai/models/ministral-3-3b-25-12) — ✅ **$0.10 in / $0.10 out**. Mistral's 3B edge model: symmetric $0.10 pricing and Apache 2.0 open weights. 256K context; Apache 2.0 open weights; Edge-device class; Released 2025-12. Pricing: [docs.mistral.ai](https://docs.mistral.ai/models/ministral-3-3b-25-12). [quality unverified; open weights; value tier A].
- [Ministral 3 8B](https://docs.mistral.ai/models/ministral-3-8b-25-12) — ✅ **$0.15 in / $0.15 out**. Mistral's 8B efficiency model: symmetric $0.15 pricing and Apache 2.0 open weights. 256K context; Apache 2.0 open weights; Released 2025-12. Pricing: [docs.mistral.ai](https://docs.mistral.ai/models/ministral-3-8b-25-12). [quality unverified; open weights; value tier A].

### Meta

- [Llama 4 Scout](https://www.llama.com/) — ⚠️ **$0.15 in / $0.40 out** (unverified). Meta's open-weights efficiency model: 10M-token context at budget API prices. 10M-token context; 198 tok/s (Artificial Analysis); Open weights; Released 2025-04. [quality 71/100; 198 tok/s; open weights; value tier A].

### Amazon

- [Nova Micro](https://aws.amazon.com/bedrock/) — ⚠️ **$0.035 in / $0.14 out** (unverified). Amazon's cheapest Bedrock text model: the lowest per-token price in the survey. Text-only micro tier; Via Amazon Bedrock; Released 2024-12. [quality unverified; value tier B].
- [Nova Lite](https://aws.amazon.com/bedrock/) — ⚠️ **$0.06 in / $0.24 out** (unverified). Amazon's budget multimodal Bedrock model. 300K context; Multimodal (text/image/video); Via Amazon Bedrock; Released 2024-12. [quality unverified; value tier B].
- [Nova 2 Lite](https://aws.amazon.com/bedrock/) — ⚠️ **$0.30 in / $2.50 out** (unverified). Amazon's current-generation lite tier on Bedrock with global routing. Global routing; Via Amazon Bedrock; Released 2026. [quality unverified; value tier B].

### MiniMax

- [MiniMax M3](https://platform.minimax.io/docs/guides/pricing-paygo) — ✅ **$0.30 in / $1.20 out**. MiniMax's multimodal open-weights model: 1M context with text/image/audio/video at budget prices. 1M combined context (2x price above 512K); AA Intelligence Index ~30; SWE-bench Verified 80.5% (vendor); 428B / 23B active MoE; Open weights (MiniMax Community License); Released 2026-06-01. Pricing: [platform.minimax.io](https://platform.minimax.io/docs/guides/pricing-paygo). [AA Index 30.0; open weights; value tier A].

### Inception Labs

- [Mercury 2.5](https://www.inceptionlabs.ai/) — ⚠️ **$0.20 in / $0.75 out** (unverified). Diffusion-based LLM: an order of magnitude faster than autoregressive models in the segment. 260K context; ~675 tok/s independent (AA); vendor claims 1,107; Launch pricing $0.04/$0.15; Diffusion architecture — different speed band; Released ~2026-10. [quality unverified; 675 tok/s; value tier A].

---

## Value leaderboard (quality per dollar)

Hosted entries scored on the AA Intelligence Index v4.3, ranked by index points per $1 of input-token price. Single-benchmark ranking — read [docs/methodology.md](docs/methodology.md) before comparing across sources.

| # | Model | AA Index | $/1M in | Index per $ |
|---|---|---|---|---|
| 1 | [Claude Haiku 5.5](https://www.anthropic.com/claude) | 43.4 | $0.10 | 434 |
| 2 | [GPT-6 Luna](https://developers.openai.com/api/docs/models) | 37.0 | $0.10 | 370 |
| 3 | [GLM-5.3-Flash](https://docs.z.ai/) | 41.8 | $0.15 | 279 |
| 4 | [Qwen3.8-Flash](https://qwen.ai/) | 39.8 | $0.16 | 249 |
| 5 | [DeepSeek V4.1 Flash](https://api-docs.deepseek.com/) | 39.5 | $0.30 | 132 |
| 6 | [MiniMax M3](https://platform.minimax.io/docs/guides/pricing-paygo) | 30.0 | $0.30 | 100 |

## Speed leaderboard

Independently measured output tokens/sec (Artificial Analysis / swfte aggregation). Vendor-claimed figures are labeled in the entries.

| # | Model | tok/s | $/1M in | Architecture |
|---|---|---|---|---|
| 1 | [Mercury 2.5](https://www.inceptionlabs.ai/) | 675 | $0.20 | diffusion |
| 2 | [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models) | 244 | $0.10 | autoregressive |
| 3 | [DeepSeek V4.1 Flash](https://api-docs.deepseek.com/) | 217 | $0.30 | autoregressive |
| 4 | [Llama 4 Scout](https://www.llama.com/) | 198 | $0.15 | autoregressive |
| 5 | [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models) | 192 | $0.30 | autoregressive |
| 6 | [GPT-6 Luna](https://developers.openai.com/api/docs/models) | 154 | $0.10 | autoregressive |
| 7 | [GLM-5.3-Flash](https://docs.z.ai/) | 117 | $0.15 | autoregressive |
| 8 | [DeepSeek V4 Flash](https://api-docs.deepseek.com/) | 105 | $0.14 | autoregressive |

---

## Self-host open weights

The budget models you can download and run yourself — ~$0 marginal API cost, priced in hardware instead of tokens. Full records in [`data/self-host.json`](data/self-host.json).

| Model | Speed | Quality | License note |
|---|---|---|---|
| [Gemma 4 27B](https://ai.google.dev/gemma) | 142 tok/s | quality 75/100 | open weights |
| [Nemotron 3 Nano Omni](https://build.nvidia.com) | 158 tok/s | quality 76/100 | open weights |
| [Qwen3.8 27B](https://qwen.ai/) | — | quality unverified | open weights |
| [Hunyuan Hy3](https://github.com/Tencent-Hunyuan) | — | quality 76/100 | open weights |
| [Ling-3.0-Flash](https://github.com/antgroup) | — | quality 74/100 | open weights |

---

## Excluded & why

Pareto lists are defined by what they leave out. As of October 2026:

| Model | Why excluded |
|---|---|
| Gemini 3.8 Flash ($0.75/$3.75) | Over the $0.50 budget cutoff — the natural step-up reference |
| Qwen 3.6 Plus ($1.40/$5.60), Claude Haiku 4.5 ($1/$5), Kimi K2.6 ($0.73/$3.49) | Over the budget cutoff |
| Celeris-1 (diffusion, ~1,500 tok/s) | No public per-token price — cannot place on a price frontier |
| GPT-5.6 Luna, Grok 3 Mini, GPT-4o mini, Claude 3.5 Haiku, Llama 4 Maverick, Qwen 2.5 Coder 32B, Codestral | Superseded or strictly dominated on quality-per-dollar by a listed model |
| GPT-6 Sol ($2/$10), Gemini 3.6 Flash ($0.75/$3.75) | Covered by the full-frontier sister repo |

Full exclusion log and the cutoff rationale: [docs/methodology.md](docs/methodology.md).

## Guides

- [Methodology](docs/methodology.md) — the budget cutoff, the Pareto rule, and how verification works
- [Choosing a budget model](docs/choosing-a-budget-model.md) — decision guide by workload
- [Glossary](docs/glossary.md) — terms used in this repo
- [Status changes](docs/status-changes.md) — retirements, renames, pricing changes

## Related repositories

- [awesome-llms-pareto-frontier](https://github.com/dakotac1994/awesome-llms-pareto-frontier) — **sister repo: the full intelligence-vs-price Pareto frontier across all tiers (this repo is its budget segment)**.
- [awesome-flash-llms](https://github.com/dakotac1994/awesome-flash-llms) — sibling list: cost-performance Flash-class LLMs and their $/1M-token pricing.
- [awesome-fast-llms](https://github.com/dakotac1994/awesome-fast-llms) — sibling list: inference-speed LLMs, providers, engines, and optimization techniques.
- [awesome-flagship-llms](https://github.com/dakotac1994/awesome-flagship-llms) — sibling list: the single most capable model from every major AI lab.
- [awesome-free-llms](https://github.com/dakotac1994/awesome-free-llms) — sibling list: free LLM API tiers, free chat apps, and open-weight local models.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). One entry = one model; the budget cutoff is $0.50/1M input tokens; prices are stamped with their verification date and never guessed.

## License

[MIT](LICENSE) © 2026 dakotac1994
