import os
import dotenv
from google import genai
from google.genai import types
import argparse


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
    model = "gemini-2.0-flash-001"
    contents = types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    response = client.models.generate_content(model=model, contents=contents)

    print(response.text)

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
