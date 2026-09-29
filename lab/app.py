"""Intentionally vulnerable, synthetic-data-only local security lab.

The server binds exclusively to loopback. Do not change the bind address or
expose/forward this port. This is a teaching fixture, not production software.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

HOST = "127.0.0.1"
PORT = 8000

# Fabricated data. These records contain no real people or credentials.
RECORDS = {
    "1001": {"name": "Alex Example", "plan": "Basic", "note": "Synthetic record A"},
    "1002": {"name": "Morgan Sample", "plan": "Premium", "note": "Synthetic record B"},
}

PAGE_STYLE = """
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 680px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #1f2937; background-color: #ffffff; }
  h1 { border-bottom: 2px solid #2563eb; padding-bottom: 8px; color: #111827; }
  a { color: #2563eb; text-decoration: none; font-weight: 500; }
  a:hover { text-decoration: underline; }
  ul { padding-left: 20px; }
  li { margin-bottom: 8px; }
  .badge { display: inline-block; padding: 4px 10px; background: #fef3c7; color: #92400e; border: 1px solid #fde68a; border-radius: 6px; font-size: 13px; margin-bottom: 16px; }
  form { margin-top: 24px; padding: 20px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; }
  label { font-weight: 500; margin-right: 8px; }
  input { padding: 8px 12px; font-size: 14px; border: 1px solid #d1d5db; border-radius: 6px; margin: 0 8px; width: 220px; }
  button { padding: 8px 18px; font-size: 14px; background: #2563eb; color: #ffffff; border: none; border-radius: 6px; cursor: pointer; font-weight: 500; }
  button:hover { background: #1d4ed8; }
  .card { padding: 20px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; margin-top: 20px; }
  .back { margin-top: 24px; display: inline-block; }
"""


class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        if parsed.path == "/favicon.ico":
            self.send_response(204)
            self.send_header("Connection", "close")
            self.end_headers()
            return

        if parsed.path == "/":
            body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Local Security Lab</title>
<style>{PAGE_STYLE}</style>
</head>
<body>
<h1>Local Security Lab</h1>
<div class="badge">Deliberately vulnerable demo &bull; Synthetic data only &bull; Loopback use only</div>
<p>Welcome to the local practice lab. Select a profile or test the search below:</p>
<ul>
  <li><a href='/profile?id=1001'>Synthetic Profile 1001 (Alex Example)</a></li>
  <li><a href='/profile?id=1002'>Synthetic Profile 1002 (Morgan Sample)</a></li>
</ul>
<form action='/search' method='get'>
  <label for='q'>Search term</label>
  <input id='q' name='q' placeholder='e.g. security'>
  <button type='submit'>Search</button>
</form>
</body>
</html>"""
            self.respond(body)
            return

        if parsed.path == "/profile":
            record_id = params.get("id", [""])[0]
            record = RECORDS.get(record_id)
            if record is None:
                body = f"""<!doctype html><html><head><meta charset=utf-8><title>Not Found</title><style>{PAGE_STYLE}</style></head>
<body><h1>Not found</h1><p>Record ID <code>{record_id}</code> was not found.</p><a class='back' href='/'>&larr; Back to Lab</a></body></html>"""
                self.respond(body, 404)
                return
            # INTENTIONAL IDOR: the caller can select any synthetic record by ID.
            body = f"""<!doctype html>
<html>
<head><meta charset=utf-8><title>Profile {record_id}</title><style>{PAGE_STYLE}</style></head>
<body>
<h1>Profile {record_id}</h1>
<div class="card">
  <p><strong>Name:</strong> {record['name']}</p>
  <p><strong>Plan:</strong> {record['plan']}</p>
  <p><strong>Note:</strong> {record['note']}</p>
</div>
<a class='back' href='/'>&larr; Back to Lab</a>
</body>
</html>"""
            self.respond(body)
            return

        if parsed.path == "/search":
            query = params.get("q", [""])[0]
            # INTENTIONAL REFLECTED HTML INJECTION: query is not HTML-escaped.
            body = f"""<!doctype html>
<html>
<head><meta charset=utf-8><title>Search Results</title><style>{PAGE_STYLE}</style></head>
<body>
<h1>Search results</h1>
<div class="card">
  <p>You searched for: {query}</p>
</div>
<a class='back' href='/'>&larr; Back to Lab</a>
</body>
</html>"""
            self.respond(body)
            return

        body = f"""<!doctype html><html><head><meta charset=utf-8><title>Not Found</title><style>{PAGE_STYLE}</style></head>
<body><h1>Not found</h1><p>The requested path <code>{parsed.path}</code> was not found.</p><a class='back' href='/'>&larr; Back to Lab</a></body></html>"""
        self.respond(body, 404)

    def respond(self, body, status=200):
        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Connection", "close")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(payload)
        self.wfile.flush()
        self.close_connection = True

    def log_message(self, fmt, *args):
        # Keep the demo's console output minimal; no query data is logged.
        print(f"{self.client_address[0]} - {fmt % args}")


class ThreadedLabServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    print(f"Local-only lab running at http://{HOST}:{PORT}/ (Ctrl+C to stop)", flush=True)
    server = ThreadedLabServer((HOST, PORT), LabHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nLab server stopped.")
    finally:
        server.server_close()
