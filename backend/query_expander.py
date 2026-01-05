from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def expand_query(query):
    prompt = f"""
    Expand the following research topic into 4 related academic search terms.
    Return only comma-separated terms.

    Topic: {query}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    text = response.choices[0].message.content.strip()
    return [t.strip() for t in text.split(",")]
