from dotenv import load_dotenv
from openai import OpenAI
import subprocess
import re
import shutil
import tempfile

load_dotenv()
client=OpenAI()

FORMAT_INSTRUCTIONS = 'Reply with the complete contents of the file inside a single ```solidity code block, and nothing else.'

def ask_model(messages):
    response = client.responses.create(
    model="gpt-6-luna",
    input=messages,
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

def make_working_copy(task_folder):
    temp_path = tempfile.mkdtemp()
    destination = temp_path + "/task"
    shutil.copytree(task_folder, destination, ignore=shutil.ignore_patterns('out', 'cache'))
    return destination

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def run_episode(task_folder, source_file, max_tries=8):
    # 1. Make a clean working copy so the original never changes
    work_folder = make_working_copy(task_folder)
    source_path = work_folder + "/src/" + source_file

    # 2. Build the first message: description + stub + format instruction
    description = read_file(work_folder + "/description.txt")
    stub = read_file(source_path)
    first_prompt = (
        description
        + "\n\nHere is the file src/" + source_file + ":\n\n"
        + stub
        + "\n\n" + FORMAT_INSTRUCTIONS
    )

    # 3. Start the message history (the AI remembers nothing, so we resend it every time)
    messages = [{'role': 'user', 'content': first_prompt}]

    for attempt in range(1, max_tries + 1):
        # Ask the model and save its reply to the history
        reply = ask_model(messages)
        messages.append({'role': 'assistant', 'content': reply})

        # Pull the code out of the reply
        code = extract_code(reply)
        if code is None:
            messages.append({
                'role': 'user',
                'content': "I couldn't find a code block. " + FORMAT_INSTRUCTIONS
            })
            continue

        # Write the code into the working copy and test it
        overwrite_extracted_code(source_path, code)
        passed, output = run_tests(work_folder)

        if passed:
            return {'success': True, 'attempts': attempt, 'folder': work_folder}

        # Tests failed: tell the model and go around again
        messages.append({
            'role': 'user',
            'content': "The tests failed. Here is the output:\n\n" + output
                       + "\n\nPlease fix it. " + FORMAT_INSTRUCTIONS
        })

    return {'success': False, 'attempts': max_tries, 'folder': work_folder}


if __name__ == "__main__":
    result = run_episode("tasks/task_sum", "Sum.sol")
    print(result)
    #copy_path = make_working_copy('tasks/task_sum')
    #print(copy_path)
    #print(response.choices[0].message.content)

    #fake = "Here you go:\n```solidity\ncontract A {}\n```\nDone."
    #print(extract_code(fake))
    #overwrite_extracted_code("test_output.sol", "contract B {}")
    #passed, output = run_tests("tasks/task_sum")
    #print(passed)
    #print(output)