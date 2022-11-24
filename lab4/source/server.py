#!/usr/bin/env python3
import http.server
import socketserver

class web_server(http.server.SimpleHTTPRequestHandler):
	encoding = 'utf-8'

	def do_header(self):
		self.protocol_version = 'HTTP/1.1'
		self.send_response(200)
		self.send_header("Content-type", "text/html; charset=UTF-8")
		self.end_headers()

	def do_GET(self):
		print(self.path)
		super().do_GET()

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
