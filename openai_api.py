import os
import openai
from dotenv import load_dotenv
from prompts import build_prompt

load_dotenv()

def query_watsonx(symptom_text):
    prompt = build_prompt(symptom_text)
    try:
        openai.api_key = os.getenv("WATSONX_API_KEY")

        response = openai.ChatCompletion.create(
            model=os.getenv("WATSONX_MODEL_ID"),
            messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=50
        )

        return response.choices[0].message['content'].strip()
    except Exception as e:
        print("Watsonx API error:", e)
        return "General Medicine"