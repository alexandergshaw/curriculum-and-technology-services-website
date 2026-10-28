"""Supplied data and replay plumbing. No model calls or external dependencies."""

import copy
import json
import re
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "cases.json"
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "can", "do", "does", "for",
    "from", "how", "i", "in", "is", "it", "my", "now", "of", "on", "or",
    "the", "to", "using", "what", "with",
}


def terms(text):
    """A deliberately simple tokenizer, not semantic search."""
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP_WORDS


def load_fixture(path=DATA_PATH):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def replay_response(case_id, fixture, revised=False):
    """Return a COPY of an authored teaching response, never a model output."""
    case = next((item for item in fixture["cases"] if item["id"] == case_id), None)
    if case is None:
        raise ValueError("Unknown teaching case: " + case_id)
    key = "revised_response" if revised else "response"
    if key not in case:
        raise ValueError("This teaching case has no authored revision.")
    return copy.deepcopy(case[key])
