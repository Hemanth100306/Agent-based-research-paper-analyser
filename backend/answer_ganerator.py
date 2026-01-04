from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def generate_answer(query, papers):
    context = ""

    for p in papers:
        context += f"Title: {p['title']}\nAbstract: {p['abstract']}\n\n"

    prompt = f"""
    Answer the following research query using the provided paper abstracts.
    Do not mention papers explicitly.
    Keep the answer concise and academic.

    Query: {query}

    Context:
    {context}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
