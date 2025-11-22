from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_files import write_file
from functions.run_python_file import run_python_file

from google.genai import types

FUNC_DICT = {
    'get_files_info': get_files_info,
    'get_file_content': get_file_content,
    'write_file': write_file,
    'run_python_file': run_python_file
}

def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    args = function_call_part.args
    args['working_directory'] = './calculator'

    func_name = function_call_part.name

    if func_name not in FUNC_DICT:
        return types.Content(
            role="tool",
            parts=[
            types.Part.from_function_response(
                name=func_name,
                response={"error": f"Unknown function: {func_name}"},
                )   
            ],
        )
    
    else:

        res = FUNC_DICT[function_call_part.name](**args)

        return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=func_name,
                        response={"result": res},
                    )
                ],
            )

