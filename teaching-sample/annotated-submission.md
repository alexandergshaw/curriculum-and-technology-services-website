# Annotated example submission

**Authored teaching example.** The submission, feedback, points, and demonstration excerpt below are fictional. They illustrate assessment; they are not student results or evidence of classroom use.

## Submitted evidence

The example submission implements current-source search and source-version checks. Its code passes the supplied reference behaviors but its added tests only repeat the Wi-Fi case. The evaluation includes this table:

| Case | Submitted decision and explanation | Instructor annotation |
| --- | --- | --- |
| Supported | Accept: Campus-Student and the login instructions appear in Wi-Fi v1 | Supported. The exact instructions are traced correctly. |
| Unsupported | Accept: The answer cites printing v1 and mentions a campus ID card | Incorrect inference. Printing v1 does not support a personal home connection. A real citation can accompany an unsupported claim. |
| Refusal | Revise: Password Help provides steps, with referral if recovery is unavailable | Supported. The response should preserve both the procedure and its limit. |
| Outdated | Revise: replace email with the Service Portal and cite software v2 | Supported, but the submitted change record does not identify the affected assignment or instructor notes. |

The submission's revised software answer is: “Submit a Software request in the Service Portal with the computer asset number, software name, and teaching purpose. Wait for approval.” It cites software v2. This is supported, although explicitly noting that email requests are no longer accepted would help explain the change.

In the authored individual demonstration, the learner correctly traces `(source_id, version)` through validation and adds a test for an unknown source. When asked about the printing answer, they initially rely on the citation's existence and then identify the unsupported phrase after a prompt. That needs further independent evidence.

## Scoring and feedback

| Criterion | Awarded | Evidence and next action |
| --- | ---: | --- |
| Implementation and source handling | 21/25 | Correct current-version behavior; add a retrieval question beyond the public set and a genuinely different boundary case. |
| Evaluation design and interpretation | 20/30 | Three cases reasoned well; revise the remote-printing judgment and explain why automated validation missed it. |
| Failure handling and revision | 12/15 | Code and answer revised; name the assignment and instructor-note changes in the record. |
| Reproducibility and handoff | 8/10 | Commands reproduce the output; add the source versions and remaining limitations to the handoff. |
| Individual explanation and modification | 16/20 | Independently explains version logic and changes a test; reassess the unsupported-claim distinction without prompting. |
| **Total** | **77/100** | **Illustrative weighted result, not a passing decision.** |

The unresolved essential competency is evaluating claim support independently. Under a policy requiring that competency, the assessment remains incomplete pending reassessment despite the numerical total. The instructor must use the college's published procedure.

## A stronger printing response

“The article explains printing while connected to the college network. It does not say whether a personal home connection is supported. Use the documented campus procedure, or ask the service desk about remote access.”

This preserves the supported information and identifies the gap. It does not invent a home-printing feature or claim that remote printing is impossible.
