from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from metadata_fetcher import fetch_papers
from query_expander import expand_query

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_papers(query, top_k=3):
    expanded_queries = expand_query(query)
    all_papers = []

    for q in expanded_queries:
        papers = fetch_papers(q, max_results=5)
        all_papers.extend(papers)

    abstracts = [p["abstract"] for p in all_papers]
    embeddings = model.encode(abstracts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for idx in indices[0]:
        paper = all_papers[idx]
        results.append({
            "title": paper["title"],
            "abstract": paper["abstract"],
            "pdf_url": paper["pdf_url"]
        })

    return results
