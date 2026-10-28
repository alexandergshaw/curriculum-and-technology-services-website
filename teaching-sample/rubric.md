# Sample rubric

Provisional weights for faculty adaptation. This assesses the offline unit; it does not award credit for live-model integration. The individual demonstration and essential competencies are required evidence even when the weighted total is high. Faculty set passing thresholds and resubmission arrangements before delivery.

| Criterion | Points | Full-credit evidence | Partial-credit example |
| --- | ---: | --- | --- |
| Implementation and source handling | 25 | Arbitrary-question retrieval, current-source filtering, stable provenance, correct response checks, useful additional tests | Works on public examples but mishandles an unknown citation or another question |
| Evaluation design and interpretation | 30 | Four reasoned judgments, exact source support, distinction between structural and semantic checks, appropriate alternatives, honest limits | Recognizes stale sources but treats a valid citation as proof of the printing claim |
| Failure handling and justified revision | 15 | Reproduces the version failure, explains and verifies the correction, updates affected teaching material | Changes the answer but omits the regression case or impact on the assignment |
| Reproducibility and handoff | 10 | Clear commands, preserved fixture labels, usable change record, limitations and verification evidence | Another person can run the code but cannot tell which article or test changed |
| Individual explanation and observed modification | 20 | Independently explains the unsupported claim and version logic, makes and checks a small relevant modification | Explains the final answer but needs substantial help tracing or modifying the code |
| **Total** | **100** | | |

## Essential evidence

Each student must explain why citation existence differs from factual support, diagnose the version mismatch, and demonstrate an implementation change. A test pass or polished report cannot replace that evidence. Faculty should state whether missing evidence results in an incomplete assessment, a required reassessment, or another published course procedure.

## Reasoning matters

For the printing question, either a qualified revision or a referral that identifies the missing information can be defensible. For the password question as written, the document supports self-service instructions; a blanket refusal is unhelpful. For the updated software article, the provided metadata identifies version 2 as current. Students should not invent conflicts or assume the old email route still works.

No model score, response time, or API expenditure contributes to this offline-unit grade. The full proposed course would assess a successful live integration and the quality of comparison reasoning, not whether one student's model produces a higher answer score than another's. All students must implement and evaluate both approaches before recommending ordinary search as the preferred solution.

## Feedback format

For each criterion, record points, the inspected evidence, one specific strength, and one next action. Separate a code defect from an unsupported interpretation. Use `annotated-submission.md` as a calibration example; it is authored, not a real student's record.
