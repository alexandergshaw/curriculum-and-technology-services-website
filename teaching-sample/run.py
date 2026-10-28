"""Run real offline retrieval or replay an explicitly authored response."""

import argparse
import importlib
import json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--question", help="Run the search baseline for any question")
    inputs.add_argument("--case", choices=["supported", "unsupported", "refusal", "outdated"])
    parser.add_argument("--revision", action="store_true", help="Replay the authored revised response")
    parser.add_argument("--implementation", choices=["reference", "starter"], default="reference")
    args = parser.parse_args()
    if args.revision and args.case != "outdated":
        parser.error("--revision is available only with --case outdated")
    engine = importlib.import_module(args.implementation)
    fixture = engine.load_fixture()
    documents = fixture["documents"]
    try:
        if args.question is not None:
            result = {
                "mode": "offline search; no model call",
                "question": args.question,
                "results": engine.search(args.question, documents),
            }
        else:
            case = next(item for item in fixture["cases"] if item["id"] == args.case)
            response = engine.replay_response(args.case, fixture, args.revision)
            result = {
                "mode": "authored teaching replay; no model call",
                "notice": fixture["fixture_notice"],
                "request": engine.prepare_request(case["question"], documents),
                "search_results": engine.search(case["question"], documents),
                "response": response,
                "structural_issues": engine.validate_response(response, documents),
                "next_step": "A person must judge whether the sources support the answer and whether answering or referring is appropriate.",
            }
    except (ValueError, NotImplementedError) as error:
        parser.exit(2, str(error) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
