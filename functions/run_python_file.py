import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):

    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        res = subprocess.run(["python", abs_path] + args, capture_output=True, timeout=30)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    if res.returncode != 0:
        return f"Process exited with code {res.returncode}"

    return f'STDOUT: {res.stdout}\nSTDERR: {res.stderr}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to run",
            ),
            "args": types.Schema(
                type=types.Type.OBJECT,
                description="A list of arguments as input",
            ),
        },
    ),
)