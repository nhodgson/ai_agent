import os
from google.genai import types

def get_files_info(working_directory, directory="."):

    abs_path = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    contents = []

    for f in os.listdir(abs_path):
        try:
            d = os.path.join(abs_path, f)
            file_size = os.path.getsize(d)
            isdir = os.path.isdir(d)
            contents.append(f'{f} file_size={file_size} bytes, is_dir={isdir}')
        except Exception as e:
            return f'Error: {e}'
        
    return '\n'.join(contents)

schema_get_files_info = types.FunctionDeclaration(
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