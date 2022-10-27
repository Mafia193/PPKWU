#!/usr/bin/env python3
import http.server
import socketserver
import time

class web_server(http.server.SimpleHTTPRequestHandler):
	encoding = 'utf-8'

	def do_header(self):
		self.protocol_version = 'HTTP/1.1'
		self.send_response(200)
		self.send_header("Content-type", "text/html; charset=UTF-8")
		self.end_headers()

	def do_GET(self):
		print(self.path)

		if self.path == '/':
			self.do_header()
			self.wfile.write(b"Hello World!\n")
		elif self.path.startswith('/cmd=time'):
			self.do_header()
			now = time.localtime()
			current_time = time.strftime("%H:%M:%S", now)
			self.wfile.write(current_time.encode(self.encoding))
		elif self.path.startswith('/cmd=rev'):
			self.do_header()
			str = self.path.split('&str=')
			if len(str) > 1:
				rev_str = str[1][::-1]
				self.wfile.write(rev_str.encode(self.encoding))				
		else:
			super().do_GET()

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
