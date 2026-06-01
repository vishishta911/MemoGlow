import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(context, question):

    prompt = f"""
You are MemoGlow AI, a memory assistant for dementia patients.

Use ONLY the memory information below.

Memory Context:
{context}

Question:
{question}

Answer in a simple, friendly way.
"""

    response = model.generate_content(prompt)

    return response.text