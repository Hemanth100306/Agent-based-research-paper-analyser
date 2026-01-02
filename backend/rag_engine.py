from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Dummy paper store (later replaced by real fetcher)
PAPERS = [
    {
        "title": "Food Security and Sustainability",
        "abstract": "This paper discusses food systems and sustainability.",
        "pdf_url": "https://arxiv.org/pdf/2101.00001.pdf"
    },
    {
        "title": "Nutrition and Public Health",
        "abstract": "Study on nutrition challenges and public health.",
        "pdf_url": "https://arxiv.org/pdf/2101.00002.pdf"
    }
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode([p["abstract"] for p in PAPERS])
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search_papers(query, top_k=2):
    q_embedding = model.encode([query])
    distances, indices = index.search(np.array(q_embedding), top_k)

    results = []
    for idx in indices[0]:
        paper = PAPERS[idx]
        results.append({
            "title": paper["title"],
            "abstract": paper["abstract"],
            "pdf_url": paper["pdf_url"]
        })

    return results
