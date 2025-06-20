from pathlib import Path


def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory_path = Path(working_directory).resolve()
    if not working_directory_path.is_dir():
        return f"Error: {working_directory} is not a valid directory"

    path = (working_directory_path / Path(file_path)).resolve()

    if path != working_directory_path and working_directory_path not in path.parents:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path, "r", encoding="utf-8") as file:
            MAX_CHARS = 10_000
            content = file.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += (
                    f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return content
    except Exception as e:
        return f"Error reading file: {e}"
