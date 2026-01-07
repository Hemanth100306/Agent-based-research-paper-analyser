function search() {
    const query = document.getElementById("query").value.trim();

    if (!query) {
        alert("Please enter a search query");
        return;
    }

    // Show loading state
    showLoading(true);
    hideEmptyState();

    fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    })
    .then(res => {
        if (!res.ok) throw new Error("Search failed");
        return res.json();
    })
    .then(data => {
        showLoading(false);
        displayResults(data);
    })
    .catch(error => {
        showLoading(false);
        console.error("Error:", error);
        alert("An error occurred while searching. Please try again.");
    });
}

function showLoading(show) {
    const loading = document.getElementById("loading");
    if (show) {
        loading.classList.remove("hidden");
    } else {
        loading.classList.add("hidden");
    }
}

function hideEmptyState() {
    document.getElementById("empty-state").classList.add("hidden");
    document.getElementById("results-section").classList.remove("hidden");
}

function displayResults(data) {
    // Display AI Answer
    const answerContent = document.getElementById("answer-content");
    answerContent.innerHTML = `<p>${escapeHtml(data.answer || "No answer available")}</p>`;

    // Display Papers
    const papersContainer = document.getElementById("papers-container");
    papersContainer.innerHTML = "";

    if (data.papers && data.papers.length > 0) {
        data.papers.forEach(paper => {
            const card = document.createElement("div");
            card.className = "card";
            card.innerHTML = `
                <h3>${escapeHtml(paper.title || "Untitled")}</h3>
                <p>${escapeHtml(paper.abstract || "No abstract available")}</p>
                <div class="meta">
                    ${paper.relevance ? `<div class="meta-item"><strong>Relevance:</strong> ${escapeHtml(paper.relevance)}</div>` : ""}
                    ${paper.source ? `<div class="meta-item"><strong>Source:</strong> ${escapeHtml(paper.source)}</div>` : ""}
                </div>
                <a href="/view-pdf?url=${encodeURIComponent(paper.pdf_url || "#")}" target="_blank" rel="noopener noreferrer">
                    📥 View PDF
                </a>
            `;
            papersContainer.appendChild(card);
        });
    } else {
        papersContainer.innerHTML = "<p style='text-align: center; color: #999;'>No papers found for this query.</p>";
    }
}

function escapeHtml(text) {
    if (!text) return "";
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

// Initialize empty state on page load
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("empty-state").classList.remove("hidden");
    document.getElementById("results-section").classList.add("hidden");
});
