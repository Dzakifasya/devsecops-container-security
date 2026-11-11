from http.server import HTTPServer, BaseHTTPRequestHandler

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Secure Dockerfile Lab</h1><p>Application is running!</p>")

server = HTTPServer(("0.0.0.0", 8080), AppHandler)
print("Server running on port 8080")
server.serve_forever()
