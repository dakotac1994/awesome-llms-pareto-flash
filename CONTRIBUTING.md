# Contributing to Awesome Pareto-Flash LLMs

Thanks for helping keep this list accurate. Budget-tier prices move fast — corrections are the most valuable contribution.

## What belongs here

- A hosted model with **input price ≤ $0.50 per 1M tokens** that is **Pareto-optimal on quality-per-dollar** (see `docs/methodology.md` for the exact rule). If a model's Pareto status is unclear, say so in the PR.
- Open-weight models with no hosted per-token price go in `data/self-host.json`, not the main file.
- Announced-but-unshipped and preview-gated models are **not** entries.
- Retired or strictly dominated models are **not** entries; they go in `docs/status-changes.md` and the README's excluded table.
- Anything over $0.50 input belongs in the sister repo [awesome-llms-pareto-frontier](https://github.com/dakotac1994/awesome-llms-pareto-frontier).

## Adding an entry

1. Edit `data/pareto-flash.json` (hosted) or `data/self-host.json` (open-weight self-host) — add one object following the schema below.
2. Run `python3 scripts/generate_readme.py` to regenerate `README.md` — never hand-edit the generated sections.
3. Keep entries factual and neutral. No marketing copy, no comparisons in the entry text.

### Schema

```json
{
  "name": "Model Name",
  "vendor": "Lab Name",
  "url": "https://official-model-or-docs-page",
  "description": "One neutral sentence: what it is and what it's for.",
  "price_input_per_1m": "$0.10",
  "price_output_per_1m": "$0.50",
  "price_verified": true,
  "pricing_url": "https://official-pricing-page",
  "status": "active",
  "category": "budget",
  "features": ["1M-token context", "154 tok/s (Artificial Analysis)", "..."],
  "tokens_per_sec": 154,
  "speed_verified": true,
  "quality_score": 37.0,
  "quality_source": "AA Intelligence Index v4.3",
  "quality_verified": true,
  "open_weights": false,
  "value_tier": "S"
}
```

Field rules:

- `url` must be the vendor's official page (model announcement, docs, or product page).
- Prices are strings like `"$0.50"`. For tiered pricing, write the cheapest standard tier in the fields and both tiers in `features`. Self-host entries use `"self-host"`. **Never guess a price** — use `price_verified: false` and `pricing_url: ""`.
- `price_verified: true` **only** if the price is corroborated by ≥2 independent sources or read on the vendor's official pricing page. Read/corroboration date goes in the README entry (✅ verified YYYY-MM-DD).
- `tokens_per_sec`: independently measured output tok/s, or `null`. `speed_verified: true` only for independent measurements — never vendor claims.
- `quality_score`: number from one declared `quality_source` (`"AA Intelligence Index v4.3"`, `"swfte composite /100 (third-party)"`, vendor benchmarks labeled `"(vendor-reported)"`, or `"unverified"` with `null` score). Never mix sources in a comparison.
- `status`: `active` (GA), `commercial` (preview-gated / enterprise), `beta`/`deprecated` as needed.
- `value_tier`: `S` (on the efficient frontier), `A` (strong value / justified exception), `B` (thin data or niche).
- Keep `features` to 6 items max: context window, speed, quality, license, release date, pricing notes.

## Pricing changes

Update the price fields, flip `price_verified` per the rule above, and add a row to `docs/status-changes.md`. If a price cut pulls a model under the $0.50 cutoff, it becomes a candidate entry.

## Retirements / renames

Move the entry out of `data/*.json`, regenerate the README, and add a row to the excluded table in `README.md` (via the generator's static section) plus `docs/status-changes.md`.

## Checks

CI validates:
- Both JSON files parse; all fields present with the right types.
- No duplicate names across both files. (Sibling models from one lab may share an official page URL.)
- All `url` / `pricing_url` start with `https://`.
- `status` is one of `active`, `beta`, `deprecated`, `commercial`; `category` is `"budget"`.
- `price_verified` is a boolean; verified entries must have an https `pricing_url`, unverified entries leave it empty. Self-host entries use `"self-host"` prices with `price_verified: false`.
- `value_tier` is one of `S`, `A`, `B`; `tokens_per_sec` / `quality_score` are numbers or null.
- All Markdown links in `README.md`, `CONTRIBUTING.md`, and `docs/` resolve (lychee), ignoring known-blocked hosts.
