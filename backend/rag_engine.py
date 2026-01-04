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

        if (!Array.isArray(data) || data.length === 0) {
            resultsDiv.innerHTML = "<p>No results found.</p>";
            return;
        }

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
