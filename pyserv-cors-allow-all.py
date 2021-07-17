#!/usr/bin/python3
import http.server as serv
import sys

class CORSServ(serv.SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header('Access-Control-Allow-Origin', '*')
        return super().end_headers()

def run(server_class=serv.ThreadingHTTPServer, handler_class=serv.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f"running port={server_address[1]}")
    httpd.serve_forever()

run(handler_class=CORSServ)
