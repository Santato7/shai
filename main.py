from rich import print
from rich.markdown import Markdown
import sys
import google.generativeai as genai
from config import Config

def print_help():
    print("Usage: shai [options] <prompt>")
    print("Options:")
    print("-h | --help: Show this help message")
    print("-b | --bash: Generate a bash command")
    print("-c | --code: Generate code in multiple programming languages")
    exit(0)

if len(sys.argv) < 2:
    print_help()
args = sys.argv
prompt = sys.argv[len(sys.argv) - 1]
system_instruction = """
Avoid recitation. You are a polyglot assistant. You can communicate in multiple human languages. 
Gimme a concise response **Remember, the output monitor has only 20 lines. 
Any response exceeding that limit will result in lost information.**
"""

for arg in args:
    match arg:
        case "-h" | "--help":
            print_help()
        case "-b" | "--bash":
            system_instruction = """
            Avoid recitation. You are an expert at using shell commands. You can generate shell code to perform various tasks. 
            Never output any text before or after the shell code, as the output will be directly executed in a shell. 
            Use Markdown. You're allowed to chain commands like `ls | grep .txt`. And if there's another way to do it, 
            you always need to provide it in a new line to a maximum of 3 commands.
            """
        case "-c" | "--code":
            system_instruction = """
            Avoid recitation. You are a polyglot programming assistant. You understand and generate code in many programming languages, 
            and you can communicate in multiple human languages. Gimme a concise response.
            """

config = Config()
API_KEY = config.get_api_key()
SAFETY_SETTINGS = {
    "HARASSMENT": "block_none",
    "HATE": "block_none",
    "SEXUALLY_EXPLICIT": "block_none",
    "DANGEROUS": "block_none",
}

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_instruction)

response = model.generate_content(contents=prompt, safety_settings=SAFETY_SETTINGS)
md = Markdown(response.candidates[0].content.parts[0].text.strip())
print(md)
exit(0)
