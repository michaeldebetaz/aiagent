from google import genai
from google.genai import types
from functions.get_tools import get_tools

MODEL = "gemini-2.0-flash-001"

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def generate_content(
    client: genai.Client, contents: list[types.Content]
) -> types.GenerateContentResponse:

    config = types.GenerateContentConfig(
        tools=get_tools(), system_instruction=SYSTEM_PROMPT
    )
    response = client.models.generate_content(
        model=MODEL, contents=contents, config=config
    )

    return response
