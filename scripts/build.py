"""Build the single-file app from src/app.html and the data files.

Outputs:
  index.html          full HTML document, served by GitHub Pages
  dist/artifact.html  body-only version, published as a Claude artifact
                      (the artifact host adds its own <html>/<head> wrapper)

Usage: python3 scripts/build.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def prompt_body(path: pathlib.Path) -> str:
    """Return the prompt text below the '---' separator in a prompt file."""
    text = path.read_text(encoding="utf-8")
    return text.split("\n---\n", 1)[1].strip() + "\n"


def main() -> None:
    src = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
    project = json.loads((ROOT / "data" / "project.json").read_text(encoding="utf-8"))
    classes = json.loads((ROOT / "data" / "classifications.json").read_text(encoding="utf-8"))
    prompt = prompt_body(ROOT / "prompts" / "classify_entries.md")

    def js(value) -> str:
        # Safe to embed inside <script>: no closing tags can appear.
        return json.dumps(value, ensure_ascii=False).replace("</", "<\\/")

    body = (
        src.replace("/*__PROJECT__*/null", js(project))
        .replace("/*__CLASS__*/null", js(classes))
        .replace('/*__PROMPT__*/""', js(prompt))
    )
    assert "__PROJECT__" not in body and "__CLASS__" not in body and "__PROMPT__" not in body

    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "artifact.html").write_text(body, encoding="utf-8")

    # Full document for GitHub Pages: move <title>, <meta>, <link>, <style> into <head>.
    head_parts = re.findall(r"(<title>.*?</title>|<meta [^>]*>|<link [^>]*>|<style>.*?</style>)", body, re.S)
    rest = body
    for part in head_parts:
        rest = rest.replace(part, "", 1)
    page = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
        + "\n".join(head_parts)
        + "\n</head>\n<body>\n"
        + rest.strip()
        + "\n</body>\n</html>\n"
    )
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print("Built index.html and dist/artifact.html")


if __name__ == "__main__":
    main()
