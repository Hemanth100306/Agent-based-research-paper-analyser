from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from metadata_fetcher import fetch_papers
from semantic_fetcher import fetch_semantic_papers
from query_expander import expand_query
from answer_generator import generate_answer

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_papers(query, top_k=5):
    expanded_queries = expand_query(query)
    all_papers = []

    for q in expanded_queries:
        all_papers.extend(fetch_papers(q, max_results=3))
        all_papers.extend(fetch_semantic_papers(q, limit=3))

    valid_papers = [p for p in all_papers if p.get("abstract")]

    abstracts = [p["abstract"] for p in valid_papers]
    embeddings = model.encode(abstracts)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []

    for rank, idx in enumerate(indices[0]):
        distance = float(distances[0][rank]) 
        relevance = float(round(100 / (1 + distance), 2))

        paper = valid_papers[idx]

        results.append({
            "title": str(paper["title"]),
            "abstract": str(paper["abstract"]),
            "pdf_url": str(paper["pdf_url"]),
            "source": str(paper["source"]),
            "relevance": relevance
        })

    safe_results = []
    for r in results:
        safe_results.append({
            k: float(v) if isinstance(v, (int, float)) else v
            for k, v in r.items()
        })

    answer = generate_answer(query, safe_results)

    return {
        "answer": str(answer),
        "papers": safe_results
    }
