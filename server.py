#!/usr/bin/env python

import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import simplejson
from mcp4726 import mcp4726

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


    def do_GET(self):
        # TODO return version?
        pass

    def do_POST(self):
        data_json = self.rfile.read(int(self.headers['Content-Length']))
        data = simplejson.loads(data_json)
        try:
            i2c_client = mcp4726()
            for i in data["data"]:
                # todo convert samples to voltage and send with correct freq
                i2c_client.send(i)
            self._send_response(200)
        except Exception as e:
            self._send_response(500, repr(e))

    def _send_response(self, code, message="unknown"):
        self.send_response(code, message)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if code != 200:
            resp = simplejson.dumps({"code": code, "error": message})
            self.wfile.write(resp.encode())


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)