# Choosing a Budget Model

Decision guide for the October 2026 budget segment (≤ $0.50/1M input tokens). Prices and scores are the 2026-10-08 snapshot; check the README badges for verification status.

## By workload

- **Cheapest API, period** — Nova Micro (⚠️ $0.035/$0.14). Quality unverified: fine for bulk low-stakes generation, not for anything you need to trust.
- **Best quality-per-dollar** — Claude Haiku 5.5 (✅ $0.10/$0.50, AA 43.4). The default answer for "good and cheap" in October 2026.
- **Best open-weights value** — GLM-5.3-Flash (✅ $0.15/$0.50, AA 41.8, MIT). DeepSeek V4 Flash (✅ $0.14/$0.28) if you want the absolute floor with open weights.
- **Fastest** — Mercury 2.5 (~675 tok/s independently measured, diffusion). Different architecture, shorter context (260K), quality unverified — best for real-time/streaming UX.
- **Fastest autoregressive** — Gemini 2.0 Flash (244 tok/s, ⚠️ $0.10/$0.40). Old but still the speed king under $0.15.
- **Long context, cheap** — Llama 4 Scout (10M tokens, ⚠️ $0.15/$0.40, open weights) or grok-4-fast (2M tokens, ✅ $0.20/$0.50).
- **Symmetric cheap pricing** — Ministral 3 3B/8B ($0.10/$0.10 and $0.15/$0.15, Apache 2.0). Output-heavy workloads love flat pricing.
- **Self-host** — Nemotron 3 Nano Omni (158 tok/s) or Gemma 4 27B (142 tok/s) if you have the GPUs; ~$0 marginal per-token cost.

## Rules of thumb

1. **Input price is the segment; output price is the bill.** Budget models are often output-heavy in price (Flash-Lite: $0.30 in / $2.50 out). Estimate your in/out mix before choosing.
2. **Tiered pricing bites.** Haiku 5.5 jumps to $0.50/$2.50 above 100K prompt tokens; MiniMax M3 doubles above 512K context. Read the features line.
3. **⚠️ means verify before you commit.** Unverified prices were single-sourced in the research pass — fine for shortlisting, re-check before signing anything.
4. **Off-peak discounts are real but disputed.** DeepSeek's ~50% off-peak cut is widely reported but the exact split is unconfirmed — don't budget on it.
5. **Diffusion ≠ autoregressive.** Mercury 2.5's tok/s is not comparable 1:1 with autoregressive models for quality-latency tradeoffs; treat it as a separate category (as this list does).
