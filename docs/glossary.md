# Glossary

Terms used in this repo.

- **Pareto frontier** — the set of options where no other option is better on *every* axis. On a price-vs-quality plot, a model is on the frontier if nothing is both cheaper and better.
- **Budget segment** — the portion of the frontier at ≤ $0.50 per 1M input tokens. This repo's scope.
- **AA Intelligence Index** — Artificial Analysis's composite benchmark (v4.3, rebased Sept 2026). The preferred quality signal in this repo; not comparable to pre-Sept-2026 AA scores.
- **tok/s** — output tokens per second; the speed metric in this repo, independently measured where possible.
- **Quality-per-dollar** — quality score divided by input $/1M; the ranking metric of the value leaderboard.
- **Input / output pricing** — per-1M-token prices for prompt tokens vs generated tokens. Output is usually 2–5x input in the budget tier.
- **Peak / off-peak** — DeepSeek's time-of-day pricing (off-peak roughly half price); the exact split is currently disputed.
- **Diffusion LM** — non-autoregressive generation (e.g. Mercury 2.5, Celeris-1); generates tokens in parallel for ~10x the tok/s of autoregressive models, with different quality/latency tradeoffs.
- **MoE / active params** — Mixture-of-Experts models (e.g. 309B total / 15B active) route each token through a subset of parameters; active params drive inference cost.
- **Self-host** — running open-weight models on your own hardware; ~$0 marginal per-token cost, priced in GPUs instead.
- **Verified / unverified** — see [methodology.md](methodology.md): ✅ corroborated by ≥2 independent sources or an official page; ⚠️ single-sourced or disputed. Never guessed.
