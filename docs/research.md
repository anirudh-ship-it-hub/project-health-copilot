# Research: where AI can create value for Deltek customers

Done in November 2026, before writing any code. Every figure below links to the page it came from.

## 1. Who Deltek serves

Deltek sells ERP, project management and business development software to **project-based businesses**: government contractors (Costpoint, GovWin IQ), architecture and engineering firms (Vantagepoint, Ajera), and professional services (Maconomy, Replicon). It is owned by Roper Technologies.

What these firms have in common: revenue is earned project by project, so margin is won or lost in how well each project's scope, hours and billing are controlled.

## 2. What Deltek already ships in AI

**Dela** is Deltek's AI brand, described as an "AI orchestrator" that "directs a team of AI agents that anticipate issues, flag risks, and take action before problems become rework." ([Dela product page](https://www.deltek.com/en/products/platform/dela))

In Vantagepoint today, Dela gives project managers ([Dela for Vantagepoint PMs, Aug 2026](https://www.deltek.com/resources/articles/dela-vantagepoint-project-managers/)):

| Capability | What it does |
| --- | --- |
| Ask Dela | Natural-language questions over project data; summarises contracts |
| Conversational time entry | Logs hours from a sentence, confirms before posting |
| Dela Insights | Proactive alerts: earned revenue ahead of invoicing, **spending ahead of earned revenue**, earned ahead of spending, expense policy violations, timesheet anomalies (missing hours, odd patterns, entries that don't fit the project structure) |
| Smart Summaries | One-click project and client briefings |
| Image capture | Business cards, receipts and invoices into records |
| Email drafting | Status updates, AR follow-ups, client emails |

Announced at ProjectCon, November 2025 ([press release](https://www.deltek.com/en/about/media-center/press-releases/2025/deltek-unveils-intelligent-platform-innovations)):
- **Deltek Proposals**: solicitation analysis, compliance mapping, first drafts. Deltek projects a 60 to 70% cut in proposal time.
- **PPM Enterprise Risk**: organisation-wide risk visibility.
- **Agentic Financial Close**: AI reconciliation with human oversight.

**Implication:** a generic "project overrun alert" or "proposal writer" would duplicate what Deltek already has or has announced.

## 3. What customers say hurts

From Deltek's own Clarity studies, May 2026, about 1,800 respondents ([press release](https://www.deltek.com/en/about/media-center/press-releases/2026/the-latest-deltek-clarity-industry-studies-highlight-ai-challenges)):
- A&E firms: utilisation fell to just under 60% and operating profit to 16.7%.
- A&E AI adoption rose from 53% to 70%, but only 38% report measurable positive impact. The top challenge is **deciding where to apply AI (62%)**.
- GovCon: 45% are unclear on AI's return; top concerns include inaccurate forecasts (29%) and difficulty validating AI insights (26%).

From A&E industry surveys:
- 73% of firms name **scope creep** as the single greatest threat to project budgets; 56% report overruns on at least 10% of projects; 40% don't monitor project profitability in real time. ([Factor A/E 2026 benchmark, via PM Global](https://news.pm-global.co.uk/2026/06/ae-firms-are-busy-growing-and-embracing-ai-but-many-still-lack-visibility-into-project-performance/?print=pdf). Factor is a software vendor, so read with that in mind.)
- **Out-of-scope costs** are "the single most difficult metric to keep on top of"; 36% of practices are not confident they recover all fees owed; 32% only spot overruns through manual review. ([RIBAJ and Hyphen Digital survey, July 2026](https://www.ribaj.com/intelligence/digital-tech-in-architecture-survey-results/), 230+ practices)

## 4. The gap

| What exists | What's missing |
| --- | --- |
| Dela flags that a project is spending ahead of earned revenue | **Why** it is, in terms a client conversation can use |
| Dela checks timesheet hours for anomalies | Nothing reads the **timesheet notes**, where staff write what they actually did and who asked |
| Vantagepoint has change order tools | Nothing **finds** the change orders a PM should be raising |

Scope creep is the top named threat, out-of-scope cost is the hardest metric to track, and the evidence for it sits in free-text notes that no current Dela feature reads. That is a natural language problem with a direct dollar value, which is where an LLM earns its place.

## 5. Competitors

A&E practice management alternatives include BQE CORE, Unanet AE, Monograph and Factor ([Monograph's competitor list](https://monograph.com/blog/deltek-competitors), [Rocketlane's list](https://rocketlane.com/blogs/deltek-alternatives)). Monograph and Factor market heavily on real-time project profitability. None of the public material reviewed describes reading timesheet notes against contract scope.

## 6. Limits of this research

- Done from public pages only. I have not used Vantagepoint.
- Survey figures come partly from vendors with an interest in the problem.
- Whether firms write useful timesheet notes is the biggest assumption. See [thinking.md](thinking.md).
