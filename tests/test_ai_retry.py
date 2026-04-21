import base64
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from src.ai.image_solver import request_picture_answer
from src.ai.text_solver import request_answer


def make_response(content):
    if content == "missing":
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace())])
    if content == "no_message":
        return SimpleNamespace(choices=[SimpleNamespace()])
    if content == "no_choices":
        return SimpleNamespace()
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))]
    )


class FakeCompletions:
    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if not self._responses:
            raise AssertionError("Unexpected extra completion request")
        return self._responses.pop(0)


class FakeClient:
    def __init__(self, responses):
        self.chat = SimpleNamespace(completions=FakeCompletions(responses))


class AiRetryTests(unittest.TestCase):
    def test_text_solver_retries_once_then_returns_second_result(self):
        client = FakeClient([make_response("   "), make_response("2")])

        result = request_answer(client, "Question?", ["A", "B"], "radio")

        self.assertEqual(result, [1])
        self.assertEqual(len(client.chat.completions.calls), 2)

    def test_image_solver_succeeds_on_third_attempt(self):
        client = FakeClient(
            [make_response(None), make_response("missing"), make_response("1, 3")]
        )

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as image_file:
            image_file.write(base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="))
            image_path = Path(image_file.name)

        try:
            result = request_picture_answer(
                client,
                "Question?",
                ["A", "B", "C"],
                "checkbox",
                str(image_path),
            )
        finally:
            image_path.unlink(missing_ok=True)

        self.assertEqual(result, [0, 2])
        self.assertEqual(len(client.chat.completions.calls), 3)

    def test_empty_output_raises_after_three_attempts(self):
        client = FakeClient(
            [make_response("no_choices"), make_response("   "), make_response(None)]
        )

        with self.assertRaisesRegex(
            ValueError, "Model returned empty output on all 3 attempts\\."
        ):
            request_answer(client, "Question?", ["A", "B"], "radio")

        self.assertEqual(len(client.chat.completions.calls), 3)

    def test_invalid_non_empty_output_fails_without_retry(self):
        client = FakeClient([make_response("not a valid choice"), make_response("2")])

        with self.assertRaisesRegex(ValueError, "Invalid radio output"):
            request_answer(client, "Question?", ["A", "B"], "radio")

        self.assertEqual(len(client.chat.completions.calls), 1)

    def test_valid_first_response_does_not_retry(self):
        client = FakeClient([make_response("typed answer")])

        result = request_answer(client, "Question?", [], "text")

        self.assertEqual(result, ["typed answer"])
        self.assertEqual(len(client.chat.completions.calls), 1)


if __name__ == "__main__":
    unittest.main()
