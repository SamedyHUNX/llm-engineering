# Scraper is outside the folder
# We need this helper to use scraper.py
import sys
from pathlib import Path
sys.path.append(str(Path("..").resolve()))
from scraper import fetch_website_contents

def get_contents(address):
    contents = fetch_website_contents(address)
    return contents

def messages_for_summarization(system_prompt, user_prompt_prefix, website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

def summarize(openai, request_obj, url):
    response = openai.chat.completions.create(
        model = "llama3.2",
        messages = request_obj
    )
    return response.choices[0].message.content