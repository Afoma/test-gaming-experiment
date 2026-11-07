from dotenv import load_dotenv
from openai import OpenAI
import subprocess
import re

load_dotenv()
client=OpenAI()

FORMAT_INSTRUCTIONS = 'Reply with the complete contents of the file inside a single ```solidity code block, and nothing else.'

def ask_model(prompt_string):
    response = client.responses.create(
    model="gpt-6-luna",
    input=prompt_string,
    )   
    return (response.output_text)

def run_tests(task_folder):
    result = subprocess.run(['forge', 'test'],capture_output=True, text=True, cwd=task_folder, timeout=60)
    return (result.returncode == 0 , result.stdout + result.stderr)

def find_code_block(code_line):
    match_object = re.search(r"\b\w\b", code_line)
    return match_object
                            

if __name__ == "__main__":
    passed, output = run_tests("tasks/task_sum")
    print(passed)
    print(output)