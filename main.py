import sys
import google.generativeai as genai
from config import Config

if len(sys.argv) < 2:
    print("Usage: python main.py [options] <prompt>")
    exit(1)
args = sys.argv[1:-1]
prompt = sys.argv[len(sys.argv) - 1]

if prompt.startswith('-'):
    prompt = None

config = Config()
API_KEY = config.get_api_key()
SYSTEM_INSTRUCTION = """You are an expert at using shell commands. Only provide a single executable line of shell code as output. Never output any text before or after the shell code, as the output will be directly executed in a shell. Never use backticks. You're allowed to chain commands like `ls | grep .txt`. And if there's another way to do it, you have to provide it in a new line to a maximum of 3 commands."""
SAFETY_SETTINGS = {
    'HARASSMENT':'block_none',
    'HATE':'block_none',
    'SEXUALLY_EXPLICIT':'block_none',
    'DANGEROUS':'block_none'
    }

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=SYSTEM_INSTRUCTION)

response = model.generate_content(contents=f"Here's what I'm trying to do: {prompt}", safety_settings=SAFETY_SETTINGS)
print(response.candidates[0].content.parts[0].text.strip())