from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
import sys

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


client = OpenAI()

try:
     response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          max_tokens=50,
          temperature=0,
          messages=[{"role": "user", "content": "hello"}],
     )
     print(response)
except openai.RateLimitError as e:
     print(
          "OpenAI API returned 429 'insufficient_quota'. "
          "Please check your plan/billing: https://platform.openai.com/account/billing.\n"
          "After adding credits or increasing quota, rerun this script.",
          flush=True,
     )
     sys.exit(1)
except Exception as e:
     print(f"OpenAI API error: {e}", flush=True)
     sys.exit(1)
