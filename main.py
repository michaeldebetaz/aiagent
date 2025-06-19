import os
import dotenv
from google import genai
from google.genai import types
import argparse
from functions.generate_content import generate_content
from functions.call_function import call_function


def main():
    dotenv.load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "":
        raise ValueError("GEMINI_API_KEY environment variable is not set")

    parser = argparse.ArgumentParser(prog="aiagent")
    parser.add_argument("user_prompt")
    parser.add_argument("--verbose", action="store_const", const=True, default=False)
    args = parser.parse_args()

    assert isinstance(args.user_prompt, str), "user_prompt must be a string"
    assert isinstance(args.verbose, bool), "verbose must be a boolean"

    client = genai.Client(api_key=api_key)

    contents = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = generate_content(client, contents)

    MAX_ITERATIONS = 20
    n_iterations = 0
    while n_iterations < MAX_ITERATIONS and response.function_calls is not None:
        n_iterations += 1

        assert isinstance(
            response.candidates, list
        ), "Response candidates must be a list"

        for candidate in response.candidates:
            if candidate.content is not None:
                contents.append(candidate.content)

        response = generate_content(client, contents)

        if response.function_calls:
            for function_call_part in response.function_calls:
                content = call_function(
                    function_call_part=function_call_part, verbose=args.verbose
                )

                assert isinstance(content.parts, list), "Content parts must be a list"

                assert isinstance(
                    content.parts[0], types.Part
                ), "Content part must be a Part instance"

                part = content.parts[0]

                assert isinstance(
                    part.function_response, types.FunctionResponse
                ), "Content part must have a function response"

                function_response = part.function_response.response

                assert isinstance(
                    function_response, dict
                ), "Function response must be a dictionary"

                if args.verbose:
                    print(f"-> {function_response}")

                contents.append(content)
        else:
            print(f"Final response:\n{response.text}")

    if args.verbose:
        metadata = response.usage_metadata
        assert isinstance(metadata, types.GenerateContentResponseUsageMetadata)

        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {metadata.prompt_token_count}")
        print(f"Response tokens: {metadata.candidates_token_count}")

    return


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An exception occurred: {e}")
        exit(1)
