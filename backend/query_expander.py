from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def expand_query(query):
    prompt = f"""
    Expand the following research topic into 4 related academic search terms:
    Topic: {query}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    expanded = response.choices[0].message.content
    if expanded is None:
        return []
    terms = [t.strip() for t in expanded.split(",")]
    return terms
