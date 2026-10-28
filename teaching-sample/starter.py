"""Student workspace. Complete the three functions; keep their interfaces."""

from common import load_fixture, replay_response, terms


def search(question, documents, limit=3):
    """Task 1: return up to limit CURRENT documents with query-term overlap.

    Validate a nonempty question and positive integer limit. Use supplied terms()
    to compute distinct token overlap: title weight 2, text weight 1. Exclude zero
    scores and superseded documents. Sort by descending score, then id/version.
    Work for arbitrary input questions; do not switch on the four case IDs.
    """
    raise NotImplementedError("Task 1: implement the search baseline")


def prepare_request(question, documents):
    """Task 2: prepare {question, instruction, sources} without a network call.

    Use search() to select documents. Each source has source_id, version, text.
    Explain in the instruction that passages provide evidence and missing
    information must be stated. An instruction alone is not a security control.
    """
    raise NotImplementedError("Task 2: preserve source identity at the boundary")


def validate_response(response, documents):
    """Task 3: return a list of structural/provenance problems; [] means none.

    Validate text, boolean abstain, citation list, citation source/version types,
    duplicate/unknown/superseded citations, and missing citations for an answer.
    Error strings are specified in tests so the CLI can expose a stable contract.
    Do NOT claim that passing these checks establishes factual support.
    """
    raise NotImplementedError("Task 3: implement structural and version checks")
