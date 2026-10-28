# Evaluate and revise an AI support assistant

A complete, offline sample unit from Access Curriculum & Technology, by Alex Shaw and Baha Marupov. Both are software professionals and college educators. This is an illustrative teaching sample, not a record of a college engagement or student results.

**The search code runs. The answer examples are authored fixtures.** No model is called, no data leaves the computer, and no API account or third-party Python package is needed. This unit demonstrates retrieval, response validation, evaluation, and maintenance. It does not demonstrate live-model integration or measure model performance.

## Start here

Use Python 3.10 or later. Open a terminal in this extracted folder. If your computer uses `python3` or `py` instead of `python`, substitute that command below.

```text
python check.py reference
python run.py --question "How do students connect to campus Wi-Fi?"
python run.py --case unsupported
python run.py --case outdated
python run.py --case outdated --revision
```

The reference check should finish with `OK`. The outdated case should show `superseded citation: software@1`; the authored revision should show an empty structural-issues list. That empty list does not establish factual correctness. Read the sources and judge the meaning.

For student work:

```text
python check.py starter
python run.py --case supported --implementation starter
```

The starter intentionally fails until its three functions are completed. Do not use `check.py reference` as evidence that a student's code passes.

## What is included

| File | Purpose |
| --- | --- |
| `student-guide.md` | Outcomes, tasks, evidence to submit, AI-use statement |
| `instructor-guide.md` | Setup, facilitation, assessment, access and outage considerations |
| `rubric.md` | Criteria, weights, and competency requirements |
| `annotated-submission.md` | Authored example showing credit, errors, and feedback |
| `course-outline.md` | Proposed semester context; the complete semester is not included |
| `change-record.md` | A completed illustrative revision record |
| `data/cases.json` | Canonical synthetic documents, authored answers, and review explanations |
| `common.py` | Supplied data loading, tokenizer, and explicitly authored replay source |
| `starter.py` / `reference.py` | Student workspace and instructor implementation |
| `run.py` / `check.py` | Command-line demonstration and test runner |
| `tests/test_lab.py` | Behavioral checks, including the document-version regression |

The same JSON powers the website's four teaching cases. Public cases and solutions are inspectable examples, not a secure exam bank. In a taught course, faculty would prepare additional unseen cases and approve the grading policy.

## Boundaries

The proposed full course in `course-outline.md` requires institution-approved access for its live integration activity. Offline replay can support preparation and outages, but it cannot permanently substitute for demonstrating a successful live integration. The full course, additional labs, and live adapter are proposed work, not included deliverables.

Faculty choose the fit, thresholds, schedule, and scope for their college. Access can adapt this approach to an existing course, develop a new course, or support agreed annual revisions. Contact: alexandergshaw@gmail.com.
