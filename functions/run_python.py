from pathlib import Path
import subprocess


def run_python_file(working_directory: str, file_path: str) -> str:
    working_directory_path = Path(working_directory).resolve()
    if not working_directory_path.is_dir():
        return f"Error: {working_directory} is not a valid directory"

    path = (working_directory_path / Path(file_path)).resolve()

    if path != working_directory_path and working_directory_path not in path.parents:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not path.exists():
        return f'Error: File "{file_path}" not found.'

    if not (path.is_file() and path.suffix == ".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        output = subprocess.run(
            ["python", path],
            timeout=30,
            cwd=working_directory_path,
            capture_output=True,
            text=True,
        )

        lines: list[str] = []

        stdout, stderr = output.stdout.strip(), output.stderr.strip()
        if stdout != "":
            lines.append(f"STDOUT:\n{stdout}")
        if stderr != "":
            lines.append(f"STDERR:\n{stderr}")
        if output.returncode != 0:
            lines.append(f"Process exited with code {output.returncode}")

        if len(lines) == 0:
            return "No output produced"

        return "\n".join(lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"
