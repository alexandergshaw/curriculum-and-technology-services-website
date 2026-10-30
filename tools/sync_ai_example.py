"""Keep the no-JavaScript example identical to the shared teaching data."""
import argparse
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- START STATIC CASE: generated from teaching-sample/data/cases.json -->"
END = "<!-- END STATIC CASE -->"


def title_case_label(label):
    """Match the interface-heading treatment in ai-example.js."""
    minor_words = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor", "of", "on", "or", "per", "the", "to", "via", "with"}
    words = label.split(" ")
    return " ".join(word.lower() if 0 < index < len(words) - 1 and word.lower() in minor_words
                    else word[:1].upper() + word[1:] for index, word in enumerate(words))


def render_case(data):
    case = data["cases"][0]
    source = next(doc for doc in data["documents"]
                  if (doc["id"], doc["version"]) == (case["source_id"], case["source_version"]))
    baseline = next(doc for doc in data["documents"]
                    if (doc["id"], doc["version"]) == (case["baseline_source"]["id"], case["baseline_source"]["version"]))
    cite = ", ".join(f'{item["source_id"]} · v{item["version"]}' for item in case["response"]["citations"])
    decision = title_case_label({"accept": "Accept", "revise": "Revise", "refer": "Refer to a person"}[case["expected_decision"]])
    return f'''{START}
          <div class="case-question"><h4 id="case-title">{escape(title_case_label(case['label']))}</h4><p id="case-question">{escape(case['question'])}</p></div>
          <div class="lab-grid"><div><h3>Source Evidence</h3><div class="source-list" id="case-sources"><article><h4>{escape(source['title'])}</h4><p class="source-meta">{escape(source['id'])} · v{source['version']} · {escape(source['status'])}</p><p>{escape(source['text'])}</p></article></div></div><div class="lab-responses"><article><h3>Search Result</h3><p id="baseline-answer">{escape(baseline['text'])}</p></article><article><h3>Authored AI-Style Answer</h3><p id="model-answer">{escape(case['response']['text'])}</p><p class="source-meta" id="answer-citations">Cites: {escape(cite)}</p></article></div></div>
          <div class="lab-fallback" id="lab-fallback"><h4 id="fallback-decision">Instructor Judgment: {decision}</h4><p id="fallback-explanation">{escape(case['explanation'])} {escape(case['alternative_judgment'])}</p></div>
          {END}'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the checked-in example differs from the shared data")
    args = parser.parse_args()
    page = ROOT / "ai-course-example.html"
    original = page.read_text(encoding="utf-8")
    data = json.loads((ROOT / "teaching-sample/data/cases.json").read_text(encoding="utf-8"))
    start, end = original.index(START), original.index(END) + len(END)
    updated = original[:start] + render_case(data) + original[end:]
    if args.check:
        if updated != original:
            raise SystemExit("Static case is stale. Run python tools/sync_ai_example.py")
        print("Static teaching case matches the shared data.")
    else:
        page.write_text(updated, encoding="utf-8", newline="\n")
        print("Static teaching case updated.")


if __name__ == "__main__":
    main()
