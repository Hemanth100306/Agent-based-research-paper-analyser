from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from metadata_fetcher import fetch_papers

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_papers(query, top_k=3):
    papers = fetch_papers(query, max_results=10)

    abstracts = [p["abstract"] for p in papers]
    embeddings = model.encode(abstracts)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for idx in indices[0]:
        results.append({
            "title": papers[idx]["title"],
            "abstract": papers[idx]["abstract"],
            "pdf_url": papers[idx]["pdf_url"]
        })

    return results
