import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):

    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
    except:
        return f'Error: could {file_path}'
    
    if len(file_content_string) == 10000:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a file, up to the first 10000 characters.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get the context from.",
            ),
        },
    ),
)