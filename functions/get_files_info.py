from pathlib import Path


def get_files_info(working_directory: str, directory: str | None = None) -> str:
    working_directory_path = Path(working_directory).resolve()
    if not working_directory_path.is_dir():
        return f"Error: {working_directory} is not a valid directory"

    path = working_directory_path

    if directory is not None:
        path = (path / Path(directory)).resolve()
        if path != working_directory_path:
            if working_directory_path not in path.parents:
                return f'Error: Cannot list "{path}" as it is outside the permitted working directory'

    if not path.is_dir():
        return f"Error: {path} is not a directory"

    lines: list[str] = []
    for file in path.iterdir():
        line = f"- {file.name}: file_size={file.stat().st_size} bytes, is_dir={file.is_dir()}"
        lines.append(line)

    return "\n".join(lines)


def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory_path = Path(working_directory).resolve()
    if not working_directory_path.is_dir():
        return f"Error: {working_directory} is not a valid directory"

    path = (working_directory_path / Path(file_path)).resolve()

    if path != working_directory_path and working_directory_path not in path.parents:
        return f'Error: Cannot read "{path}" as it is outside the permitted working directory'

    if not path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path, "r", encoding="utf-8") as file:
            MAX_CHARS = 10_000
            content = file.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += f'\n[...File "{path}" truncated at 10000 characters]'

            return content
    except Exception as e:
        return f"Error reading file: {e}"


def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory_path = Path(working_directory).resolve()
    if not working_directory_path.is_dir():
        return f"Error: {working_directory} is not a valid directory"

    path = (working_directory_path / Path(file_path)).resolve()
    if path != working_directory_path and working_directory_path not in path.parents:
        return f'Error: Cannot write to "{path}" as it is outside the permitted working directory'

    if not path.is_file():
        return f'Error: Cannot write to "{path}" as it is not a regular file'

    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
            return f'Successfully write to"{path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"
