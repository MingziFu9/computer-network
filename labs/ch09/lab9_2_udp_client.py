# 实验 9-2 改一改：UDP 版客户端（《计算机网络》第 9 章）
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for text in ["你好，我是小林", "今晚六点开会"]:
    c.sendto(text.encode(), ("127.0.0.1", 9001))          # 不用 connect，直接发
    print(c.recvfrom(1024)[0].decode())
c.close()
