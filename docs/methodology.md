# Methodology

How this list is built, what "budget segment" means, and how to read the numbers. Updated **October 2026**.

## The budget cutoff

A model belongs in this list only if its hosted API costs **≤ $0.50 per 1M input tokens** (standard tier, short context). The cutoff is not arbitrary: in the October 2026 landscape there is a natural gap — the next tier up starts at $0.75 (Gemini 3.8 Flash) and $1.00+ (Claude Haiku 4.5, Qwen 3.6 Plus). Everything at or under $0.50 is the commodity tier; everything above is covered by the sister repo [awesome-llms-pareto-frontier](https://github.com/dakotac1994/awesome-llms-pareto-frontier).

Tiered pricing (e.g. Claude Haiku 5.5's $0.10/$0.50 up to 100K prompt, $0.50/$2.50 above) is judged on the **cheapest standard tier**.

## The Pareto rule

Within the budget segment, a model is listed if it is **Pareto-optimal on quality-per-dollar**: no other listed model is both cheaper (input $/1M) *and* better-or-equal quality at the same time. Concretely:

1. Rank candidates by input price (ascending).
2. Walk up in price; a model makes the list only if its quality beats everything cheaper than it, *or* it is strictly cheaper than everything better than it.
3. Two deliberate exceptions, flagged in the entries:
   - **Speed outliers**: diffusion models (Mercury 2.5) live in a different speed band (~10x autoregressive). They are listed for speed, not quality-per-dollar.
   - **Self-host open weights** (`data/self-host.json`): no per-token price exists, so they cannot sit on a price frontier. They are listed separately because ~$0 marginal API cost is the ultimate budget play.

`value_tier` in the data is a coarse summary: **S** = on the efficient frontier (top quality-per-dollar), **A** = strong value or a justified exception, **B** = thin data or niche positioning.

## Quality: one source hierarchy

Quality scores are **never mixed across sources** in a ranking. The README's value leaderboard uses only one benchmark:

1. **AA Intelligence Index v4.3** (Artificial Analysis, Sept 2026 rebase) — preferred; the current 2026 composite standard.
2. **swfte composite /100** (third-party aggregation of MMLU Pro + HumanEval + MATH, cross-checked vs LMArena) — used where no AA score exists.
3. **Vendor-reported** (e.g. DeepSWE %) — labeled as such, `quality_verified: false`, never ranked.

`quality_verified: true` means the number comes from an independent third party. Vendor numbers are always unverified.

## Speed: measured, not claimed

`tokens_per_sec` is output tokens/sec from **independent measurement** (Artificial Analysis or the swfte aggregation) wherever available. Vendor-claimed figures are labeled in the entry text and the entry uses the independent figure (`speed_verified: true` = independently measured). Models with no independent measurement get `tokens_per_sec: null`.

## Verification policy

- `price_verified: true` — the price was corroborated by **≥2 independent sources** in the October 8, 2026 research pass, or read on the vendor's official pricing page.
- `price_verified: false` — single-sourced or disputed (e.g. DeepSeek V4.1 Flash's peak/off-peak split). These entries carry **no** `pricing_url` and show ⚠️ in the README.
- **Prices are never guessed.** If no usable price exists, the model is excluded (see below).

## Exclusions (October 2026)

- **Celeris-1** (diffusion, ~1,500 tok/s): no public per-token price — cannot be placed on a price frontier. Fastest model observed; excluded on the no-guessed-prices rule.
- **Gemini 3.8 Flash** ($0.75/$3.75), **Qwen 3.6 Plus** ($1.40/$5.60), **Claude Haiku 4.5** ($1.00/$5.00), **Kimi K2.6** ($0.73/$3.49): over the budget cutoff.
- **GPT-5.6 Luna, Grok 3 Mini, GPT-4o mini, Claude 3.5 Haiku, Llama 4 Maverick, Qwen 2.5 Coder 32B, Codestral**: superseded or strictly dominated on quality-per-dollar by a listed model.
- Announced-but-unshipped and preview-gated models are never entries.

## Refresh cadence

Prices move monthly in this tier (see the GPT-6 Sol/Luna 50% price cuts of Sept 2026). Treat every figure as a snapshot dated **2026-10-08**; the monthly link-check CI catches rot, and price changes go in `docs/status-changes.md`.
