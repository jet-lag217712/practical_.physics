import re


def parse_answer(output, qtype):
    if not output:
        raise ValueError("Empty model output")
    output = output.strip()
    if qtype == "radio":
        match = re.search(r'\d+', output)
        if not match:
            raise ValueError(f"Invalid radio output: {output}")
        value = int(match.group())
        return [value - 1]
    elif qtype == "checkbox":
        numbers = re.findall(r'\d+', output)
        if not numbers:
            raise ValueError(f"Invalid checkbox output: {output}")
        return [int(n) - 1 for n in numbers]
    elif qtype == "text":
        return [output.strip()]
    else:
        raise ValueError(f"Unknown question type: {qtype}")