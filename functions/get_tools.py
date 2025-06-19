from google.genai import types


def get_tools() -> types.ToolListUnion:
    get_files_info_function_declaration = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    get_file_content_function_declaration = types.FunctionDeclaration(
        name="get_file_content",
        description="Retrieves the content of a file in the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to read, relative to the working directory.",
                ),
            },
        ),
    )

    run_python_file_function_declaration = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes a Python file in the working directory with optional arguments.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the Python file to execute, relative to the working directory.",
                ),
            },
        ),
    )

    write_file_function_declaration = types.FunctionDeclaration(
        name="write_file",
        description="Writes or overwrites a file in the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to write, relative to the working directory.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to write to the file.",
                ),
            },
        ),
    )

    return [
        types.Tool(
            function_declarations=[
                get_files_info_function_declaration,
                get_file_content_function_declaration,
                run_python_file_function_declaration,
                write_file_function_declaration,
            ]
        )
    ]
