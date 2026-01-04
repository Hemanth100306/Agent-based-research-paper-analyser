import requests

SEMANTIC_API = "https://api.semanticscholar.org/graph/v1/paper/search"

def fetch_semantic_papers(query, limit=5):
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,abstract,url,openAccessPdf"
    }

    response = requests.get(SEMANTIC_API, params=params, timeout=10)
    data = response.json()

    papers = []
    for item in data.get("data", []):
        pdf_url = None
        if item.get("openAccessPdf"):
            pdf_url = item["openAccessPdf"].get("url")

        if pdf_url:
            papers.append({
                "title": item["title"],
                "abstract": item.get("abstract", ""),
                "pdf_url": pdf_url,
                "source": "semantic_scholar"
            })

    return papers
