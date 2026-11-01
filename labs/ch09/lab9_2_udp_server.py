# 实验 9-2 改一改：UDP 版服务器（《计算机网络》第 9 章）
import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # SOCK_DGRAM 表示 UDP
srv.bind(("127.0.0.1", 9001))
print("UDP 服务器在 9001 端口等待……")
for _ in range(2):                                        # 收两条就结束
    msg, addr = srv.recvfrom(1024)                        # 不用 accept，没有连接
    print("收到", addr, "：", msg.decode())
    srv.sendto(("收到：" + msg.decode()).encode(), addr)
