"""录制抓包用的小网站：GET 返回网页，POST /login 返回“登录成功”。可选 HTTPS。
用法：python tiny_server.py 网站目录 端口 [证书 私钥]"""
import ssl
import sys
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    server_version = "XiaoheWeb/1.0"
    protocol_version = "HTTP/1.1"
    sys_version = ""

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        self.rfile.read(length)
        body = "<html><body><h1>登录成功，欢迎回来！</h1></body></html>".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


root, port = sys.argv[1], int(sys.argv[2])
httpd = HTTPServer(("0.0.0.0", port), partial(Handler, directory=root))
if len(sys.argv) > 4:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(sys.argv[3], sys.argv[4])
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
