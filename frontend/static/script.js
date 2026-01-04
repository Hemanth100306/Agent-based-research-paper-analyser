function search() {
    const query = document.getElementById("query").value;

    fetch("/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    })
    .then(res => res.json())
    .then(data => {
        const div = document.getElementById("results");

        div.innerHTML = `
            <h2>Answer</h2>
            <p>${data.answer}</p>
            <h2>Relevant Papers</h2>
        `;

        data.papers.forEach(paper => {
            div.innerHTML += `
                <div class="card">
                    <h3>${paper.title}</h3>
                    <p>${paper.abstract}</p>
                    <p><b>Relevance Score:</b> ${paper.relevance}</p>
                    <p><b>Source:</b> ${paper.source}</p>
                    <a href="/view-pdf?url=${encodeURIComponent(paper.pdf_url)}" target="_blank">
                        View / Download PDF
                    </a>
                </div>
            `;
        });
    })
    .catch(err => {
        console.error("Search error:", err);
    });
}
