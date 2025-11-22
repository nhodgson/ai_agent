import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.write_files import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.get_file_content import schema_get_file_content
from functions.call_function import call_function

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def main():

    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

If a function is provided without arguements run anyway.
"""

    client = genai.Client(api_key=API_KEY)

    config = types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[available_functions])
    
    for i in range(20):
        
        response = client.models.generate_content(
                        model='gemini-2.0-flash-001',
                        contents=messages,
                        config=config,
            )
        if (response.function_calls is None) and (response.text != ''):
            break

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.function_calls is not None:
            for fc in response.function_calls:
                r = call_function(fc)
                if not r.parts[0].function_response.response:
                    raise Exception('Error: No response')
                else:
                    if '--verbose' in sys.argv:
                        print(f"-> {r.parts[0].function_response.response}")

                    messages.append(
                        types.Content(
                            role="user", 
                            parts=[types.Part(text=r.parts[0].function_response.response['result'])])
                    )



    print(response.text)

    if '--verbose' in sys.argv:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()
