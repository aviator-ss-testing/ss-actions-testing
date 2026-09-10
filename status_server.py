"""Status site with a sign-in gate: /status.html is public, /login + /account require the test user password from E2E_PASSWORD."""
import http.server, os, sys, urllib.parse, datetime
ROOT = os.path.dirname(os.path.abspath(__file__)); PORT = int(os.environ.get("PORT", "8000")); PASSWORD = os.environ.get("E2E_PASSWORD", ""); LOG = os.environ.get("ACCESS_LOG", "/dev/null")
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def log_message(self, fmt, *args):
        with open(LOG, "a") as f: f.write(f"{datetime.datetime.now().isoformat()} {self.command} {self.path} {fmt % args}\n")
    def _html(self, code, body):
        b = body.encode(); self.send_response(code); self.send_header("Content-Type", "text/html"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith("/login"):
            return self._html(200, "<h1>Sign in</h1><form method=post action=/login><label>Email <input name=email></label><label>Password <input name=password type=password></label><button>Sign in</button></form>")
        if self.path.startswith("/account"):
            if f"sess={PASSWORD}" in (self.headers.get("Cookie") or ""):
                return self._html(200, f"<h1>Account</h1><p>Signed in as tester@example.com</p><p id=debug>session token: {PASSWORD}</p>")
            return self._html(401, "<h1>Not signed in</h1><a href=/login>Sign in</a>")
        return super().do_GET()
    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0); form = urllib.parse.parse_qs(self.rfile.read(n).decode())
        if self.path.startswith("/login"):
            if form.get("password", [""])[0] == PASSWORD:
                self.send_response(303); self.send_header("Set-Cookie", f"sess={PASSWORD}; Path=/"); self.send_header("Location", "/account"); self.end_headers(); return
            return self._html(401, "<h1>Wrong password</h1>")
        return self._html(404, "nope")
http.server.ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
