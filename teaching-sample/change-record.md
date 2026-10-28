# Illustrative change record: software requests

**Authored teaching example.** This record demonstrates a revision process. It does not record an actual college policy change or completed faculty approval.

| Field | Record |
| --- | --- |
| Change | Software installation requests move from service-desk email to the Service Portal |
| Previous source | `software`, version 1; email route |
| Current source | `software`, version 2; portal route and explicit withdrawal of email requests |
| Trigger | The previously supported answer still cites version 1 after version 2 becomes current |
| Affected materials | Source collection, response fixture, regression test, student assignment, instructor explanation |
| Agreed sample scope | Correct source selection and validation, revise the authored answer, update the evaluation guidance, record remaining limits |

## Reproduce the problem

Run `python run.py --case outdated`. The replay deliberately returns the original authored answer; current retrieval returns software v2. Validation reports `superseded citation: software@1`.

The regression test constructs the earlier collection where v1 was current and verifies that the original response had valid provenance then. It adds the newer collection and checks that the old citation is flagged. This demonstrates a real change in validation behavior, not a claim that a live model changed its answer.

## Agreed correction shown in the sample

Search excludes superseded documents. Response validation checks the identifier/version pair against current metadata. The authored revised response uses the Service Portal route, preserves the required information and approval instruction, and cites v2.

Run `python run.py --case outdated --revision` and `python check.py reference`. Structural issues should be empty for the revision and the checks should finish with `OK`. A reviewer must still compare the revised instructions with v2; passing checks alone do not prove support.

## Teaching-material revision

The student guide now asks learners to explain why the old answer becomes stale, identify both versions, and update the assignment and instructor notes in their record. The instructor explanation distinguishes retrieval of a current document from detecting a response that cites an old one. The rubric assesses both implementation and evidence of revision.

## Faculty review and remaining priorities

In a real engagement, faculty would review the revised assignment, expected reasoning, and grading impact before approving use. Record the actual reviewer, decision, and date at that time; approval has not occurred in this illustrative record.

Remaining limits: article metadata must be maintained by an accountable owner; a current citation can still support an incorrect inference; lexical search misses synonyms; four cases do not establish reliability; live-provider behavior is not tested here. A future review should add realistic questions and inspect feedback and student assessment evidence before expanding scope.

Review together → agree priorities → update materials → review the changes with faculty.
