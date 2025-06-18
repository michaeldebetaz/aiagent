from pathlib import Path


def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory_path = Path(working_directory).resolve()
    if not working_directory_path.is_dir():
        return f"Error: {working_directory} is not a valid directory"

    path = (working_directory_path / Path(file_path)).resolve()
    if path != working_directory_path and working_directory_path not in path.parents:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not path.exists():
        try:
            path.touch()
        except Exception as e:
            return f"Error creating file: {e}"

    if path.exists() and not path.is_file():
        return f'Error: Cannot write to "{file_path}" as it is not a regular file'

    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
            return f'Successfully write to"{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"
