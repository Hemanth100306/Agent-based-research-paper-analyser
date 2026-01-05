from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, papers):
    context = "\n\n".join([paper["abstract"] for paper in papers])

    prompt = f"""
    Answer the question using ONLY the information from the abstracts below.
    Do not add external knowledge.

    Question:
    {query}

    Abstracts:
    {context}

    Answer:
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
