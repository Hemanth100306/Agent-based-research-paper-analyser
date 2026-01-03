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
        div.innerHTML = "";

        data.forEach(paper => {
            div.innerHTML += `
                <div class="card">
                    <h3>${paper.title}</h3>
                    <p>${paper.abstract}</p>
                    <a href="/view-pdf?url=${encodeURIComponent(paper.pdf_url)}" target="_blank">
                        View / Download PDF
                    </a>
                </div>
            `;
        });
    });
}
