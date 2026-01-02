import requests
from flask import Response

def stream_pdf(pdf_url):
    r = requests.get(pdf_url, stream=True, timeout=10)

    return Response(
        r.iter_content(chunk_size=1024),
        content_type="application/pdf"
    )
