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

## 3. Why this is an LLM problem

The signal is in sentences like "Client asked to see a third layout option after SD sign-off." Rules on hours or codes cannot see that. Keyword search breaks on phrasing. An LLM can read the note, compare it with the contract wording, and say which clause it falls outside and why.

But not everything should be AI:

| Step | Who does it | Why |
| --- | --- | --- |
| Read notes, match to clauses, quote evidence | LLM | Language understanding |
| Hours times rate, totals by cause | Plain code | Must be exact and auditable |
| Decide what goes to the client | Project manager | Client relationship, judgement, liability |
| Write the request | Template first, LLM rewrite optional | The numbers come from code; the LLM only changes the wording |

This mirrors what I did at Deloitte on predictive maintenance: the model predicted failures, and I wrote the rules that decided when a prediction became a work order. Here, the model reads notes, and code plus the PM decide when a flag becomes a change order.

## 4. Design choices in the prototype

- **Three labels, not two.** "Needs a check" is a first-class outcome. When a note is vague ("Misc. revisions", 11 hours), the honest answer is to ask the person who wrote it, not to guess.
- **Every call shows its evidence.** The exact words from the note are highlighted and the clause is one hover away. A PM can verify a flag in seconds, which is what builds trust. Deltek's own survey says 26% of GovCon firms struggle to validate AI insights.
- **Grouped by cause, not by note.** Clients agree to "the imaging suite you added," not to entry T14. Grouping by driver also tells the PM the story behind the overrun.
- **Overrides are data.** Every time a PM changes a call, that becomes a labelled example for the eval set.
- **Positioned next to Dela, not against it.** The page shows what Dela already flags (margin at risk) and what Scope Guard adds (why, and what to bill).

## 5. How I would measure it

| Metric | Why it matters |
| --- | --- |
| Out-of-scope dollars found per project per month | The value claim |
| Share of found dollars that become approved change orders | Whether flags turn into revenue, not just noise |
| Precision of "out of scope" flags, from PM overrides | If PMs keep overriding, they stop opening it |
| Time from first out-of-scope note to change request sent | Scope creep is cheapest to raise early |
| Weekly active PMs | Adoption |

Guardrails: wrong flags that reach a client (target zero, since the PM reviews everything), and staff time spent on "needs a check" follow-ups.

`scripts/eval.py` shows the evaluation method on the demo data: precision and recall for out-of-scope flags against PM-reviewed labels, with "needs a check" counted as routed to a human. The gold labels here are illustrative, so the numbers show the method, not a claim of accuracy.

## 6. Risks and what I would test first

1. **Do staff write useful notes?** The whole idea depends on it. First test: pull a month of real timesheet notes from 3 to 5 pilot firms and count how many are specific enough to classify. If most say "design work," the first feature is a better note prompt at time entry, which Dela's conversational time entry could ask for.
2. **Is the contract scope in the system?** If scope lives only in a signed PDF, Dela's existing contract summarisation could extract the clauses.
3. **Will PMs act on it?** Raising extra fees is uncomfortable. The draft request is written to make that conversation easier, and the metric that matters is approved change orders, not flags.
4. **Privacy.** Timesheet notes can mention people and clients. Deltek already commits that GenAI partners can't train on customer data; this feature should sit under the same controls.

## 7. What I would build next

- Run weekly, and alert the PM the first time a new cause appears, not at month end.
- Read client emails and meeting notes as a second source of evidence.
- For GovCon in Costpoint: the same idea checks charged work against the contract's statement of work, which also protects against unallowable costs in audits.
