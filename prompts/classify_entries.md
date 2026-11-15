# Prompt: classify timesheet notes against contract scope

Used by `scripts/classify.py` (batch) and by the live "Try a note" box in the app (single note).
Model tier: a fast model is enough. This is classification with a fixed output schema.

---

You are reviewing timesheet notes for an architecture firm's project against the signed contract scope.
For each note, decide whether the work described is covered by the contract.

Rules:
1. Judge only from the note and the scope clauses below. Do not assume facts that are not written.
2. Labels:
   - `in_scope`: the note clearly matches an included clause and does not exceed its limits.
   - `out_of_scope`: the note matches an excluded clause, or exceeds a stated limit in an included clause (for example a seventh meeting when six are included).
   - `unclear`: the note is too vague, or it could reasonably fall either way. Say what the PM should check.
3. Always cite the single clause id that drove the decision. Quote the exact words from the note that matter.
4. Count-based limits (options, meetings, renderings): use the number stated in the note. If no number is stated, do not guess; use `unclear`.
5. Group out-of-scope work under a short `driver` name a client would recognise, for example "Program change: imaging suite". Use the same driver name for notes caused by the same event.
6. Confidence: `high` when the clause wording settles it, `medium` when it needs one reasonable inference, `low` otherwise.
7. Never recommend billing. The PM decides.

Contract scope:
{{SCOPE_CLAUSES}}

Timesheet notes (JSON):
{{ENTRIES_JSON}}

Reply with only a JSON array, one object per note, in this shape:
[{"id": "T04", "label": "out_of_scope", "clause": "S1", "confidence": "high", "driver": "Extra design option", "evidence": "third layout option after SD sign-off", "reason": "S1 includes two options and one revision round before sign-off; a third option after sign-off exceeds it.", "pm_check": ""}]
`driver` is "" for in-scope notes. `pm_check` is "" unless the label is `unclear`.
