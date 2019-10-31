from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SocketServer

from urlparse import urlparse

class ServerHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        query = urlparse(self.path).query
        name = query.split('=')[1]

        with open('files/' + name, 'w') as file:
            file.write(post_body)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write("File successfuly loaded")

        return

server = SocketServer.TCPServer(("", 8080), ServerHandler)

print("Server is working!")

server.serve_forever()