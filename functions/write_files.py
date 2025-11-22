import os
from google.genai import types

def write_file(working_directory, file_path, content):

    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    try:
        with open(abs_path,'w') as f:
            f.write(content)
        return f'Successfully wrote to "{abs_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: unable to write file: {e}'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes content to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
    ),
)