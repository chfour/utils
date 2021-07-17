#!/usr/bin/python3
# original: https://gist.github.com/dergachev/7028596

# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443

# actually now you have to run python3 simple-https-server.py [portname]
from http.server import SimpleHTTPRequestHandler, HTTPServer
import ssl, sys

httpd = HTTPServer(('0.0.0.0', int(sys.argv[1])), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
