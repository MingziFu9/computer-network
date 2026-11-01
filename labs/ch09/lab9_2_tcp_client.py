# 实验 9-2：TCP 聊天的客户端，服务器运行后再运行它（《计算机网络》第 9 章）
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 9000))                            # 发起三次握手
print("已连接，本机地址和端口：", c.getsockname())
for text in ["你好，我是小林", "今晚六点开会"]:            # ← 改这里：要说的话
    c.sendall(text.encode())                              # 文字变成字节再发送
    print(c.recv(1024).decode())                          # 等服务器回复
c.close()                                                 # 发起四次挥手
