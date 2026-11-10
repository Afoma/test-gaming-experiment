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

def extract_code(reply):
    match = re.search(r"```solidity\n(.*?)```", reply, re.DOTALL)
    if match:
        return match.group(1)
    return None                

def overwrite_extracted_code(file_path, code):
    with open(file_path, 'w') as file:
        file.write(code)

if __name__ == "__main__":
    #fake = "Here you go:\n```solidity\ncontract A {}\n```\nDone."
    #print(extract_code(fake))
    overwrite_extracted_code("test_output.sol", "contract B {}")
    #passed, output = run_tests("tasks/task_sum")
    #print(passed)
    #print(output)