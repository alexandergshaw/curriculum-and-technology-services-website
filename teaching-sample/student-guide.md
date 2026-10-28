# Student guide

## Your assignment

Help a fictional college improve an IT support assistant. You will build a simple search baseline, preserve source information, validate answer structure, evaluate authored responses, and show how a source change affects the application.

You should already be able to write and debug a small Python program, work with lists and dictionaries, read JSON, and use basic Git. Before starting, find the current software article in `data/cases.json`, explain the difference between its identifier and version, and write a function that selects current documents. Ask for a refresher if those tasks are unfamiliar.

The data is synthetic. The responses were authored for teaching; they are not live model outputs. Do not report the four cases as an AI accuracy benchmark.

## Learning outcomes

By the end of this unit you should be able to implement retrieval that preserves provenance, distinguish structural checks from evidence of claim support, diagnose a stale answer, and explain a tested revision independently.

## 1. Establish the baseline

Run the reference checks and one arbitrary search question using the README commands. Inspect the returned passages. Explain what the tokenizer and overlap score can and cannot recognize.

Complete `search()` in `starter.py`. Follow its documented scoring and ordering contract. Exclude superseded documents, reject invalid inputs, and return no result when no terms match. The function must work for questions beyond the four public cases.

Complete `prepare_request()`. Preserve each selected source's identifier, version, and exact passage. No provider request is made. Explain why retaining the identifier alone would be insufficient after an article changes.

## 2. Validate and evaluate

Complete `validate_response()`. The contract concerns text, refusal flags, citation structure, known references, and current versions. Run `python check.py starter` while working.

Then review all four authored cases. For each, record your decision (accept, revise, or refer), the exact passage supporting your decision, whether structural validation passes, and a revised answer when needed. Explain defensible alternative judgments. Pay particular attention to the remote-printing claim and the unnecessary password-reset refusal.

Add at least two tests of your own: one input or citation boundary case and one retrieval case using a question outside the public set. Explain the defect each would detect. Automated structural checks cannot decide whether a passage supports a claim; record that human judgment separately.

## 3. Make and document a revision

Run the outdated case and its authored revision. In the existing regression test, inspect the original source collection, the updated collection, and the corrected citation. Explain why the same answer changes from acceptable provenance to a stale reference.

Your change record must identify the affected article and version, the old and new route for software requests, the application change, the assignment/instructor-note changes, checks performed, and remaining limitations. Use `change-record.md` as an authored example, not as evidence that faculty have approved your work.

## Submit

Submit your completed `starter.py`, added tests, check output, four-case evaluation, change record, and a short handoff note with reproduction commands and known limitations. Keep the fixture notice with any copied responses. Do not include credentials or real support records.

Include a brief AI-assistance statement: what assistance you used, what you accepted or changed, and how you verified it. You do not need to submit private chat histories. Faculty may set additional course rules before assigning the work.

## Individual demonstration

Explain the unsupported printing claim, identify the stale source version, and make a small code change requested by your instructor while explaining its effect. An accessible equivalent can use a typed walkthrough and an observed keyboard-based modification under the same criteria. An instructor will assess your understanding of the implementation and evidence, not the fluency of a generated explanation.

A useful conclusion may be that ordinary search is sufficient for this narrow task. In the proposed full course, you would still implement and evaluate the model-backed approach before making that recommendation. This offline unit does not assess live integration.
