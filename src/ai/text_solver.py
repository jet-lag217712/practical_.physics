from src.ai.utils.sys_context import system_context_radio, system_context_checkbox, system_context_textbox
from src.ai.utils.format import *
from src.ai.retry import request_with_retry

def request_answer(client, question, answer, type):

    if type == 'radio':
        context = system_context_radio
    elif type == 'checkbox':
        context = system_context_checkbox
    elif type == 'text':
        context = system_context_textbox

    request_kwargs = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {
                "role": "system",
                "content": (
                    context
                )
            },
            {
                "role": "user",
                "content": f"""
                Question: {question}
                Answer Choices: {answer}
                """
            }
        ],
        "temperature": 0.5,
        "max_completion_tokens": 256,
        "top_p": 1,
        "reasoning_effort": "high",
        "stream": False,
        "stop": None
    }

    return request_with_retry(client, request_kwargs, qtype=type)
