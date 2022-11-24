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
		try:
			print(self.path)
			text = self.path.split('?')
			print(text)
			args = text[len(text) - 1].split('&')
			print(args)
			argname  = args[0].split('=')[0]
			argname2 = args[1].split('=')[0]
	
			num1 = 0
			num2 = 0
			if argname == 'num1':
				num1 = int(args[0].split('=')[1])
			if argname2 == 'num2':
				num2 = int(args[1].split('=')[1])
			if argname == 'num2':
				num2 = int(args[0].split('=')[1])
			if argname2 == 'num1':
				num1 = int(args[1].split('=')[1])
			
			self.do_header()
			self.wfile.write(bytes('{"sum":%s,"sub":%s,"mul":%s,"div":%s,"mod":%s}' % (int(num1)+int(num2), int(num1)-int(num2), int(num1)*int(num2), int(int(num1)/int(num2)), int(num1)%int(num2)), self.encoding))
		except Exception as e:
			print(e)
		
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
