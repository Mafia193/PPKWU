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

		if self.path[0] == '/':
			self.do_header()
			str = self.path.split('&str=')
			text = str[len(str) - 1]
			if len(text) <= 1:
				self.wfile.write(bytes("{{ \"lowercase\" : 0, \"uppercase\" : 0, \"digits\" : 0, \"special\" : 0}}".format(), self.encoding))
				return 
			lower = sum(1 for c in text if c.islower())
			upper = sum(1 for c in text if c.isupper())
			digit = sum(1 for c in text if c.isdigit())
			space = sum(1 for c in text if c.isspace())
			other = len(text) - upper - lower - digit - space
			self.wfile.write(bytes("{{ \"lowercase\" : {}, \"uppercase\" : {}, \"digits\" : {}, \"special\" : {}}}".format(lower, upper, digit, other), self.encoding))
		else:
			super().do_GET()

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
