function search() {
    const queryInput = document.getElementById("query");
    const resultsDiv = document.getElementById("results");

    if (!queryInput || !resultsDiv) {
        console.error("Required DOM elements not found");
        return;
    }

    const query = queryInput.value.trim();
    if (!query) {
        resultsDiv.innerHTML = "<p>Please enter a search query.</p>";
        return;
    }

<<<<<<< HEAD
    fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        resultsDiv.innerHTML = "";
=======
    for q in expanded_queries:
        all_papers.extend(fetch_papers(q, max_results=5))
>>>>>>> 24e416453fb12faf0a23cdf6024d70de65531d52

        if (!Array.isArray(data) || data.length === 0) {
            resultsDiv.innerHTML = "<p>No results found.</p>";
            return;
        }

<<<<<<< HEAD
        data.forEach(paper => {
            resultsDiv.innerHTML += `
                <div class="card">
                    <h3>${paper.title ?? "No title available"}</h3>
                    <p>${paper.abstract ?? "No abstract available"}</p>
                    <p><b>Relevance Score:</b> ${paper.relevance ?? "N/A"}</p>
                    <a href="/view-pdf?url=${encodeURIComponent(paper.pdf_url)}" target="_blank">
                        View / Download PDF
                    </a>
                </div>
            `;
        });
    })
    .catch(error => {
        console.error("Search error:", error);
        resultsDiv.innerHTML = "<p>Something went wrong. Please try again.</p>";
    });
}
=======
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for rank, idx in enumerate(indices[0]):
        distance = distances[0][rank]

        relevance_score = round(100 / (1 + distance), 2)

        paper = all_papers[idx]
        results.append({
            "title": paper["title"],
            "abstract": paper["abstract"],
            "pdf_url": paper["pdf_url"],
            "relevance": relevance_score
        })

    return results
>>>>>>> 24e416453fb12faf0a23cdf6024d70de65531d52
