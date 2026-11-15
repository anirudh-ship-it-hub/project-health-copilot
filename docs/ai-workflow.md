# How this was built with AI

The application asks for the prompts and workflow used to respond to it. This is that record.

## Tools

| Tool | What I used it for here |
| --- | --- |
| Claude (claude.ai, with web search) | Research on Deltek, its AI products and customer pain; pressure-testing ideas |
| Claude Code | Writing the app, data, prompts, scripts and docs; running builds and checks; pushing to GitHub |
| Claude artifacts | Publishing the live demo, with Claude classifying new notes inside the page |
| Playwright (through Claude Code) | Screenshots at desktop and phone width to check the layout |

## Workflow

1. **Brief.** I shared screenshots of the job post and asked for complete research, a prototype of one function, a GitHub repo and clear documentation of the thinking.
2. **Research before ideas.** Claude searched Deltek's product pages, its Dela AI pages, the 2025 ProjectCon announcements and the 2026 Clarity studies, plus independent A&E surveys. I asked it to separate what Deltek already ships from what is only announced.
3. **Kill duplicates.** My first idea, a project overrun early warning, turned out to overlap Dela Insights and PPM Enterprise Risk. The research changed the pick to scope creep in timesheet notes. See [thinking.md](thinking.md).
4. **Prompt first, then app.** The classification prompt was written before the UI, with a fixed JSON schema, so the batch script and the live demo use the same prompt.
5. **Build in one file.** Single HTML page, no framework, so it runs on GitHub Pages and as a Claude artifact.
6. **Check.** Schema validation and a small eval (`scripts/eval.py`), a JavaScript syntax check, and screenshots at two widths before publishing.

## Prompts I used

The brief, in my words:

> I need to do complete research. Get some prototype ready for it with my git links and stuff to actually brainstorm a function for them, by clearly documenting all thought processes and final git and published links.

What I asked for along the way, in order:
- Research first, and keep what Deltek already ships separate from what is only announced.
- Drop any idea that duplicates Dela.
- A classification prompt that cites one clause, quotes the evidence and says "unclear" instead of guessing.
- Honest documentation of what was and wasn't run.

The production prompts are in [`/prompts`](../prompts).

## My other AI-led builds

| Repo | What it is |
| --- | --- |
| [curious](https://github.com/anirudh-ship-it-hub/curious) | LLM app for everyday curiosity: classifies a question, returns one schema-validated JSON knowledge object rendered at three depths, plus an LLM-as-judge mode that scores your own explanation |
| [digibouquet](https://github.com/anirudh-ship-it-hub/digibouquet) | Digital bouquet gift web app, static site on Vercel, built and improved with Claude Code |
| [personal-development-os](https://github.com/anirudh-ship-it-hub/personal-development-os) | Gamified personal development app in Next.js, TypeScript and Supabase |
