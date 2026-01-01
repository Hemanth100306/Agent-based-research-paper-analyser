from flask import Flask, render_template, request, jsonify, Response
from rag_engine import search_papers
from pdf_proxy import stream_pdf

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query")
    results = search_papers(query)
    return jsonify(results)

@app.route("/view-pdf")
def view_pdf():
    pdf_url = request.args.get("url")
    return stream_pdf(pdf_url)

if __name__ == "__main__":
    app.run(debug=True)
