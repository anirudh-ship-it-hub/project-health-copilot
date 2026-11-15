# Thought process

How I went from the job description to this prototype, including the options I dropped.

## 1. Start from the job, not the tech

The role asks three questions: can AI make PMs more productive, can it create a better experience than traditional software, and can it unlock new business value. It also asks for "measurable customer value" and "frameworks for responsible AI usage and evaluation."

So my filter for an idea was:
1. A real, frequent pain for Deltek customers, backed by evidence.
2. Something Deltek does not already ship or announce.
3. An LLM is the right tool, not just a possible one.
4. The value can be counted in dollars.
5. A person stays in control of anything that leaves the firm.

## 2. Options I considered

| Idea | Why I dropped it or kept it |
| --- | --- |
| Project overrun early warning | Dela Insights already flags spending ahead of earned revenue, and PPM Enterprise Risk is announced. Duplicate. |
| AI proposal writer for GovCon | Deltek Proposals is announced with a 60 to 70% time-saving claim. Duplicate. |
| Resource planning assistant | Real pain (70% of A&E firms plan in spreadsheets) but mostly an optimisation problem. An LLM adds little over good scheduling logic. |
| Timesheet auto-fill | Dela already does conversational time entry. |
| **Scope Guard: read timesheet notes against contract scope** | Kept. Scope creep is the top named budget threat, the evidence is in free text nobody reads, and the output (a change request) is worth real money. |

## 3. Enhancement, not a new product

A new product only makes sense when the data, the user or the buyer is different. Here none of them are: the timesheets and contracts are already in Vantagepoint, the user is the PM who already opens Dela, and the buyer is the same firm. So Scope Guard is an extension of what Dela already does.

The closest existing feature is **Dela policy review** (Vantagepoint, August 2026), which checks timesheets against company policy and flags exceptions to approvers ([release](https://www.deltek.com/resources/articles/vantagepoint-dela-insights-2026-3/)). Scope Guard is the same pattern pointed at the signed contract. It also builds on Dela Insights' "spending ahead of earned revenue" alert by explaining the why.

## 4. Why it probably doesn't exist yet

It's the obvious next step, so I asked why Deltek might not have built it before assuming they missed it. Public material shows no scope or change-order AI, and Deltek's own [Scope Creep Survival Guide](https://www.deltek.com/resources/articles/scope-creep-architecture-projects/) gives only process advice. So they know the pain.

| Type | Hypothesis | Likelihood | How the design answers it |
| --- | --- | --- | --- |
| Trade-off | Weak data: notes are vague or optional, scope sits in PDFs | Highest | Phase 0 data audit; Dela asks "who asked for this?" at time entry; scope clauses from Dela's contract summaries |
| Trade-off | Risk of a wrong flag reaching a client | High | Internal only, like policy review; evidence on every call; a person sends anything external |
| Focus | Proposals and month-end close help every customer first | High | Start narrow: fixed-fee projects on Vantagepoint cloud |
| Focus | Only matters on fixed-fee work | Medium | That is the launch segment, not a flaw |
| Unintended | Crosses timesheet, billing and Dela teams, so no single owner | Medium | Hard to see from outside; worth asking in the interview |
| Unintended | Nobody thought of it | Low | Their own scope creep guide shows they know the problem |

The question I'd ask the team: "Policy review checks timesheets against company policy. Has the team considered checking them against the contract, and was it the data or the risk that held it back?"

## 5. Why this is an LLM problem

The signal is in sentences like "Client asked to see a third layout option after SD sign-off." Rules on hours or codes cannot see that. Keyword search breaks on phrasing. An LLM can read the note, compare it with the contract wording, and say which clause it falls outside and why.

But not everything should be AI:

| Step | Who does it | Why |
| --- | --- | --- |
| Read notes, match to clauses, quote evidence | LLM | Language understanding |
| Hours times rate, totals by cause | Plain code | Must be exact and auditable |
| Decide what goes to the client | Project manager | Client relationship, judgement, liability |
| Write the request | Template first, LLM rewrite optional | The numbers come from code; the LLM only changes the wording |

This mirrors what I did at Deloitte on predictive maintenance: the model predicted failures, and I wrote the rules that decided when a prediction became a work order. Here, the model reads notes, and code plus the PM decide when a flag becomes a change order.

## 6. Design choices in the prototype

- **Three labels, not two.** "Needs a check" is a first-class outcome. When a note is vague ("Misc. revisions", 11 hours), the honest answer is to ask the person who wrote it, not to guess.
- **Every call shows its evidence.** The exact words from the note are highlighted and the clause is one hover away. A PM can verify a flag in seconds, which is what builds trust. Deltek's own survey says 26% of GovCon firms struggle to validate AI insights.
- **Grouped by cause, not by note.** Clients agree to "the imaging suite you added," not to entry T14. Grouping by driver also tells the PM the story behind the overrun.
- **Overrides are data.** Every time a PM changes a call, that becomes a labelled example for the eval set.
- **Positioned next to Dela, not against it.** The page shows what Dela already flags (margin at risk) and what Scope Guard adds (why, and what to bill).

## 7. How I would measure it

North star: **monthly active scope reviewers**, the share of eligible PMs who act on at least one scope flag in a month. It measures adoption that comes with value, which is Deltek's real problem: 70% of A&E firms use AI but only 38% see measurable impact. Inputs, value metrics, guardrails, kill criteria and the rollout are in [metrics.md](metrics.md).

`scripts/eval.py` shows the evaluation method on the demo data: precision and recall for out-of-scope flags against PM-reviewed labels, with "needs a check" counted as routed to a human. The gold labels here are illustrative, so the numbers show the method, not a claim of accuracy.

## 8. Risks and what I would test first

1. **Do staff write useful notes?** The whole idea depends on it. First test: pull a month of real timesheet notes from 3 to 5 pilot firms and count how many are specific enough to classify. If most say "design work," the first feature is a better note prompt at time entry, which Dela's conversational time entry could ask for.
2. **Is the contract scope in the system?** If scope lives only in a signed PDF, Dela's existing contract summarisation could extract the clauses.
3. **Will PMs act on it?** Raising extra fees is uncomfortable. The draft request is written to make that conversation easier, and the metric that matters is approved change orders, not flags.
4. **Privacy.** Timesheet notes can mention people and clients. Deltek already commits that GenAI partners can't train on customer data; this feature should sit under the same controls.

## 9. What I would build next

- Run weekly, and alert the PM the first time a new cause appears, not at month end.
- Read client emails and meeting notes as a second source of evidence.
- For GovCon in Costpoint: the same idea checks charged work against the contract's statement of work, which also protects against unallowable costs in audits.
