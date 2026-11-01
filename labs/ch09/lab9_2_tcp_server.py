# 实验 9-2：TCP 聊天的服务器端，先运行它（《计算机网络》第 9 章）
import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # SOCK_STREAM 表示 TCP
srv.bind(("127.0.0.1", 9000))                             # ← 改这里：端口号
srv.listen()                                              # 开始等待连接
print("服务器在 9000 端口等待连接……")
conn, addr = srv.accept()                                 # 三次握手在这里完成
print("有人连上来了：", addr)
while True:
    msg = conn.recv(1024)                                 # 收数据，最多 1024 字节
    if not msg:                                           # 对方关闭了连接
        break
    print("收到：", msg.decode())
    conn.sendall(("收到：" + msg.decode()).encode())       # 回复对方
conn.close()
print("连接已关闭")
