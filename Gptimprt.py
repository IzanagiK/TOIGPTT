from main import OPENAI_API_KEY
import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003", prompt="Create a dance text in five lines", temperature=0, max_tokens=7)