from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import led

class MyServer:
  def __init__(self):
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

class MyHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    led.light_up()
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write('LED activated')
    return

print('listening at http://localhost:8080')
MyServer()
