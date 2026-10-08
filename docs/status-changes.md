# Status Changes

Retirements, renames, and pricing changes affecting the budget segment. Newest first.

## 2026-10-08 — Baseline (list created)

Initial survey of the October 2026 budget segment (≤ $0.50/1M input). Notable state at launch:

- **New:** Claude Haiku 5.5 (Oct 7, 2026) — resets the quality-per-dollar bar at AA 43.4 / $0.10.
- **New:** Mercury 2.5 (~Oct 2026) — first diffusion model in the segment; launch pricing $0.04/$0.15.
- **Disputed:** DeepSeek V4.1 Flash peak/off-peak price split — sources disagree; listed at peak prices, flagged unverified.
- **Superseded (excluded):** GPT-5.6 Luna → GPT-6 Luna; Claude 3.5 Haiku → Haiku 4.5/5.5; Grok 3 Mini → grok-4-fast line.
- **Dominated (excluded):** GPT-4o mini, Llama 4 Maverick, Qwen 2.5 Coder 32B, Codestral — beaten on quality-per-dollar by listed models.
- **Price-watched:** Gemini 3.8 Flash ($0.75/$3.75) and Gemini 4 Argon sit just above the cutoff; a price cut would pull them into scope.

## How to log a change

One row per event: date, model, what changed (retired / renamed / repriced with old → new), and the source. Remove retired models from `data/*.json` and `README.md` (regenerate via `scripts/generate_readme.py`).
