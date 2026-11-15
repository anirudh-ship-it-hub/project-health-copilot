# Scope Guard

**A proposed extension of Dela, Deltek's AI, that tells a Vantagepoint project manager why a project is losing money and what to bill for it.**

Dela's policy review already checks timesheets against company policy. Scope Guard points the same pattern at the signed contract. It reads every timesheet note against the contract scope, flags work that falls outside it with the evidence and the clause, totals the unbilled value by cause, and drafts the additional services request. The project manager reviews every flag. Nothing is sent automatically.

- **Live demo (GitHub Pages):** https://anirudh-ship-it-hub.github.io/project-health-copilot/
- **Live demo with Claude classifying new notes:** https://claude.ai/artifact/5RtU6fhJoyAEdz1Jb44B2P
- **Thought process:** [docs/thinking.md](docs/thinking.md)
- **North star, success and kill metrics:** [docs/metrics.md](docs/metrics.md)
- **Research:** [docs/research.md](docs/research.md)
- **How it was built with AI:** [docs/ai-workflow.md](docs/ai-workflow.md)

Built by Anirudh Chennamaneni as part of an application for Product Manager, AI-First Products at Deltek. Not affiliated with or endorsed by Deltek. All project data is fictional.

---

## The problem

Architecture and engineering firms lose margin to scope creep: 73% name it the single greatest threat to project budgets, and out-of-scope cost is the metric they find hardest to track ([sources](docs/research.md#3-what-customers-say-hurts)).

Deltek's AI, Dela, already flags when a project is *spending ahead of earned revenue*. It says the margin is at risk. It does not say **why**, and it does not read timesheet notes, which is where staff write down the extra work a client asked for.

## What Scope Guard does

| Step | Who | Output |
| --- | --- | --- |
| 1. Read timesheet notes | Data | Note, phase, person, hours, rate |
| 2. Match each note to the contract | LLM | In scope, out of scope, or needs a check, with one clause and the quoted evidence |
| 3. Total the value | Code | Hours times billing rate, grouped by cause |
| 4. Decide and send | Project manager | Agree or override each call, then send the request |

In the demo project, it finds **$15,175 of out-of-scope work across six causes** (mostly an imaging suite the owner added after design development sign-off) and routes three vague notes to the PM to check.

## North star

**Monthly active scope reviewers**: the share of eligible PMs (with a fixed-fee project on Vantagepoint cloud) who act on at least one scope flag in a month. Deltek's own research says 70% of A&E firms use AI but only 38% see measurable impact, so the metric counts adoption that comes with value. Input metrics, guardrails, kill criteria and the rollout plan are in [docs/metrics.md](docs/metrics.md). The demo page fires the events these metrics need.

## Enhancement, not a new product

The data (timesheets, contracts), the user (the PM in Dela) and the buyer are all the same, so this belongs inside Dela Insights, next to policy review. The thought process also covers [why Deltek probably hasn't built it yet](docs/thinking.md#4-why-it-probably-doesnt-exist-yet) (weak notes, risk of client-facing errors, other priorities) and how the design answers each.

## Why this function

I started with five ideas and dropped four because Deltek already ships or has announced them (overrun alerts, AI proposals, conversational time entry) or because an LLM was not the right tool (resource planning). The full reasoning, metrics, risks and what I'd test first are in [docs/thinking.md](docs/thinking.md).

## Repo layout

```
index.html                 the app (GitHub Pages)
dist/artifact.html         same app, published as a Claude artifact with live AI
src/app.html               app source; data is inlined by the build
data/project.json          fictional contract scope, phases and timesheet notes
data/classifications.json  LLM output for each note
data/gold_labels.json      PM-reviewed labels used for evaluation
prompts/                   the classification and change request prompts
scripts/build.py           builds index.html and dist/artifact.html
scripts/classify.py        re-runs classification through the Anthropic API, with validation
scripts/eval.py            precision and recall of out-of-scope flags against PM labels
docs/                      research, thought process, metrics, AI workflow
```

## Run it

```bash
python3 scripts/build.py      # rebuild the page from src and data
python3 scripts/eval.py       # score the saved classifications (no API key needed)

pip install anthropic
export ANTHROPIC_API_KEY=...
python3 scripts/classify.py --check   # re-run the LLM and compare with the saved results
```

Open `index.html` in a browser. The "Try it" box classifies new notes live only when the page runs as a Claude artifact; on GitHub Pages it shows the prompt instead.

## Honest limits

- The classifications in `data/` were produced with Claude in the build session using `prompts/classify_entries.md`. `scripts/classify.py` is the repeatable path but was not run here, since no API key was available.
- The eval uses illustrative gold labels, so its numbers show the method, not a measured accuracy.
- The biggest open question is whether real timesheet notes are specific enough. That is the first thing I would test with pilot firms.
