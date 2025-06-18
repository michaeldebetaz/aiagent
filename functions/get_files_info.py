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
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not path.is_dir():
        return f"Error: {directory} is not a directory"

    lines: list[str] = []
    for file in path.iterdir():
        line = f"- {file.name}: file_size={file.stat().st_size} bytes, is_dir={file.is_dir()}"
        lines.append(line)

    return "\n".join(lines)
