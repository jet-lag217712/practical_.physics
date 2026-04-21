from src.ai.utils.sys_context import system_context_radio, system_context_checkbox, system_context_textbox
from src.ai.utils.format import *

def request_answer(client, question, answer, type):

    if type == 'radio':
        context = system_context_radio
    elif type == 'checkbox':
        context = system_context_checkbox
    elif type == 'text':
        context = system_context_textbox

    output = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
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
        temperature=0.25,
        max_completion_tokens=256,
        top_p=1,
        stream=False
    )

    answer_text = output.choices[0].message.content.strip()
    return parse_answer(answer_text, qtype=type)
