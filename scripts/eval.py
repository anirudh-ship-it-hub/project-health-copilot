"""Score saved classifications against PM-reviewed labels. No API key needed.

The question that matters to a PM: of the work the agent flags as out of
scope, how much really is (precision), and how much real out-of-scope work
does it catch (recall)? 'unclear' counts as routed to a human, not as a miss.

Usage: python3 scripts/eval.py
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from classify import validate  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> None:
    project = json.loads((ROOT / "data" / "project.json").read_text())
    results = json.loads((ROOT / "data" / "classifications.json").read_text())["results"]
    gold = json.loads((ROOT / "data" / "gold_labels.json").read_text())["labels"]
    hours = {e["id"]: e["hours"] for e in project["entries"]}

    problems = validate(results, project)
    print("Schema checks:", "pass" if not problems else problems)

    pred = {r["id"]: r["label"] for r in results}
    tp = [i for i in gold if pred[i] == "out_of_scope" and gold[i] == "out_of_scope"]
    fp = [i for i in gold if pred[i] == "out_of_scope" and gold[i] != "out_of_scope"]
    fn = [i for i in gold if pred[i] == "in_scope" and gold[i] == "out_of_scope"]
    routed = [i for i in gold if pred[i] == "unclear"]
    caught_by_review = [i for i in routed if gold[i] == "out_of_scope"]

    precision = len(tp) / (len(tp) + len(fp)) if tp or fp else 0
    recall_auto = len(tp) / (len(tp) + len(fn) + len(caught_by_review))
    recall_with_review = (len(tp) + len(caught_by_review)) / (len(tp) + len(fn) + len(caught_by_review))

    print(f"Out-of-scope precision: {precision:.0%}  ({len(tp)} right, {len(fp)} wrong flags)")
    print(f"Out-of-scope recall, auto only: {recall_auto:.0%}")
    print(f"Out-of-scope recall, after PM checks the 'unclear' notes: {recall_with_review:.0%}")
    print(f"Missed outright (labelled in scope): {fn or 'none'}")
    print(f"Sent to PM as unclear: {len(routed)} notes, {sum(hours[i] for i in routed)} h; "
          f"{len(caught_by_review)} turned out to be out of scope")
    hrs_found = sum(hours[i] for i in tp)
    hrs_true = sum(hours[i] for i in gold if gold[i] == "out_of_scope")
    print(f"Out-of-scope hours flagged directly: {hrs_found} of {hrs_true} ({hrs_found / hrs_true:.0%})")


if __name__ == "__main__":
    main()
