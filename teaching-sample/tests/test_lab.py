"""Behavioral checks, not a model-quality benchmark or a secure exam bank."""

import copy
import importlib
import os
import unittest

engine = importlib.import_module(os.environ.get("LAB_IMPLEMENTATION", "reference"))


class LabChecks(unittest.TestCase):
    def setUp(self):
        self.fixture = engine.load_fixture()
        self.documents = self.fixture["documents"]

    def test_baseline_matches_public_case_sources(self):
        for case in self.fixture["cases"]:
            with self.subTest(case=case["id"]):
                first = engine.search(case["question"], self.documents)[0]
                self.assertEqual({"id": first["id"], "version": first["version"]}, case["baseline_source"])

    def test_arbitrary_question_is_not_a_case_lookup(self):
        result = engine.search("Visitors need a Wi-Fi day pass", self.documents)
        self.assertEqual(result[0]["id"], "wifi")
        self.assertIn("reception desk", result[0]["text"])

    def test_empty_and_invalid_questions(self):
        for value in ("", "   ", None, 12):
            with self.subTest(value=value), self.assertRaises(ValueError):
                engine.search(value, self.documents)

    def test_unknown_terms_return_no_result(self):
        self.assertEqual(engine.search("telescope orbital spectrum", self.documents), [])

    def test_limit_and_current_sources(self):
        result = engine.search("software installation", self.documents, limit=1)
        self.assertEqual([(doc["id"], doc["version"]) for doc in result], [("software", 2)])
        for limit in (0, -1, True, 1.5):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                engine.search("software", self.documents, limit=limit)

    def test_request_retains_source_version_and_text(self):
        request = engine.prepare_request("request software installation", self.documents)
        self.assertEqual(request["question"], "request software installation")
        self.assertTrue(request["instruction"].strip())
        self.assertEqual(request["sources"][0]["source_id"], "software")
        self.assertEqual(request["sources"][0]["version"], 2)
        self.assertIn("Service Portal", request["sources"][0]["text"])

    def test_supported_response_has_no_structural_issue(self):
        response = engine.replay_response("supported", self.fixture)
        self.assertEqual(engine.validate_response(response, self.documents), [])

    def test_valid_citation_does_not_prove_support(self):
        response = engine.replay_response("unsupported", self.fixture)
        self.assertEqual(engine.validate_response(response, self.documents), [])
        self.assertEqual(self.fixture["cases"][1]["expected_decision"], "revise")

    def test_refusal_can_be_structurally_valid_but_unhelpful(self):
        response = engine.replay_response("refusal", self.fixture)
        self.assertEqual(engine.validate_response(response, self.documents), [])

    def test_source_update_exposes_stale_response_and_revision_resolves_it(self):
        original = engine.replay_response("outdated", self.fixture)
        before = copy.deepcopy([doc for doc in self.documents if not (doc["id"] == "software" and doc["version"] == 2)])
        for doc in before:
            if doc["id"] == "software":
                doc["current"], doc["status"] = True, "current"
        self.assertEqual(engine.validate_response(original, before), [])
        self.assertIn("superseded citation: software@1", engine.validate_response(original, self.documents))
        revised = engine.replay_response("outdated", self.fixture, revised=True)
        self.assertEqual(engine.validate_response(revised, self.documents), [])
        self.assertIn("Service Portal", revised["text"])

    def test_missing_citation_and_bad_shapes(self):
        self.assertIn("response must be an object", engine.validate_response(None, self.documents))
        self.assertIn("text must be a nonempty string", engine.validate_response({"text": "", "abstain": True, "citations": []}, self.documents))
        self.assertIn("abstain must be a boolean", engine.validate_response({"text": "x", "abstain": "false", "citations": []}, self.documents))
        self.assertIn("citations must be a list", engine.validate_response({"text": "x", "abstain": False, "citations": "wifi"}, self.documents))
        self.assertIn("an answer must cite at least one source", engine.validate_response({"text": "x", "abstain": False, "citations": []}, self.documents))

    def test_unknown_duplicate_and_malformed_citations(self):
        response = {"text": "Check the instructions.", "abstain": False, "citations": [
            {"source_id": "wifi", "version": 1}, {"source_id": "wifi", "version": 1},
            {"source_id": "missing", "version": 1}, {"source_id": "wifi", "version": True},
            {"version": 1}, "wifi",
        ]}
        issues = engine.validate_response(response, self.documents)
        for expected in ("duplicate citation: wifi@1", "unknown citation: missing@1", "citation version must be a positive integer", "citation needs a source_id", "citation must be an object"):
            self.assertIn(expected, issues)

    def test_replay_is_an_independent_authored_copy(self):
        response = engine.replay_response("supported", self.fixture)
        response["text"] = "changed"
        self.assertNotEqual(engine.replay_response("supported", self.fixture)["text"], "changed")
        with self.assertRaises(ValueError):
            engine.replay_response("missing", self.fixture)
        with self.assertRaises(ValueError):
            engine.replay_response("supported", self.fixture, revised=True)


if __name__ == "__main__":
    unittest.main()
