from src.ai.utils.format import parse_answer

MAX_EMPTY_RESPONSE_ATTEMPTS = 3


def _extract_message_content(output):
    choices = getattr(output, "choices", None)
    if not choices:
        return None

    message = getattr(choices[0], "message", None)
    if message is None:
        return None

    return getattr(message, "content", None)


def request_with_retry(client, request_kwargs, qtype, max_attempts=MAX_EMPTY_RESPONSE_ATTEMPTS):
    for attempt in range(1, max_attempts + 1):
        output = client.chat.completions.create(**request_kwargs)
        answer_text = _extract_message_content(output)

        if isinstance(answer_text, str) and answer_text.strip():
            return parse_answer(answer_text, qtype=qtype)

        if answer_text is not None and not (isinstance(answer_text, str) and not answer_text.strip()):
            raise ValueError(f"Unsupported model output content type: {type(answer_text).__name__}")

        if attempt == max_attempts:
            raise ValueError(
                f"Model returned empty output on all {max_attempts} attempts."
            )

