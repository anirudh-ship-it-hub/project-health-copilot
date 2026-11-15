# Metrics: north star, inputs, guardrails and kill criteria

All targets and thresholds here are my proposals for a pilot. They are not Deltek figures.

## The problem the north star has to answer

Deltek's 2026 Clarity study: 70% of A&E firms use AI, but only 38% report measurable positive impact, and the top challenge is knowing where to apply it ([source](https://www.deltek.com/en/about/media-center/press-releases/2026/the-latest-deltek-clarity-industry-studies-highlight-ai-challenges)). Roper says AI monetisation comes through the move to cloud, and adoption pace is the key unknown ([Q2 2026 call](https://vectorshift.ai/research/companies/roper/earnings/2026-q2)).

So the north star has to measure adoption that comes with value, not views.

## North star

**Monthly active scope reviewers**: the share of eligible PMs who act on at least one scope flag in a month.

- **Act** = agree with a flag, override it, or send a change request.
- **Eligible** = PMs with at least one fixed-fee project on Vantagepoint cloud.
- **Pilot target**: 40% by week 8 of the PM-facing phase.
- **Why**: acting on a flag means the PM used Dela *and* got something worth money from it. Counting views would reward noise.

**Halo metric**: weekly active Dela users among PMs, pilot firms against matched non-pilot firms. Scope flags give PMs a money reason to open Dela every week, which should lift use of everything else in it.

## Input metrics (what moves the north star)

| Metric | Target | Why it matters |
| --- | --- | --- |
| Notes specific enough to classify | 60%+ | Without good notes there is nothing to flag |
| Eligible projects with scope clauses extracted | 80%+ | Without scope there is nothing to compare against |
| Flag precision (PM agrees with out-of-scope call) | 80%+ | Low precision trains PMs to ignore the panel |
| Days from out-of-scope note to flag | 7 or less | Scope creep is cheapest to raise early |
| Flags acted on within 7 days | 50%+ | The direct driver of the north star |

## Value metrics (is it worth it)

| Metric | What good looks like |
| --- | --- |
| Out-of-scope dollars found per project per month | Rises at first, then levels off as PMs raise changes earlier |
| Share of found dollars put in a sent request | Rising |
| Share of requested dollars the client approves | 60%+ |
| Recovered fees per firm per quarter | Above what the firm would pay for it, as an add-on or as part of the cloud uplift |

## Guardrails

| Metric | Limit |
| --- | --- |
| Wrong flags inside a sent request | 0. Each one gets a written review |
| Flags dismissed without opening | Under 30% |
| PMs who mute the insight | Under 10% |
| Time on "needs a check" follow-ups, per PM per week | Under 15 minutes |
| Requests the client rejects as actually in scope | Under 20% |

## Kill criteria (agreed before the pilot starts)

Pilot: 5 firms on Vantagepoint cloud, about 40 PMs, 8 weeks PM-facing.

| If this happens | By when | Then |
| --- | --- | --- |
| Fewer than 30% of notes are specific enough, even with the time-entry question on | 4 weeks after the question ships | Kill the agent. Keep the time-entry question as its own feature |
| Flag precision stays under 65% | After 2 prompt iterations | Kill. The model can't be trusted with this |
| Fewer than 20% of flags are acted on | Week 6 | Pivot from live alerts to a monthly billing review report |
| Recovered fees per firm are below what we'd charge | End of pilot | Rethink: bundle into cloud rather than sell separately |
| A wrong flag reaches a client and causes a dispute | Any time | Pause and review before turning it back on |

Writing these down first matters more than the exact numbers: it stops a pilot from drifting on because nobody wants to call it.

## Rollout

| Phase | Weeks | What happens | Exit check |
| --- | --- | --- | --- |
| 0. Data audit | 0 to 2 | Pull a month of notes from 5 cloud firms; measure specificity and whether scope is stored | Note quality at or near 60%, or a plan to get there |
| 1. Shadow mode | 3 to 6 | Flags generated, seen only by the team; PMs label a sample | Precision 80%+ |
| 2. PM-facing pilot | 7 to 14 | Flags in Dela Insights plus a weekly digest; time-entry question on | North star 40%, no guardrail breached |
| 3. Cloud release | After | Fixed-fee projects on Vantagepoint cloud; then statement-of-work checks in Costpoint | Sustained north star, value above price |

## Adoption levers

1. **No new place to go.** Flags sit in the Dela Insights panel PMs already open.
2. **A weekly digest** with the top cause and its dollar value, because PMs act on money.
3. **One click to agree.** Reviewing a flag should take seconds, with the evidence on screen.
4. **The draft request is the value moment.** It turns an uncomfortable client conversation into a ready letter.
5. **A firm-level view for principals.** Owners care about recovered fees, and they push PMs to use it.

## Instrumentation

The prototype fires the events these metrics need. Open the demo, agree with or override a flag, and the event log at the bottom of the page shows it:

| Event | Feeds |
| --- | --- |
| `flag_agreed`, `flag_overridden` | North star, flag precision |
| `request_sent` | North star, share of found dollars requested |
| `cause_toggled` | Which causes PMs choose not to bill |
| `flags_filtered` | How PMs work the list |
| `note_classified_live`, `request_rewritten` | Use of the AI-only features |
