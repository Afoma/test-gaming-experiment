from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()

def ask_model(prompt_string):
    response = client.responses.create(
    model="gpt-6-luna",
    input=prompt_string,
    )   
    return (response.output_text)

if __name__ == "__main__":
    print (ask_model("Say no"))