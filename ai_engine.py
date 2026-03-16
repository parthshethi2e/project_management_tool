import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_tasks(requirement):

    prompt = f"""
You are an AI project manager.

A development team has:
- Android Developer
- iOS Developer
- Web Developer

Generate tasks for each developer.

Requirement:
{requirement}

Return ONLY valid JSON in this format:

{{
"android": ["task1","task2"],
"ios": ["task1","task2"],
"web": ["task1","task2"]
}}
"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()["choices"][0]["message"]["content"]

    # Remove markdown if AI adds it
    result = result.replace("```json", "").replace("```", "").strip()

    return result


def generate_summary(requirement):

    prompt = f"""
    Summarize the following project requirement in 3 sentences.

    Requirement:
    {requirement}
    """

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()["choices"][0]["message"]["content"]