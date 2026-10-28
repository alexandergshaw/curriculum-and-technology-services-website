"""Loopback preview of public site assets only; no directory or source browsing."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
ASSETS = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/curriculum-sample.html": ("curriculum-sample.html", "text/html; charset=utf-8"),
    "/ai-course-example.html": ("ai-course-example.html", "text/html; charset=utf-8"),
    "/ai-example.css": ("ai-example.css", "text/css; charset=utf-8"),
    "/ai-example.js": ("ai-example.js", "text/javascript; charset=utf-8"),
    "/styles.css": ("styles.css", "text/css; charset=utf-8"),
    "/sample.css": ("sample.css", "text/css; charset=utf-8"),
    "/script.js": ("script.js", "text/javascript; charset=utf-8"),
    "/favicon.svg": ("favicon.svg", "image/svg+xml"),
    "/downloads/illustrative-curriculum-map.csv": ("downloads/illustrative-curriculum-map.csv", "text/csv; charset=utf-8"),
    "/teaching-sample/data/cases.json": ("teaching-sample/data/cases.json", "application/json; charset=utf-8"),
    "/downloads/applied-ai-sample.zip": ("downloads/applied-ai-sample.zip", "application/zip"),
    "/output/pdf/access-capabilities.pdf": ("output/pdf/access-capabilities.pdf", "application/pdf"),
}


class Preview(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.serve_asset(False)

    def do_GET(self):
        self.serve_asset(True)

    def serve_asset(self, body):
        if self.headers.get("Host") not in ("127.0.0.1:8765", "localhost:8765"):
            self.send_error(403)
            return
        asset = ASSETS.get(urlsplit(self.path).path)
        if asset is None:
            self.send_error(404)
            return
        path, content_type = asset
        try:
            payload = (ROOT / path).read_bytes()
        except FileNotFoundError:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        if body:
            self.wfile.write(payload)


if __name__ == "__main__":
    print("Local preview: http://127.0.0.1:8765", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8765), Preview).serve_forever()
