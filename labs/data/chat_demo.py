"""录制抓包用：自动说两句话的 TCP / UDP 聊天。用法：python chat_demo.py server|client tcp|udp [服务器IP]"""
import socket
import sys
import time

role, kind = sys.argv[1], sys.argv[2]
PORT = 9000 if kind == "tcp" else 9001
typ = socket.SOCK_STREAM if kind == "tcp" else socket.SOCK_DGRAM
s = socket.socket(socket.AF_INET, typ)
if role == "server":
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", PORT))
    if kind == "tcp":
        s.listen(1)
        conn, addr = s.accept()
        for _ in range(2):
            msg = conn.recv(1024)
            conn.sendall("收到：".encode() + msg)
        conn.close()
    else:
        for _ in range(2):
            msg, addr = s.recvfrom(1024)
            s.sendto("收到：".encode() + msg, addr)
else:
    host = sys.argv[3]
    if kind == "tcp":
        s.connect((host, PORT))
        for text in ["你好，我是小林", "今晚六点开会"]:
            s.sendall(text.encode()); s.recv(1024); time.sleep(0.2)
    else:
        for text in ["你好，我是小林", "今晚六点开会"]:
            s.sendto(text.encode(), (host, PORT)); s.recvfrom(1024); time.sleep(0.2)
s.close()
