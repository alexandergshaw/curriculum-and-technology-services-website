# Instructor guide

## What is ready to teach

This package contains one complete offline evaluation-and-revision unit, including a working reference implementation and a deliberately incomplete student workspace. The broader semester outline is proposed. The fixture answers, submission, and change record are authored teaching materials; none records a student, model run, or actual faculty approval.

## Preparation and environment

Use a college-managed computer with Python 3.10 or later, an editor, and a terminal. No package installation, accounts, network service, or GPU is required. Confirm the configured Python command with `python --version`. Unzip the package into a writable folder, open a terminal there, and run `python check.py reference`. Confirm `OK` before assigning it. Check that the editor opens UTF-8 Markdown and JSON correctly.

Run every README example yourself. Read the four cases, rubric, and annotated submission. The starter and reference use the same tests; the untouched starter should fail. For a real assessment, create new equivalent cases and approve the criteria before release. Public solutions are intentionally inspectable and cannot serve as a secret test bank.

The default facilitation sequence is a baseline walkthrough, a student implementation session, a case-review discussion, then a revision and individual demonstration. Faculty should pilot the unit to choose contact time and preparation workload; this sample has no measured teaching-time claim.

## Readiness and scaffolding

Use the student guide's readiness task to check functions, dictionaries, JSON, and debugging. Provide a short refresher before the implementation if needed. `common.py` supplies file loading, replay, and tokenization so students focus on the three assessed functions. Instructors may give more of `search()` as scaffolding for less experienced cohorts while adjusting the implementation criterion transparently.

Explain the distinction between a language model, this replay component, and a search algorithm. The replay returns authored text; it is not a model and does not produce a new answer to arbitrary questions. The search does process arbitrary questions, with deliberately limited lexical matching.

## Facilitation notes

Ask students to identify the exact support for each instruction before selecting a decision. In the printing case, structural validation passes despite the unsupported home-internet claim. In the reset case, a valid refusal still fails the usefulness criterion. In the software case, distinguish selecting a current source from detecting an answer that still cites an older version.

Do not force one-word answers when reasoning supports a different action. A referral for unresolved remote printing can be justified; a confident claim that remote printing is impossible cannot. For the software case, current-version metadata is supplied. If that authority were unknown, checking with the responsible person would be appropriate.

## Assessment

Use `rubric.md` and `annotated-submission.md` to calibrate feedback. Evaluate implementation and reasoning separately. Passing automated tests alone is insufficient. Require each student to locate the unsupported claim, explain source-version handling, and demonstrate a relevant code modification. Provide an accessible equivalent with the same competencies and follow the college's resubmission policy.

Clarify permitted AI assistance before the unit. The supplied statement asks students to describe assistance and verification, not disclose personal conversations. Group implementation can be permitted if individual understanding remains independently assessed.

## Common difficulties

| Symptom | Check |
| --- | --- |
| Python command is missing | Use the college's supported installation; try its documented `python3` or `py` command |
| Fixture file cannot be found | Preserve the extracted `data/` folder beside the scripts; the loader resolves paths from its own location |
| Starter reports `NotImplementedError` | Expected until the three functions are completed; do not switch to reference checks to obtain a student pass |
| Old software article appears in search | Check `current` filtering before scoring |
| Unknown or stale citations pass | Validate the identifier/version pair and current status |
| Printing answer passes all automated checks | Expected: a person must judge whether the passage supports the remote-access claim |
| A question returns no passage | Inspect token overlap; the baseline does not understand synonyms |

## Full-course delivery requirements

The proposed full course adds a verified model adapter and a live comparison activity. Before scheduling that version, the college and Access must agree the approved provider/environment, faculty setup responsibilities, student access, usage limits, data rules, support, and assessment arrangements. Students should not need personal paid accounts. No live adapter or provider integration is included or claimed here.

Complete this access checklist with the college before delivering the proposed live activity. It is blank because no college/provider arrangement is implied by this sample.

| Delivery decision | College decision / responsible person |
| --- | --- |
| Approved provider, model/version, and environment | ____________________ |
| How every student receives equivalent approved access without a personal paid account | ____________________ |
| Who configures credentials and verifies a successful faculty test request | ____________________ |
| Which synthetic/approved data may be sent and how output records are retained | ____________________ |
| Per-student usage limits, overall ceiling, and person monitoring spending | ____________________ |
| Supported lab environment and instructor setup/troubleshooting owner | ____________________ |
| Accessible assessment arrangements and support contact | ____________________ |
| Outage plan and replacement opportunity to demonstrate live integration | ____________________ |

### Blank cost-planning worksheet

These are planning inputs, not published rates, measured usage, or a quote. Record the source of each estimate. The example formula assumes separate per-million input/output token prices; adapt it to the approved provider's actual billing rules, including any cache, tool, embedding, or storage charges.

| Input | Symbol | Value / source |
| --- | --- | --- |
| Provider and model/version | — | ____________________ |
| Pricing source and date checked | — | ____________________ |
| Number of students | N | ____________________ |
| Planned calls per student, including evaluation repeats and retries | S | ____________________ |
| Average input tokens per call, including retrieved passages | I | ____________________ |
| Average output tokens per call | O | ____________________ |
| Input price per million tokens in the chosen currency | Pin | ____________________ |
| Output price per million tokens in the same currency | Pout | ____________________ |
| Other estimated course charges in that currency | X | ____________________ |
| Contingency fraction, expressed as a decimal | C | ____________________ |
| Agreed total spending ceiling in that currency | B | ____________________ |
| Estimate owner and review date | — | ____________________ |

Estimated token cost: `T = N * S * (I * Pin + O * Pout) / 1,000,000`.

Estimated total with contingency: `E = (T + X) * (1 + C)`.

Compare `E` with ceiling `B` before delivery and revise activity volume or access arrangements if needed. Provider limits and actual spend monitoring remain necessary; a worksheet does not enforce a cap. Record whether token counts came from a small pilot or from planning assumptions, and update them after the faculty test run.

During an outage, use replay for implementation practice and previously captured, clearly dated real outputs for analysis when available. Authored fixtures must remain labeled. Arrange restored or equivalent approved access and another assessment opportunity for live integration; do not silently replace that competency with replay or penalize a student for an access failure.

## Accessibility and upkeep

All instructions and outputs are text. Offer the typed walkthrough and observed modification described in the student guide when appropriate. Check the college's editor/terminal accessibility before delivery and allow equivalent ways to present evidence.

Review together, agree priorities, update materials, and review changes with faculty. Track source versions, case decisions, rubric changes, and instructor notes together. This sample's `change-record.md` shows that process without implying approval occurred.
