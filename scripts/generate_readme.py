#!/usr/bin/env python3
"""Generate README.md for awesome-llms-pareto-flash from data/*.json.

Usage: python3 scripts/generate_readme.py
Writes README.md in the repo root.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(name):
    return json.loads((DATA / name).read_text())


def price_str(e):
    if e["price_input_per_1m"] == "self-host":
        return "self-host"
    badge = "\u2705" if e["price_verified"] else "\u26a0\ufe0f"
    s = f'{badge} **{e["price_input_per_1m"]} in / {e["price_output_per_1m"]} out**'
    if not e["price_verified"]:
        s += " (unverified)"
    return s


def pricing_link(e):
    if e["price_verified"] and e["pricing_url"]:
        host = re.sub(r"^https?://(www\.)?", "", e["pricing_url"]).split("/")[0]
        return f' Pricing: [{host}]({e["pricing_url"]}).'
    return ""


def quality_str(e):
    if e["quality_score"] is None:
        return "quality unverified"
    src = e["quality_source"]
    if src.startswith("AA Intelligence Index"):
        return f"AA Index {e['quality_score']}"
    if src.startswith("swfte"):
        return f"quality {e['quality_score']:.0f}/100"
    return f"{src}: {e['quality_score']}"


def speed_str(e):
    if e["tokens_per_sec"] is None:
        return ""
    v = f"{e['tokens_per_sec']:.0f} tok/s"
    if not e["speed_verified"]:
        v += " (unverified)"
    return v


def entry_line(e):
    bits = [f'[{e["name"]}]({e["url"]})', "\u2014", price_str(e)]
    feats = [f for f in e["features"]]
    extra = "; ".join(feats)
    line = f"- {' '.join(bits)}. {e['description']}"
    if extra:
        line += f" {extra}."
    line += pricing_link(e)
    return line


VENDOR_ORDER = [
    "Anthropic", "OpenAI", "Google DeepMind", "xAI", "DeepSeek",
    "Alibaba", "Zhipu AI", "Xiaomi", "Mistral AI", "Meta",
    "Amazon", "MiniMax", "Inception Labs",
]


def anchor(name):
    # GitHub heading-anchor algorithm: lowercase, drop punctuation except
    # hyphens/underscores, spaces -> hyphens.
    return re.sub(r"\s+", "-", re.sub(r"[^a-z0-9 _-]", "", name.lower()))


def main():
    hosted = load("pareto-flash.json")
    selfhost = load("self-host.json")

    by_vendor = {}
    for e in hosted:
        by_vendor.setdefault(e["vendor"], []).append(e)
    vendors = [v for v in VENDOR_ORDER if v in by_vendor] + sorted(
        set(by_vendor) - set(VENDOR_ORDER)
    )

    # Value leaderboard: AA-scored hosted entries by score / input-price ratio.
    def in_price(e):
        try:
            return float(e["price_input_per_1m"].lstrip("$"))
        except ValueError:
            return None

    value_rows = []
    for e in hosted:
        p = in_price(e)
        if e["quality_score"] is not None and p and e["quality_source"].startswith("AA"):
            value_rows.append((e["quality_score"] / p, e))
    value_rows.sort(key=lambda r: -r[0])

    # Speed leaderboard: hosted entries with measured tok/s.
    speed_rows = sorted(
        (e for e in hosted if e["tokens_per_sec"]),
        key=lambda e: -e["tokens_per_sec"],
    )

    L = []
    A = L.append

    A("# Awesome Pareto-Flash LLMs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    A("> The **budget segment** of the October 2026 LLM Pareto frontier — cheap models that are Pareto-optimal on price vs quality (and speed). Updated **October 2026**.\n")
    A("This list covers only the budget segment: every hosted model here costs **\u2264 $0.50 per 1M input tokens**, and each entry is non-dominated on quality-per-dollar among cheap models (see [docs/methodology.md](docs/methodology.md) for the exact rule). For the full intelligence-vs-price frontier across **all** tiers, see the sister repo [awesome-llms-pareto-frontier](https://github.com/dakotac1994/awesome-llms-pareto-frontier).\n")
    A("The October 2026 story: the budget tier is no longer a quality desert. **Claude Haiku 5.5** (Oct 7) scores AA Index 43.4 at $0.10/$0.50 \u2014 frontier-adjacent intelligence at commodity prices. Open-weight efficiency models (**GLM-5.3-Flash**, **DeepSeek V4 Flash**, **MiMo-V2.6-Flash**, **Qwen3.8-Flash**) cluster at $0.14\u2013$0.16 input with AA scores in the high 30s to low 40s. And diffusion models (**Mercury 2.5**) run an order of magnitude faster than anything autoregressive in the segment.\n")
    A("**Pricing confidence:** every price below is stamped \u2705 **verified 2026-10-08** (corroborated by \u22652 independent sources in the research pass, or read on an official pricing page) or \u26a0\ufe0f **unverified** (single-sourced or disputed). **Prices are never guessed.** Machine-readable records live in [`data/pareto-flash.json`](data/pareto-flash.json) (hosted APIs) and [`data/self-host.json`](data/self-host.json) (open-weight self-host), each carrying `price_verified`, `speed_verified`, and `quality_verified` booleans.\n")

    A("## 2026 Highlights\n")
    A("- **Claude Haiku 5.5** (Anthropic, Oct 7): AA Index 43.4 at \u2705 $0.10/$0.50 \u2014 the best quality-per-dollar in the survey by a wide margin.")
    A("- **GPT-6 Luna** (OpenAI, Sept 22): AA Index 37 at \u2705 $0.10/$0.50, 154 tok/s \u2014 the frontier-family price floor.")
    A("- **GLM-5.3-Flash** (Z.ai, Aug): AA Index 41.8 at \u2705 $0.15/$0.50, MIT open weights \u2014 the open-weight value pick.")
    A("- **DeepSeek V4.1 Flash** (Sept 10): 217 tok/s with AA Index 39.5; peak/off-peak pricing split still disputed (\u26a0\ufe0f).")
    A("- **Mercury 2.5** (Inception Labs, ~Oct): diffusion LM at ~675 tok/s independently measured \u2014 a different speed band entirely.")
    A("- **Price floor:** Nova Micro at \u26a0\ufe0f $0.035/$0.14 \u2014 cheapest API in the survey, quality unverified.")
    A("- **Self-host wave:** Nemotron 3 Nano Omni, Gemma 4 27B, Qwen3.8 27B \u2014 open weights you can run yourself at ~$0 marginal API cost.\n")

    A("## Contents\n")
    A("- [Budget models](#budget-models)")
    for v in vendors:
        A(f"  - [{v}](#{anchor(v)})")
    A("- [Value leaderboard (quality per dollar)](#value-leaderboard-quality-per-dollar)")
    A("- [Speed leaderboard](#speed-leaderboard)")
    A("- [Self-host open weights](#self-host-open-weights)")
    A("- [Excluded & why](#excluded--why)")
    A("- [Guides](#guides)")
    A("- [Related repositories](#related-repositories)")
    A("- [Contributing](#contributing)")
    A("- [License](#license)\n")
    A("---\n")

    A("## Budget models\n")
    A("Hosted APIs at \u2264 $0.50/1M input tokens, Pareto-optimal on quality-per-dollar. `value_tier` S = top of the frontier, A = strong value, B = thin data or niche.\n")
    for v in vendors:
        A(f"### {v}\n")
        for e in by_vendor[v]:
            bits = [quality_str(e)]
            sp = speed_str(e)
            if sp:
                bits.append(sp)
            if e["open_weights"]:
                bits.append("open weights")
            bits.append(f'value tier {e["value_tier"]}')
            A(f"{entry_line(e)} [{'; '.join(bits)}].")
        A("")

    A("---\n")
    A("## Value leaderboard (quality per dollar)\n")
    A("Hosted entries scored on the AA Intelligence Index v4.3, ranked by index points per $1 of input-token price. Single-benchmark ranking \u2014 read [docs/methodology.md](docs/methodology.md) before comparing across sources.\n")
    A("| # | Model | AA Index | $/1M in | Index per $ |")
    A("|---|---|---|---|---|")
    for i, (ratio, e) in enumerate(value_rows, 1):
        A(f"| {i} | [{e['name']}]({e['url']}) | {e['quality_score']} | {e['price_input_per_1m']} | {ratio:.0f} |")
    A("")

    A("## Speed leaderboard\n")
    A("Independently measured output tokens/sec (Artificial Analysis / swfte aggregation). Vendor-claimed figures are labeled in the entries.\n")
    A("| # | Model | tok/s | $/1M in | Architecture |")
    A("|---|---|---|---|---|")
    for i, e in enumerate(speed_rows, 1):
        arch = "diffusion" if "Diffusion" in " ".join(e["features"]) else "autoregressive"
        A(f"| {i} | [{e['name']}]({e['url']}) | {e['tokens_per_sec']:.0f} | {e['price_input_per_1m']} | {arch} |")
    A("")

    A("---\n")
    A("## Self-host open weights\n")
    A("The budget models you can download and run yourself \u2014 ~$0 marginal API cost, priced in hardware instead of tokens. Full records in [`data/self-host.json`](data/self-host.json).\n")
    A("| Model | Speed | Quality | License note |")
    A("|---|---|---|---|")
    for e in selfhost:
        sp = speed_str(e) or "\u2014"
        q = quality_str(e)
        lic = "open weights"
        A(f"| [{e['name']}]({e['url']}) | {sp} | {q} | {lic} |")
    A("")

    A("---\n")
    A("## Excluded & why\n")
    A("Pareto lists are defined by what they leave out. As of October 2026:\n")
    A("| Model | Why excluded |")
    A("|---|---|")
    A("| Gemini 3.8 Flash ($0.75/$3.75) | Over the $0.50 budget cutoff \u2014 the natural step-up reference |")
    A("| Qwen 3.6 Plus ($1.40/$5.60), Claude Haiku 4.5 ($1/$5), Kimi K2.6 ($0.73/$3.49) | Over the budget cutoff |")
    A("| Celeris-1 (diffusion, ~1,500 tok/s) | No public per-token price \u2014 cannot place on a price frontier |")
    A("| GPT-5.6 Luna, Grok 3 Mini, GPT-4o mini, Claude 3.5 Haiku, Llama 4 Maverick, Qwen 2.5 Coder 32B, Codestral | Superseded or strictly dominated on quality-per-dollar by a listed model |")
    A("| GPT-6 Sol ($2/$10), Gemini 3.6 Flash ($0.75/$3.75) | Covered by the full-frontier sister repo |")
    A("")
    A("Full exclusion log and the cutoff rationale: [docs/methodology.md](docs/methodology.md).\n")

    A("## Guides\n")
    A("- [Methodology](docs/methodology.md) \u2014 the budget cutoff, the Pareto rule, and how verification works")
    A("- [Choosing a budget model](docs/choosing-a-budget-model.md) \u2014 decision guide by workload")
    A("- [Glossary](docs/glossary.md) \u2014 terms used in this repo")
    A("- [Status changes](docs/status-changes.md) \u2014 retirements, renames, pricing changes\n")

    A("## Related repositories\n")
    A("- [awesome-llms-pareto-frontier](https://github.com/dakotac1994/awesome-llms-pareto-frontier) \u2014 **sister repo: the full intelligence-vs-price Pareto frontier across all tiers (this repo is its budget segment)**.")
    A("- [awesome-flash-llms](https://github.com/dakotac1994/awesome-flash-llms) \u2014 sibling list: cost-performance Flash-class LLMs and their $/1M-token pricing.")
    A("- [awesome-fast-llms](https://github.com/dakotac1994/awesome-fast-llms) \u2014 sibling list: inference-speed LLMs, providers, engines, and optimization techniques.")
    A("- [awesome-flagship-llms](https://github.com/dakotac1994/awesome-flagship-llms) \u2014 sibling list: the single most capable model from every major AI lab.")
    A("- [awesome-free-llms](https://github.com/dakotac1994/awesome-free-llms) \u2014 sibling list: free LLM API tiers, free chat apps, and open-weight local models.\n")

    A("## Contributing\n")
    A("See [CONTRIBUTING.md](CONTRIBUTING.md). One entry = one model; the budget cutoff is $0.50/1M input tokens; prices are stamped with their verification date and never guessed.\n")
    A("## License\n")
    A("[MIT](LICENSE) \u00a9 2026 dakotac1994\n")

    (ROOT / "README.md").write_text("\n".join(L))
    print(f"Wrote README.md ({len(L)} lines)")


if __name__ == "__main__":
    main()
